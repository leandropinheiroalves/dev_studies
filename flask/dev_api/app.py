from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

# Devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            dev = devs[id]
            print(dev)
            return jsonify(dev)
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe!'
            return jsonify({'status':'ERRO', 'mensagem':mensagem})
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            return jsonify({'status':'ERRO', 'mensagem':mensagem})
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'SUCESSO', 'mensagem':'Registro excluído'})


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify(devs[posicao])
    elif request.method == 'GET':
        return jsonify(devs)
        
if __name__ == '__main__':
    app.run()