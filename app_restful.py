from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':0,
        'nome':'Maycon',
        'skills':['Python', 'Flask']
     },

    {
        'id':1,
        'nome':'Santos',
        'skills':['Python', 'Django']
     }
]



class Desenvolvedor(Resource):
    def get(self, dev_id):
        try:
            response = desenvolvedores[dev_id]
        
        except IndexError:
            mensagem = f'ID: {dev_id} de desenvolvedor não encontrado'
            response = {'status':'erro', 'mensagem':mensagem}

        return response
    
    
    def put(self, dev_id):
        dados = json.loads(request.data)
        desenvolvedores[dev_id] = dados
        return dados
    

    def delete(self, dev_id):
        desenvolvedores.pop(dev_id)
        return {'status':'sucesso', 'mensagem':'Registro apagado com sucesso'}

class Listadesenvolvedor(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:dev_id>')
api.add_resource(Listadesenvolvedor,'/dev')

if __name__ == '__main__':
    app.run(debug=True)