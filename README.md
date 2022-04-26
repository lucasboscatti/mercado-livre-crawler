# mercado-livre-crawler

Este é um projeto de nível iniciante para a área de engenharia de dados. O objetivo é extrair dados das ofertas de produtos do site [Mercado Livre](https://www.mercadolivre.com.br) e armazená-los em um banco de dados [PostgreSQL](https://www.postgresql.org/) com um mesmo schema. Na branch [docker-version](https://github.com/lucasboscatti/mercado-livre-crawler/tree/docker_version) está implementado o código para ser executado localmente em um container [Docker](https://www.docker.com/) com orquestramento do crawler e do banco de dados feito pelo [Docker Compose](https://docs.docker.com/compose/). Na branch principal está o código para ser executado e hospedado na plataforma [Heroku](https://www.heroku.com/). O banco de dados também está hospedado nesta plataforma com um limite de 10.000 registros.

## Artigo
Escrevi um tutorial no [Medium](https://medium.com/@lucasboscatti/agendando-a-execu%C3%A7%C3%A3o-de-um-crawler-no-heroku-de-forma-gratuita-337561c87d92) com um passo a passo para realizar o deploy de um Crawler com Scrapy no Heroku.

## Análise dos dados
[Neste repositório](https://github.com/lucasboscatti/mercado-livre-data-analysis) fiz uma limpeza e análise dos dados coletados por este crawler.
