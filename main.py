from fastapi import FastAPI
from utils import obtem_biblias, obtem_versiculo, obtem_capitulo, obtem_livro

app = FastAPI()


almeida, almeida_corrigida, nova_versao_internacional = obtem_biblias()


@app.get('/')
async def root():
    return {'message': 'Server OK!'}


@app.get('/{versao}/{abv_livro}/{capitulo}/{versiculo}')
def versiculo(versao: str, abv_livro: str, capitulo: int, versiculo: int):

    if versao == "aa":
        biblia = almeida
    elif versao == "ac":
        biblia = almeida_corrigida
    elif versao == "nvi":
        biblia = nova_versao_internacional

    vers = obtem_versiculo(abv_livro, biblia, capitulo, versiculo)
    return {'versiculo': vers}


@app.get('/{versao}/{abv_livro}/{capitulo}')
def capitulo(versao: str, abv_livro: str, capitulo: int):

    if versao == "aa":
        biblia = almeida
    elif versao == "ac":
        biblia = almeida_corrigida
    elif versao == "nvi":
        biblia = nova_versao_internacional

    vers = obtem_capitulo(abv_livro, biblia, capitulo)
    return {'versiculos': vers}


@app.get('/{versao}/{abv_livro}')
def livro(versao: str, abv_livro: str):

    if versao == "aa":
        biblia = almeida
    elif versao == "ac":
        biblia = almeida_corrigida
    elif versao == "nvi":
        biblia = nova_versao_internacional

    livro = obtem_livro(abv_livro, biblia)
    return {'livro': livro}
