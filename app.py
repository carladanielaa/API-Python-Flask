#aqui to importando
from flask import Flask, make_response, jsonify, request # make_response é para ele retorna uma responsta da API e o jsonify é para configura o json
from bd import Carros   #aqui tô importando o banco de dados (Carros)de mentira 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # o Flask por padrãpo ordena em ordem alfabetica e com essa configuração fica na orde que eu coloco

#função e routa e o decoretion q é o @APP
@app.route('/carros', methods=['GET']) 
def get_carros():
    return make_response (jsonify(
        
        mensagem= 'Lista de Carros.',
        dados=Carros
        
    ))

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response (jsonify(
        mensagem = 'Carro criado com sucesso',
        carro=carro
        
    ))



app.run()