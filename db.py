from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///clientes.db')  # Pode ser alterado para outro banco de dados
Session = sessionmaker(bind=engine)

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    data_nascimento = Column(Date)
    data_cadastro = Column(Date, default=datetime.utcnow)
    email = Column(String)

Base.metadata.create_all(engine)
