# Classes (tabelas) do banco de dados

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

    def __init__(self, nome, email, senha, ativo):

        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


# Dentistas
# Procedimentos
# 


#cria efetivamente o banco de dados
Base.metadata.create_all(db)