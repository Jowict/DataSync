from pydantic import BaseModel 

class PessoaModelo(BaseModel):
    id: int = None
    nome: str