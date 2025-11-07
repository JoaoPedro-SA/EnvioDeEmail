import smtplib
from email.message import EmailMessage
import mimetypes
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import json
from mandarSenha import f

remetente = "trajetoexpress04@gmail.com"

def enviarEmail4(destinatario, assunto, mensagem, arquivo ,senha):
     
     try:
          senha_decodificada = f.decrypt(senha).decode()
          
          
          msg = EmailMessage()
          msg['Subject'] = assunto
          msg['From'] = remetente
          msg['To'] = destinatario
          msg.set_content(mensagem)


          with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
               email.login(remetente, senha_decodificada)
               email.send_message(msg)
          
          # with smtplib.SMTP("localhost", 1025) as email: 
          #      email.login(remetente, senha)
          #      email.send_message(msg)
               
          return "Email enviado com sucesso!"

     except Exception as e:
          return f"Erro ao enviar email: {str(e)}"
     
