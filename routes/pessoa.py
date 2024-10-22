from flask import Blueprint, Response
from flask import jsonify
from flask_restful import reqparse
from database.models.pessoa import Pessoa
import json

pessoa_resource = Blueprint('pessoa', __name__)

@pessoa_resource.route("/")
def lista_pessoas():
    
    pessoas = Pessoa.select()
    
    pessoas_list = []
    for pessoa in pessoas:
        pessoas_list.append({
            "id": pessoa.id,
            "nome": pessoa.nome,
            "sobrenome": pessoa.sobrenome,
            "email": pessoa.email,
            "idade": pessoa.idade,
            "data_nasc": pessoa.data_nasc,
        })
        
    json_response = json.dumps({"Pessoas": pessoas_list}, sort_keys=False)
    return Response(json_response, mimetype='application/json')

@pessoa_resource.route("/", methods=['POST'])
def cadastrar_pessoas():
    
    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help='Nome obrigatório')
    parser.add_argument('sobrenome', type=str, required=True, help='Sobrenome obrigatório')
    parser.add_argument('email', type=str, required=True, help='Email obrigatório')
    parser.add_argument('idade', type=int, required=True, help='Idade obrigatório')  
    parser.add_argument('data_nasc', type=str, required=True, help='Data nascimento obrigatório')    
    args = parser.parse_args()
    
    nova_pessoa = Pessoa.create(nome=args['nome'],
                                sobrenome=args['sobrenome'],
                                email=args['email'],
                                idade=args['idade'],
                                data_nasc=args['data_nasc'])
    
    return {"msg": "Success"}

@pessoa_resource.route("/", methods=['PUT'])
def atualizar_pessoas():
    
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True, help='Id obrigatório')
    parser.add_argument('nome', type=str, required=False)
    parser.add_argument('sobrenome', type=str, required=False)
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('idade', type=int, required=False)  
    parser.add_argument('data_nasc', type=str, required=False)    
    args = parser.parse_args()
    
    pessoa = Pessoa.get_by_id(args['id'])
    
    if not pessoa:
            return {'message': 'Pessoa não encontrada'}, 404
        
    if args['nome']:
        pessoa.nome = args['nome']
    if args['sobrenome']:
        pessoa.sobrenome = args['sobrenome']
    if args['email']:
        pessoa.email = args['email']
    if args['idade']:
        pessoa.idade = args['idade']
    if args['data_nasc']:
        pessoa.data_nasc = args['data_nasc']
        
    pessoa.save()
    
    return {"msg": "Success"}

@pessoa_resource.route("/", methods=['DELETE'])
def deletar_pessoas():
    
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True, help='Id obrigatório')
    args = parser.parse_args()
    
    pessoa = Pessoa.get_by_id(args['id'])
    pessoa.delete_instance()
    return {'msg': 'Success'}