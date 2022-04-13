# Mercado Livre Crawler docker version

Versão docker do crawler do Mercado Livre para ser executada localmente.

## Instalação

1) Clone esta branch do repositório

```
$ git clone -b docker-version https://github.com/lucasboscatti/mercado-livre-crawler
```


2) Crie um arquivo .env com as configurações do seu banco de dados de acordo com o documento env-sample.txt na pasta contrib. Abaixo um exemplo de configuração do DATABASE_URL

```
DATABASE_URL='postgresql+psycopg2://<DB_USERNAME>:<DB_PASSWORD>@db:5432'
```

3) Execute os comandos docker-compose no terminal

```
$ docker-compose build
```
```
$ docker-compose up
```

Seu projeto já esta em execução!

Caso queira parar o projeto, execute o comando:

```
$ docker-compose down
```

Se estiver com conflitos em relação a porta do seu banco de dados, execute o comando:

```
$ sudo service postgresql stop
```