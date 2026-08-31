from fastapi import APIRouter

auth = APIRouter(prefix="/auth", tags="auth")

@auth.get("/")
async def autenticar():
    return {"começo" : "testes"}