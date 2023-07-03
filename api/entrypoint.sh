#!/bin/sh

# Navega para a pasta raiz do projeto
cd /app

# Define a variável de ambiente FLASK_APP para o módulo que contém a aplicação
export FLASK_APP=app

# Servidor de desenvolvimento
flask run --host=0.0.0.0
flask db migrate
flask db upgrade
# Servidor de Produção
#exec gunicorn --log-level debug -w 1 -b 0.0.0.0:5000 "app:app"
