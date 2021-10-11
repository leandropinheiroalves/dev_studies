from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {
        'id':0,
        'responsavel':'Rafael',
        'tarefa':'Desenvolver método Get',
        'status':'concluido'
    },
    {
        'id':1,
        'responsavel':'Galleani',
        'tarefa':'Desenvolver método POST',
        'status':'pendente' 
    }
]


# Listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_todas_tarefas():
    return jsonify(tarefas)
    

# Listar tarefa por ID, alterar status da tarefa e deletar a tarefa
@app.route('/tarefa/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def listar_tarefa(id):
    if request.method == 'GET':
        try:
            return jsonify(tarefas[id])
        except Exception:
            mensagem = f'O ID {id} não corresponde a nenhuma tarefa.'
            return jsonify({'status':'erro GET', 'mensagem':mensagem})

    elif request.method == 'PUT':
        try:
            if tarefas[id]['status'] == 'pendente':
                status = 'concluido'
                tarefas[id]['status'] = status
            else:
                status = 'pendente'
                tarefas[id]['status'] = status
            mensagem = f'O status da tarefa foi alterado para {status}.'
            return jsonify({'mensagem':mensagem})
        except Exception:
            mensagem = f'O ID {id} não corresponde a nenhuma tarefa.'
            return jsonify({'status':'erro PUT', 'mensagem':mensagem})

    elif request.method == 'DELETE':
        try:
            tarefas.pop(id)
            return jsonify({'mensagem':f'A tarefa {id} foi removida com sucesso!'})
        except Exception:
            mensagem = f'O ID {id} não corresponde a nenhuma tarefa.'
            return jsonify({'status':'erro DELETE', 'mensagem':mensagem})

if __name__ == '__main__':
    app.run()
