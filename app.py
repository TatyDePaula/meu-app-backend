from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from model import Session

from sqlalchemy.exc import IntegrityError

from model.models import Convidado
from logger import logger
from schemas.convidado_schemas import ConvidadoBuscaSchema, ConvidadoSchema, ListaConvidadosSchema, ConvidadoViewSchema, \
    ConvidadoDelSchema, apresenta_convidados, ConvidadoBuscaIdSchema
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
convidado_tag = Tag(name="Convidado", description="Adição, visualização e remoção de convidados e seus relacionamentos")
co_convidado_tag = Tag(name="CoConvidado", description="Adição e visualização de coconvidados")
mesa_tag = Tag(name="Mesa", description="Operações relacionadas a mesas")
comentario_tag = Tag(name="Comentário", description="Adição e visualização de comentários")


# Rota raiz, redireciona para /openapi
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')


# Adição de novo convidado
@app.post('/convidado', tags=[convidado_tag], responses={"200": ConvidadoViewSchema})
def add_convidado(form: ConvidadoSchema):
    convidado = Convidado(
        nome=form.nome,
        numero_convidado=form.numero_convidado,
        numero_telefone=form.numero_telefone
    )

    logger.debug(f"Adicionando convidado de nome: '{convidado.nome}'")
    print(convidado)
    try:
        session = Session()
        session.add(convidado)
        session.commit()
        logger.debug(f"Adicionado convidado de nome: '{convidado.nome}'")

        return apresenta_convidados([convidado]), 200
    except IntegrityError as e:
        error_msg = "Convidado com mesmo número já salvo na base :/"
        logger.warning(f"Erro ao adicionar convidado '{convidado.nome}', {error_msg}")
        return {"message": error_msg, "nome": convidado.nome}, 409

    except Exception as e:
        print(e)
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar convidado '{convidado.nome}', {error_msg}")
        return {"message": error_msg, "nome": convidado.nome}, 400


# Visualização de todos os convidados
@app.get('/convidados', tags=[convidado_tag], responses={"200": ListaConvidadosSchema})
def get_convidados():
    session = Session()
    convidados = session.query(Convidado).all()

    if not convidados:
        return {"convidados": []}, 200
    else:
        return apresenta_convidados(convidados), 200


# Visualização de um convidado específico
@app.get('/convidado', tags=[convidado_tag], responses={"200": ConvidadoViewSchema})
def get_convidado(query: ConvidadoBuscaSchema):
    convidado_nome = query.nome
    session = Session()
    convidado = session.query(Convidado).filter(Convidado.nome == convidado_nome).first()

    if not convidado:
        error_msg = "Convidado não encontrado na base :/"
        logger.warning(f"Erro ao buscar convidado '{convidado_nome}', {error_msg}")
        return {"message": error_msg, "nome": convidado_nome}, 404
    else:
        return apresenta_convidados([convidado]), 200


# Remoção de convidado
@app.delete('/convidado', tags=[convidado_tag], responses={"200": ConvidadoDelSchema})
def del_convidado(query: ConvidadoBuscaIdSchema):
    try:
        logger.debug(f"Deletando dados sobre convidado ID #{query.id}")
        session = Session()
        convidado = session.query(Convidado).filter(Convidado.id == query.id).first()
        session.delete(convidado)
        session.commit()
        logger.debug(f"Deletado convidado ID #{query.id}")
        return {"message": "Convidado removido", "nome": query.id}, 200
    except Exception as e:
        return {"message": str(e), "nome": query.id}, 404


if __name__ == '__main__':
    app.run(debug=True)

