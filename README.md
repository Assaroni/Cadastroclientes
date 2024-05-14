# Sistema de Cadastro de Clientes

Este projeto é um sistema de cadastro de clientes desenvolvido em Python utilizando a biblioteca PySimpleGUI para a interface gráfica. Ele permite o cadastro, a listagem e a gestão de clientes de forma simples e eficaz. Este sistema também inclui validações robustas para CPF, data de nascimento, e e-mail, garantindo a integridade dos dados inseridos.

## Funcionalidades

- **Cadastro de Clientes**: Adicione clientes com informações detalhadas como nome, CPF, data de nascimento, e-mail e data de cadastro.
- **Validação de Dados**: Inclui validações para CPF (com verificação de dígitos), datas (para impedir datas futuras) e formato de e-mail.
- **Interface Gráfica Amigável**: Interface desenvolvida usando PySimpleGUI com um tema DarkBlue14, facilitando a interação do usuário.
- **Geração de Executável**: Possibilidade de converter o sistema em um executável para facilitar a distribuição e utilização em ambientes Windows.

## Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/) para ORM
- [SQLite](https://www.sqlite.org/index.html) como sistema de banco de dados (configurável para outros bancos)

## Instalação

Certifique-se de ter o Python instalado em sua máquina. É recomendável usar a versão mais recente. Python pode ser baixado [aqui](https://www.python.org/downloads/).

### Clonando o Repositório

Clone este repositório usando o seguinte comando:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
