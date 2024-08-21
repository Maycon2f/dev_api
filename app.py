from flask import Flask, request, jsonify
import json

app = Flask(__name__)



tarefas = [
    {
        'id':0,
        'responsavel':'maycon',
        'tarefa': ['Desenvolver método GET',
                   'Desenvolver método DELETE'],
        'status': 'concluido',
    },
    {
        'id':1,
        'responsavel':'santos',
        'tarefa': ['Desenvolver método POST',
                   'Desenvolver metodo GET'],
        'status': 'pendente'
    }

]

@app.route('/task/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def consultas(id):
    if request.method == 'GET':
        return jsonify(tarefas[id])
    
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = dados['status']
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        tarefas[id]['tarefa'].clear()
        return 'status:sucesso  mensagem:excluido com sucesso'


@app.route('/task/<int:id>', methods=['POST'])
def adicionar(id):
    dados = json.loads(request.data)
    tarefas[id]['tarefa'].append(dados)
    return jsonify(tarefas[id])


@app.route('/task', methods=['GET'])
def exibir_task():
    return jsonify(tarefas)



if __name__ == '__main__':
    app.run()


