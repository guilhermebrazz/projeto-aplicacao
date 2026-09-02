# models.py: Cria o banco de dados e modela as tabelas

from sqlalchemy import create_engine, Column, Integer, Boolean, Float, String, ForeignKey # cria o banco de dados + colunas e tipos
from sqlalchemy.orm import declarative_base
#Para migrations utilize alembic

#cria a conexão do banco
db = create_engine("sqlite:///banco.db")

#cria a base do banco de dados
Base = declarative_base()

#cria as classes(tabelas) do banco
# Usuários

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)

    def __init__(self, nome: str, email: str, senha: str, ativo=True):

        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

'''class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column("id", Integer, primary_key=True ,autoincrement=True)
    nome = Column("nome", String, nullable=False)
    sexo = Column("sexo")
    nascimento = Column("nascimento")
    email = Column("email", String)
    telefone = Column("telefone", String)
    rg = Column("rg", String)
    cpf = Column("cpf", String)
    observacoes = Column("observacoes", String)

    def __init__(self, nome, sexo, nascimento, email, telefone, rg, cpf, observacoes):

        self.nome = nome
        self.sexo = sexo
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone
        self.rg = rg
        self.cpf = cpf
        self.observacoes = observacoes
        '''
# Dentistas
# Procedimentos
# 


#cria efetivamente o banco de dados
Base.metadata.create_all(db)