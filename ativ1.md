# Atividade 1

## 1. Quais tabelas você definiu inicialmente?

Inicialmente, defini a tabela **usuarios** com as seguintes colunas:

- **id** 
- **nome** 
- **email** 
- **senha** 
- **ativo** 

E a tabela **pacientes** com as seguintes colunas:


- **nome**
- **sexo**
- **nascimento**
- **email**
- **telefone**
- **rg**
- **cpf**
- **observacoes**

As tabelas foram definidas utilizando SQLAlchemy ORM. A ideia é que a tabela **usuarios** guarde apenas os admins do sistema (como dentistas e recepcionistas) que terão acesso ao painel administrativo, onde conseguirão "criar um novo paciente" onde preencherão os dados dele que irá direto para a tabela dos pacientes.

## 2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.

Por enquanto não foi necessário.

## 3. Qual o caminho do arquivo que gera a seed do seu banco?

O banco de dados é criado automaticamente quando a aplicação é iniciada. O arquivo responsável é `backend/models.py`, onde estão definidos o `create_engine("sqlite:///banco.db")` e a chamada `Base.metadata.create_all(db)`. O arquivo do banco SQLite gerado fica em `backend/banco.db. O banco é criado vazio e os dados são inseridos através do endpoint de cadastro de usuários.

## 4. Quais os endpoints que você irá implementar inicialmente?

- **GET /** - Página inicial onde terão funções login (caso já tenha um cadastro) e a de criar conta.

- **GET /auth/** — Endpoint de teste/health check para verificar se a rota de autenticação está funcionando.

- **POST /auth/criar_conta** — Cria uma nova conta de usuário no sistema (recebe nome, email e senha no body como JSON e salva no banco de dados).

- **POST /auth/login** — Autentica um usuário existente, validando email e senha (planejado, ainda não implementado).

## 5. Você está usando algum framework para escrever os endpoints da sua API?

Sim, estou utilizando o FastAPI como framework para a construção dos endpoints.