# Usa uma imagem base leve com Python 3
FROM python:3.10

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do diretório atual para o diretório de trabalho do contêiner (/app)
COPY ./api .
COPY .env .
# Expõe a porta 5000 para que o Flask possa receber solicitações
EXPOSE 5000

# Define o script como executável
RUN chmod +x ./entrypoint.sh

# Define o comando de entrada como o script entrypoint.sh quando o contêiner estiver em execução
CMD ["./entrypoint.sh"]
