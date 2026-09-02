from fastapi import APIRouter, Depends
from models import Usuario
from dependicies import usar_secao

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/")
async def autenticar():
    return {"começo" : "testes"}

@router.post("/criar_conta") #envia
async def login(email: str, senha: str, nome: str, ativo: bool, session = Depends(usar_secao)): #recebe

    usuario = session.query(Usuario).filter(Usuario.email == email).all() # SELECT * FROM usuarios WHERE email = 'joao@email.com';

    if len(usuario) > 0:

        return {"mensagem": "Esse e-mail está em uso por outro usuário"}

    else:

        novo_usuario = Usuario(nome, email, senha, ativo)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Novo usuário registrado"}