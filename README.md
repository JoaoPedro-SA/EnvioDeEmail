# api_email

API simples para envio de e-mail usando Flask e smtplib.

Este micro-serviço fornece endpoints para enviar e-mails via SMTP (Gmail) e para codificar/decodificar senhas com criptografia Fernet.

## Recursos

- Flask como framework web
- Endpoints em `controle/emailControle.py`:
  - `GET /test` — retorna um JSON simples confirmando que o Blueprint está funcionando
  - `GET /enviarEmail` — envia e-mail usando a função `enviarEmail` (variável de ambiente `EMAIL_PASSWORD`)
  - `GET /enviarEmail3` — envia e-mail usando a função `enviarEmail3` (variável de ambiente `EMAIL_PASSWORD2`)
  - `GET /pega/senha` — retorna a senha codificada (função `codificarSenhaEmail`)
- Dockerfile e Procfile para deploy (Heroku/Gunicorn)

## Estrutura de pastas (resumo)

- `app.py` / `main.py` — arquivo principal que registra o blueprint e inicia o servidor
- `controle/emailControle.py` — define os endpoints do serviço
- `model/` — contém as implementações de envio de e-mail e utilitários (enviarEmail.py, enviarEmail2.py, enviarEmail3.py, enviarEmail4.py, mandarSenha.py)
- `requirements.txt` — dependências Python
- `dockerfile` — docker image baseada em Python 3.13
- `Procfile` — configuração para execução com Gunicorn

## Pré-requisitos

- Python 3.11+ (a imagem Docker usa Python 3.13)
- Conta(s) de e-mail do Gmail com senha de aplicativo ou autenticação adequada para SMTP

## Variáveis de ambiente

Crie um arquivo `.env` (nunca o comite) com as chaves necessárias. Um exemplo no diretório `model/.env` já contém placeholders:

```
EMAIL_PASSWORD="sua_senha_gmail_para_remetente1"
EMAIL_PASSWORD2="sua_senha_gmail_para_remetente2"
```

OBS: Use senhas de aplicativo do Gmail (App Password) quando necessário, e mantenha as credenciais em um local seguro.

## Instalação e execução local

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```powershell
python -m venv venv; .\venv\Scripts\Activate
```

2. Instale as dependências:

```powershell
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo `.env` (ou via variáveis de ambiente do sistema)

4. Execute a aplicação localmente:

```powershell
python app.py
```

5. Teste o endpoint principal:

```powershell
curl -X GET "http://127.0.0.1:5000/test"
```

Para testar o envio de e-mail, o código atual usa requisições GET esperando JSON no corpo (o que é incomum). Exemplo de chamada para envio (pode variar conforme cliente HTTP):

```powershell
curl -X GET "http://127.0.0.1:5000/enviarEmail" -H "Content-Type: application/json" -d "{\"destinatario\": \"destinatario@exemplo.com\",\"assunto\": \"Teste\",\"mensagem\": \"Olá\"}"
```

## Docker

Para rodar com Docker:

```powershell
docker build -t api_email:latest .
docker run -p 5000:5000 --env-file model/.env api_email:latest
```

## Observações e boas práticas

- Não use JSON em requisições GET: o ideal é usar POST para enviar payloads (melhorar os endpoints do blueprint é recomendado).
- Não comite credenciais (arquivo `.env`) no controle de versão.
- Se for para produção, considere trocar para um serviço SMTP com maior segurança ou usar OAuth2.
- Arquivos `enviarEmail`, `enviarEmail2`, `enviarEmail3` e `enviarEmail4` demonstram diferentes abordagens (anexos, múltiplos remetentes, senha codificada via `mandarSenha.py`).

## Licença

Este repositório não possui uma licença especificada (adicione se necessário).

---

Feito com ❤ — scripts simples para demonstrar envio de e-mail com Flask e smtplib.
