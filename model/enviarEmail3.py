import os
import smtplib
from email.message import EmailMessage
import mimetypes
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

remetente = "trajetoexpress04@gmail.com"

def enviarEmail3(destinatario, assunto, mensagem):

     # Use variáveis de ambiente para dados sensíveis
     senha = os.getenv("EMAIL_PASSWORD2")  
     
     try:
          msg = EmailMessage()
          msg['Subject'] = assunto
          msg['From'] = remetente
          msg['To'] = destinatario
          msg.set_content(mensagem)


          with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
               email.login(remetente, senha)
               email.send_message(msg)
          
          # with smtplib.SMTP("localhost", 1025) as email: 
          #      email.login(remetente, senha)
          #      email.send_message(msg)
               
          return "Email enviado com sucesso!"

     except Exception as e:
          return f"Erro ao enviar email: {str(e)}"