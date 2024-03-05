from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Transacao(BaseModel):
    valor: float
    tipo: str | None = None
    desc: str | None = None

class Cliente(BaseModel):
    id: int
    nome: str | None = None
    valor_na_conta: float
    transacoes: List[Transacao] = []

clientes_db = [
    {
        "id": 1,
        "nome": "Silvio Santos",
        "valor_na_conta": 10000,
        "transacoes": [
            {"valor": 1500, "tipo": "d", "descricao": "Uma transacao"}
        ]
    },
    {
        "id": 2,
        "nome": "Fausto Silva",
        "valor_na_conta": 10,
        "transacoes": [
            {"valor": 1500, "tipo": "c", "descricao": "Uma transacao"},
            {"valor": 32, "tipo": "d", "descricao": "Uma transacao"}
        ]
    },
    {
        "id": 3,
        "nome": "Gugu Liberato",
        "valor_na_conta": 0,
        "transacoes": []
    }
]

@app.get("/clientes/{cliente_id}/transacoes")
async def obter_transacoes_do_cliente(cliente_id: int = 0):
    for cliente in clientes_db:
        if cliente["id"] == cliente_id:
            return {"transacoes": cliente["transacoes"]}

@app.get("/clientes/{cliente_id}")
async def obter_cliente_por_id(cliente_id: int = 0):
    for cliente in clientes_db:
        if cliente["id"] == cliente_id:
            informacoes_do_cliente = {k: v for k, v in cliente.items() if k != "transacoes"}
            transacoes_do_cliente = obter_transacoes_do_cliente(cliente_id)
        raise HTTPException(status_code=404, detail="Cliente não encontrado")