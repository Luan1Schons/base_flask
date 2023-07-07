#!/bin/bash

# Carrega as variáveis do arquivo .env
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Verifica se o mkcert está instalado
if ! dpkg -s "mkcert" >/dev/null 2>&1; then
  echo "O mkcert não está instalado. Instalando..."

  # Verifica o sistema operacional e usa o gerenciador de pacotes apropriado
  if uname | grep -iq "darwin"; then
    brew install mkcert
  elif uname | grep -iq "linux"; then
    sudo apt install libnss3-tools
    sudo apt update
    sudo apt install -y mkcert
  else
    echo "Sistema operacional não suportado. Certifique-se de instalar o mkcert manualmente."
    exit 1 
  fi
fi 

# Cria o diretório raiz dos certificados
certs_dir="./server/certs"
mkdir -p "$certs_dir"
cd "$certs_dir"

# Gera os certificados com mkcert
mkcert -install >/dev/null 2>&1
mkcert -cert-file crt.pem -key-file key.pem "$API_URL" >/dev/null 2>&1

echo "Certificados gerados em $certs_dir"
cd ../../
docker-compose -f "docker-compose.yml" up --build
