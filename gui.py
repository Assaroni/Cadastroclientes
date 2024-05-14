import PySimpleGUI as sg
from db import Cliente, Session
import re
from datetime import datetime

def validate_cpf(cpf):
    # Checa se o CPF tem 11 dígitos e se todos são numéricos
    if not (len(cpf) == 11 and cpf.isdigit()):
        sg.popup('CPF deve conter exatamente 11 dígitos numéricos.')
        return False
    # Validação de dígitos verificadores do CPF
    def calc_dv(nove_digitos):
        soma = sum((10 - i) * int(n) for i, n in enumerate(nove_digitos))
        dv = 11 - soma % 11
        return '0' if dv >= 10 else str(dv)
    
    dv1 = calc_dv(cpf[:-2])
    dv2 = calc_dv(cpf[:-1])
    if dv1 == cpf[-2] and dv2 == cpf[-1]:
        return True
    else:
        sg.popup('CPF inválido. Dígitos verificadores não correspondem.')
        return False

def validate_date(date_text):
    try:
        selected_date = datetime.strptime(date_text, '%d/%m/%Y')
        if selected_date > datetime.now():
            sg.popup('Data não pode ser futura.')
            return False
        return True
    except ValueError:
        sg.popup('Data de nascimento inválida. Use o formato DD/MM/AAAA.')
        return False

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        sg.popup('Email inválido. Deve conter um "@" e um ".".')
        return False

def add_cliente(values):
    if not (validate_cpf(values['cpf']) and validate_date(values['data_nascimento']) and validate_email(values['email']) and validate_date(values['data_cadastro'])):
        return

    try:
        session = Session()
        cliente = Cliente(
            nome=values['nome'],
            cpf=values['cpf'],
            data_nascimento=datetime.strptime(values['data_nascimento'], '%d/%m/%Y'),
            data_cadastro=datetime.strptime(values['data_cadastro'], '%d/%m/%Y'),
            email=values['email']
        )
        session.add(cliente)
        session.commit()
        sg.popup('Cliente adicionado com sucesso!')
    except Exception as e:
        sg.popup(f'Erro ao adicionar cliente: {str(e)}')
    finally:
        session.close()

# Tema da Interface
sg.theme('DarkBlue14')

layout = [
    [sg.Text('Sistema de Cadastro de Clientes', size=(30,1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Frame(layout=[
    [sg.Text('Nome', size=(15, 1)), sg.Input(key='nome')],
    [sg.Text('CPF', size=(15, 1)), sg.Input(key='cpf')],
    [sg.Text('Data de Nascimento', size=(15, 1)), sg.Input(key='data_nascimento'), sg.CalendarButton("Escolher Data", target='data_nascimento', format='%d/%m/%Y')],
    [sg.Text('Data do Cadastro', size=(15, 1)), sg.Input(key='data_cadastro'), sg.CalendarButton("Escolher Data", target='data_cadastro', format='%d/%m/%Y')],
    [sg.Text('Email', size=(15, 1)), sg.Input(key='email')]],
    title='Dados do Cliente', title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Button('Adicionar Cliente'), sg.Button('Sair')]
]

window = sg.Window('Sistema de Cadastro de Clientes', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Adicionar Cliente':
        add_cliente(values)

window.close()
