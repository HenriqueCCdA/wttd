# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver ?

1. Clone o repositório.
2. Cria um virtualenv
3. Ative o virtualenv
4. Instale as dependêcias.
5. Configure a instância com o .env
6. Execute os testes

```consolse
git clone git@github.com:HenriqueCCdA/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.p test
```

## Com fazer o deploy?

1. Crie uma instÂcia no heroku.
2. Envia as configurações para o heroku.
3. Defina um SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envia o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```