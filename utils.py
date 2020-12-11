import json
import codecs


def obtem_biblias():
    with codecs.open('./json/aa.json', 'r', 'utf-8-sig') as aa:
        almeida = json.load(aa)

    with codecs.open('./json/acf.json', 'r', 'utf-8-sig') as acf:
        almeida_corrigida = json.load(acf)

    with codecs.open('./json/nvi.json', 'r', 'utf-8-sig') as nvi:
        nova_versao_internacional = json.load(nvi)

    return almeida, almeida_corrigida, nova_versao_internacional


def obtem_versiculo(abreviacao, biblia, capitulo, versiculo):
    capitulo -= 1
    versiculo -= 1
    for livro in biblia:
        if livro["abbrev"] == abreviacao:
            return livro["chapters"][capitulo][versiculo]


def obtem_capitulo(abreviacao, biblia, capitulo):
    capitulo -= 1
    for livro in biblia:
        if livro["abbrev"] == abreviacao:
            return livro["chapters"][capitulo]


def obtem_livro(abreviacao, biblia):
    for livro in biblia:
        if livro["abbrev"] == abreviacao:
            return livro
