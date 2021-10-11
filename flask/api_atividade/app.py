from flask import Flask, request
from flask_restful import Resource, Api
from models import Atividade, Pessoas, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#    'rafael':'123',
#    'galleani':'321'
#}
#
#@auth.verify_password
#def verificacao(login, senha):
#    if not (login, senha):
#        return False
#    return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    usuario = Usuarios.query.filter_by(login=login).first()
    if not (login, senha) or usuario.ativo != 1:
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa não encontrada'
            }
        return response
    
    @auth.login_required
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        response = {
            'status':'sucesso',
            'mensagem':f'Pessoas {pessoa.nome} excluída com sucesso'
        }
        pessoa.delete()
        return response

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividade.query.all()
        response = [{
            'id':i.id,
            'nome':i.nome, 
            'pessoa':i.pessoa.nome, 
            'status':i.status} for i in atividades]
        return response
    
    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response

class AtividadePessoa(Resource):
    def get(self, nome):
        atividades = Atividade.query.all()
        response = []
        for i in atividades:
            if nome == i.pessoa.nome:
                response.append({'id atividade':i.id, 'nome':i.nome, 'status':i.status})
        if response == []:
            response = {
                'status':'erro',
                'mensagem':'Pessoa não encontrada'
            }
        return response

class StatusAtividade(Resource):
    def get(self, id):
        try:
            atividade = Atividade.query.filter_by(id=id).first()
            response = {
                'id':atividade.id,
                'nome':atividade.nome,
                'status':atividade.status,
                'pessoa':atividade.pessoa.nome
            }
        except Exception:
            response = {
                'status':'erro',
                'mensagem':'Atividade não encontrada'
            }
        return response

    @auth.login_required
    def put(self, id):
        try:
            atividade = Atividade.query.filter_by(id=id).first()
            mensagem = f'O status da atividade "{atividade.nome}" foi alterado para '
            if atividade.status == 'pendente':
                atividade.status = 'concluido'
            elif atividade.status == 'concluido':
                atividade.status = 'pendente'
            mensagem += atividade.status
            response = {
                'status da operacao':'concluido',
                'mensagem':mensagem
            }
            atividade.save()
        except Exception:
            response = {
                'status':'erro',
                'mensagem':'Atividade não encontrada'
            }
        return response

    
api.add_resource(Pessoa, '/pessoas/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoas/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(AtividadePessoa, '/atividades/<string:nome>')
api.add_resource(StatusAtividade, '/atividades/<int:id>')

if __name__ == '__main__':
    app.run()