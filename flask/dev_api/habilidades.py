from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        mensagem = f'A habilidade {lista_habilidades[-1]} foi adicionada a lista.'
        return mensagem

class AlterarHabilidade(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        mensagem = f'A habilidade {lista_habilidades[id]} foi aterada pela habilidade '
        lista_habilidades[id] = dados
        mensagem += lista_habilidades[id]
        return mensagem

    def delete(self, id):
        mensagem = f'A habilidade {lista_habilidades[id]} '
        lista_habilidades.pop(id)
        mensagem += 'foi removida dalista de habilidades.'
        return mensagem
    