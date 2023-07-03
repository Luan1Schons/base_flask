# Micro Framework API Rest com JWT Token e frontend em Vue.js

Surgiu a necessidade de uma aplicação em flask para autenticar usuários via jwt, portanto criei este micro-framework com migrations, models e controllers
para facilitar o meu uso diário com desenvolvimento.

## Contém um Front-End utilizando Vue.js 3 para realizar a integração entre back-end e front-end
- Interceptors configurados para tratar erros, sempre enviar o bearer token, mostrar notificações de erros usando o Toastify.
- Camadas de proteções no back-end para revogar tokens, expiração, validar token em todas rotas privadas.
- Tokens JWT Armazenados em Cookies com a flag httpOnly para previnir XSS
- Migrações do banco de dados, seguindo normalização de dados 1 e 2
- Configuração inicial dos arquivos de configuração (config.py)
- Rotas padrão configurada atendendo normas Rest Api
- Servidor Python WSGI HTTP Gunicorn e nginx com proxy pass e otimizações de segurança e conteúdo.
- Banco de dados MySQL
- Geração de certificados ssl em desenvolvimento local

# Poder, Segurança, Escalabilidade e Perfomance


   . Nginx para recursos estáticos e caching: O Nginx é conhecido por sua eficiência ao servir arquivos estáticos e pode melhorar o desempenho do seu aplicativo ao lidar com esses recursos. Além disso, o Nginx também oferece recursos de caching, que podem ajudar a reduzir a carga no seu aplicativo e melhorar o tempo de resposta para solicitações repetidas.

   . Gunicorn como servidor WSGI: O Gunicorn é um servidor WSGI (Web Server Gateway Interface) que lida com as solicitações HTTP recebidas pelo seu aplicativo Python. Ele fornece um ambiente robusto para a execução do seu aplicativo Python, gerenciando threads e processos para atender às solicitações dos clientes.

   O Nginx lida com os recursos estáticos e caching, e o Gunicorn executa o código Python


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

5. Build dos containers docker e suba o servidor
```bash
  renomeie o arquivo docker-compose-base.yml para docker-compose.yml e o arquivo configs_base.py para configs.py
  docker compose up --build -d

  # Acesse http://localhost:5000
  ```

4. Faça bom uso...
- Dentro da pasta App contém exemplos de utilização do framework.
- Dentro da pasta frontend contém um frontend de exemplo que autentica usuários utilizando Jwt Token

## Como contribuir?
Faça um fork do projeto e crie uma branch

## Licença
[MIT](https://choosealicense.com/licenses/mit/)