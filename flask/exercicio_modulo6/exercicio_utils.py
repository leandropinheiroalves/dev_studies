from sqlalchemy.orm import column_property

from exercicio_models import Habilidades, Programador


# Funções relacionadas ao Programador
def add_dev(n:str, i:int, e:str):
    dev = Programador(nome=n, idade=i, email=e)
    dev.save()
    print(dev)

def consulta_dev(d=999):
    if  d == 999:
        dev = Programador.query.all()
        print(dev)
    else:
        dev = Programador.query.filter_by(id=d).first()
        print(f'ID: {dev.id}')
        print(f'Nome: {dev.nome}')
        print(f'Idade: {dev.idade}')
        print(f'Email: {dev.email}')

def altera_dev():
    consulta_dev()
    i = int(input('Informe o ID do programador que deseja alterar: '))
    dev = Programador.query.filter_by(id=i).first()
    escolha = str(input('O que deseja alterar? [nome, idade, email] '))
    if escolha == 'nome':
        n = str(input('Digite o novo nome: '))
        resultado = f'O nome {dev.nome} foi alterado para '
        dev.nome = n
        dev.save()
        resultado += f'{dev.nome} com sucesso.'
        print(resultado)
    
    elif escolha == 'idade':
        n = int(input('Digite a nova idade: '))
        resultado = f'A idade {dev.idade} foi alterada para '
        dev.idade = n
        dev.save()
        resultado += f'{dev.idade} com sucesso.'
        print(resultado)
    
    elif escolha == 'email':
        n = str(input('Digite o novo email: '))
        resultado = f'O email {dev.email} foi alterado para '
        dev.email = n
        dev.save()
        resultado += f'{dev.email} com sucesso.'
        print(resultado)
    
    else:
        print('Escolha inválida.')
    
def exclui_dev():
    consulta_dev()
    i = int(input('Digite o ID do programador que deseja excluir: '))
    dev = Programador.query.filter_by(id=i).first()
    resultado = f'O programador {dev.nome} foi excluído com sucesso'
    dev.delete()
    print(resultado)

# Funções relacionadas as Habilidades
def add_hab(n):
    hab = Habilidades(nome=n)
    hab.save()
    print(hab)

def consulta_hab(d=999):
    if  d == 999:
        hab = Habilidades.query.all()
        print(hab)
    else:
        hab = Habilidades.query.filter_by(id=d).first()
        print(f'ID: {hab.id}')
        print(f'Nome: {hab.nome}')


def altera_hab():
    consulta_hab()
    i = int(input('Informe o ID da habilidade que deseja alterar: '))
    hab = Habilidades.query.filter_by(id=i).first()
    h = str(input('Digite a nova habilidade: '))
    resultado = f'A habilidade {hab.nome} foi alterada para '
    hab.nome = h
    hab.save()
    resultado += f'{hab.nome} com sucesso.'
    print(resultado)

def exclui_hb():
    consulta_hab()
    i = int(input('Informe o ID da habilidade que deseja excluir: '))
    hab = Habilidades.query.filter_by(id=i).first()
    print(f'A habilidade {hab.nome} foi deletada com sucesso')
    hab.delete()

if __name__ == '__main__':
    
    
