from pydantic import BaseModel 

class ProdutoModelo(BaseModel):
    id_produto: int = None
    nome_produto: str