from flask import Blueprint, request, jsonify
from model.enviarEmail2 import enviarEmail
from model.enviarEmail3 import enviarEmail3
from model.mandarSenha import codificarSenhaEmail

from dotenv import load_dotenv

load_dotenv()

envioEmail = Blueprint('envioEmail', __name__)

@envioEmail.route("/test", methods=['GET'])
def test():
    return jsonify({"message":"Envio Email Blueprint funcionando!"}), 200

@envioEmail.route("/enviarEmail", methods=['GET'])
def mandarEmail():
     
     dados = request.get_json()
     
     destinatario_json = dados.get('destinatario')
     assunto_json =  dados.get('assunto')
     mensagem_json =  dados.get('mensagem')
     
     try:
          response = enviarEmail(destinatario_json, assunto_json, mensagem_json)
     
     except Exception as e:
          return jsonify({'erro': str(e)}), 500
     
     return jsonify(response), 200

@envioEmail.route("/enviarEmail3", methods=['GET'])
def mandarEmail3():
     
     dados = request.get_json()
     
     destinatario_json = dados.get('destinatario')
     assunto_json =  dados.get('assunto')
     mensagem_json =  dados.get('mensagem')
     
     try:
          response = enviarEmail3(destinatario_json, assunto_json, mensagem_json)
     
     except Exception as e:
          return jsonify({'erro': str(e)}), 500
     
     return jsonify(response), 200

@envioEmail.route("/pega/senha", methods=['GET'])
def mandarSenha():
     try: 
         return codificarSenhaEmail(),200
     
     except Exception as e:
          return jsonify({'erro': str(e)}), 500

     
     
     
     
     