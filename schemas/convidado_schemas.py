from pydantic import BaseModel
from typing import Optional, List
from model.models import Session
from model.models import Convidado


class ConvidadoSchema(BaseModel):
    """ Define como um novo convidado a ser inserido deve ser representado
    """
    nome: str = "Carlos Roberto Pereira"
    numero_telefone: str = "000000000"
    numero_convidado: int = 1


class ConvidadoBuscaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do convidado.
    """
    id: int = 1

class ConvidadoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do convidado.
    """
    nome: str = "Teste"


class ListaConvidadosSchema(BaseModel):
    """ Define como uma lista de convidados será retornada.
    """
    convidados: List[ConvidadoSchema]


class ConvidadoViewSchema(BaseModel):
    """ Define como o convidado será retornado: convidado + mesa.
    """
    id: int
    numero_convidado: Optional[int]
    nome: str
    numero_telefone: int


class ConvidadoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str


def apresenta_convidados(convidados: List[ConvidadoSchema]):
    """ Retorna uma representação dos convidados seguindo o schema definido em ConvidadoViewSchema. """
    result = []
    for convidado in convidados:
        result.append({
            "id": convidado.id,
            "numero_convidado": convidado.numero_convidado,
            "nome": convidado.nome,
            "numero_telefone": convidado.numero_telefone
        })

    return {"convidados": result}
