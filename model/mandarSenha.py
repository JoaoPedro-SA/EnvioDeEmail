from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import json

# cola aqui a chave gerada anteriormente:
key = b'vG1Ku_8qA1bO-eXUJq2R7u5dglZdrZlK0RHVobkBGls='

f = Fernet(key)

senha = "12345"
senha_codificada = f.encrypt(senha.encode())
print(senha_codificada.decode())

# e para decodificar depois:
senha_decodificada = f.decrypt(senha_codificada).decode()
print(senha_decodificada)


def codificarSenhaEmail():
    # Carrega as variáveis de ambiente
    load_dotenv()

    senha = os.getenv("EMAIL_PASSWORD2")

    # Codifica a senha (gera bytes)
    senha_codificada = f.encrypt(senha.encode())

    # Converte para string para poder usar em JSON
    senha_codificada_str = senha_codificada.decode()

    # Só para teste: decodifica de volta
    senha_decodificada = f.decrypt(senha_codificada).decode()

    print("Senha codificada:", senha_codificada_str)
    print("Senha decodificada:", senha_decodificada)

    # Retorna um dicionário pronto para converter em JSON
    return {"senha": senha_codificada_str}



