from habilidades import AlterarHabilidade, Habilidades
from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

devs = [    
    {
        'id': 0,
        'nome':'Rafael',
        'habilidades':['Python', 'Flask']
    },
    {
        'id': 1,
        'nome':'Galleani',
        'habilidades':['Python', 'Django']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            resposta = devs[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe!'
            resposta = {'status':'ERRO', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            resposta = {'status':'ERRO', 'mensagem':mensagem}
        return resposta
        
    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status':'SUCESSO', 'mensagem':'Registro excluído'}

class ListaDevs(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return devs[posicao]
    
    def get(self):
        return devs

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDevs, '/dev')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(AlterarHabilidade, '/habilidade/<int:id>')

if __name__ == '__main__':
    app.run()