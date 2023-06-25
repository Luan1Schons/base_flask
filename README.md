# Micro Framework API Rest com JWT Token e frontend em Vue.js

Surgiu a necessidade de uma aplicação em flask para autenticar usuários via jwt, portanto criei este micro-framework com migrations, models e controllers
para facilitar o meu uso diário com desenvolvimento.

## Contém um Front-End utilizando Vue.js 3 para realizar a integração entre back-end e front-end
- Interceptors configurados para tratar erros, sempre enviar o bearer token, mostrar notificações de erros usando o Toastify.
- Camadas de proteções no back-end para revogar tokens, expiração, validar token em todas rotas privadas.
- Migrações do banco de dados, seguindo normalização de dados 1 e 2
- Configuração inicial dos arquivos de configuração (config.py)
- Rotas padrão configurada atendendo normas Rest Api

As seguintes ferramentas foram usadas na
## Pré-requisitos
- [Node]
- [Python]
- [Windows, Mac, Linux]

## Instalação

1. Clone o repositório:

```bash
   git clone https://github.com/Luan1Schons/base_flask.git
   ```

2. Instale as dependencias
```bash
    pip install -r requirements.txt
    npm install
    npm run build

    # Inicie o ambiente de desenvolvimento com
    npm run dev
   ```

3. Faça bom uso...
- Dentro da pasta App contém exemplos de utilização do framework.
- Dentro da pasta frontend contém um frontend de exemplo que autentica usuários utilizando Jwt Token

## Como contribuir?
Faça um fork do projeto e crie uma branch

## Licença
[MIT](https://choosealicense.com/licenses/mit/)