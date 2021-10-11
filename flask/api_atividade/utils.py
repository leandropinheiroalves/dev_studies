from sqlalchemy.orm import column_property
from models import Pessoas, Atividade, Usuarios

# Pessoas
def insere_pessoas(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Pedro').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Pedro'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.delete()
    print('deletado com sucesso')


# Atividade
def insere_atividade(tar, pes):
    pessoa = Pessoas.query.filter_by(nome=pes).first()
    atividade = Atividade(nome=tar, pessoas_id=pessoa.id)
    print(atividade, pessoa)
    atividade.save()

def consulta_atividade():
    atividades = Atividade.query.all()
    print(atividades)
    
def altera_atividade(id, alt):
    atividade = Atividade.query.filter_by(id=id).first()
    atividade.nome = alt
    atividade.save()

def exclui_atividade(id):
    atividade = Atividade.query.filter_by(id=id).first()
    atividade.delete()
    print('Deletado com sucesso')

# inserir 5 nomes
def ins():
    nomes = ['Leandro', 'Tiago', 'Pedro', 'Rafael', 'Galleani']
    idades = [30, 25, 40, 29, 24]
    for i, nome in enumerate(nomes):
        insere_pessoas(nome, idades[i])

# inserir 5 trabalhos aleatorios
def tra():
    from random import randint
    ins()
    tarefas = [
                'Colher café',
                'Moer cana',
                'Manda email',
                'Soltar pipa',
                'Pisar em uvas'
              ]
    nomes = {1:'Leandro', 2:'Tiago', 3:'Pedro', 4:'Rafael', 5:'Galleani'}
    for tarefa in tarefas:
        insere_atividade(tarefa, nomes[randint(1, 5)])
    insere_usuario('leandro', '1234')
    insere_usuario('rafael', '1234')
    insere_usuario('pedro', '1234')
    insere_usuario('tiago', '1234')

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def alterar_permisao_usuario(usuario):
    usuario = Usuarios.query.filter_by(login=usuario).first()
    print(usuario, usuario.ativo)
    if usuario.ativo == 1:
        usuario.ativo = 0
    elif usuario.ativo == 0:
        usuario.ativo = 1
    usuario.save()
    print(usuario, usuario.ativo)

if __name__ == '__main__':
    alterar_permisao_usuario('leandro')
