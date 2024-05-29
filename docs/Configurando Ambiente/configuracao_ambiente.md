---
title: 1.1 Usando airflow no Docker
author: Oséias Farias

---

<style>
        .tab {
            display: inline-block;
            margin-left: 40px;
        }
        .tab1 {
            display: inline-block;
            margin-left: 80px;
        }
</style>


<br>

# Como Instalar o Apache Airflow no Docker

Apache Airflow é uma plataforma de código aberto que permite a criação, programação e monitoramento de workflows programáveis. Uma maneira eficiente de utilizar o Airflow é através de contêineres Docker. Este artigo fornecerá um guia passo a passo para instalar e configurar o Apache Airflow usando Docker.

## Índice
- [Como Instalar o Apache Airflow no Docker](#como-instalar-o-apache-airflow-no-docker)
  - [Índice](#índice)
  - [Pré-requisitos](#pré-requisitos)
  - [Passo 1: Instalar Docker](#passo-1-instalar-docker)
    - [Verifique a instalação do Docker](#verifique-a-instalação-do-docker)
    - [Verifique a instalação do Docker Compose](#verifique-a-instalação-do-docker-compose)
  - [Passo 2: Configurar o Docker Compose](#passo-2-configurar-o-docker-compose)
  - [Passo 3: Iniciar o Apache Airflow](#passo-3-iniciar-o-apache-airflow)
    - [Inicialize o banco de dados](#inicialize-o-banco-de-dados)
    - [Iniciar os serviços do Airflow](#iniciar-os-serviços-do-airflow)
  - [Passo 4: Acessar a Interface Web do Airflow](#passo-4-acessar-a-interface-web-do-airflow)
  - [Conclusão](#conclusão)

## Pré-requisitos

- Docker instalado no seu sistema. Se você ainda não tem o Docker instalado, siga as instruções do [guia de instalação do Docker](#guia-de-instalação-do-docker).
- Docker Compose instalado. As instruções para instalação do Docker Compose podem ser encontradas [aqui](https://docs.docker.com/compose/install/).

## Passo 1: Instalar Docker

Antes de começarmos, certifique-se de que o Docker e o Docker Compose estão instalados no seu sistema.

### Verifique a instalação do Docker

```sh
docker --version
```

### Verifique a instalação do Docker Compose

```sh
docker-compose --version
```

Se ambos os comandos retornarem versões instaladas, você está pronto para continuar.

## Passo 2: Configurar o Docker Compose

Crie um diretório para o projeto Airflow e navegue até ele:

```sh
mkdir airflow-docker
cd airflow-docker
```

Dentro desse diretório, crie um arquivo `docker-compose.yml` com o seguinte conteúdo:

```yaml
version: '3'
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    logging:
      options:
        max-size: 10m
        max-file: "3"

  webserver:
    image: apache/airflow:2.3.0
    depends_on:
      - postgres
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__FERNET_KEY: "$(python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())')"
      AIRFLOW__CORE__LOAD_EXAMPLES: "True"
    volumes:
      - ./dags:/opt/airflow/dags
      - ./logs:/opt/airflow/logs
      - ./plugins:/opt/airflow/plugins
    ports:
      - "8080:8080"
    command: webserver
    healthcheck:
      test: ["CMD-SHELL", "[ -f /opt/airflow/airflow-webserver.pid ]"]
      interval: 30s
      timeout: 30s
      retries: 3
    logging:
      options:
        max-size: 10m
        max-file: "3"

  scheduler:
    image: apache/airflow:2.3.0
    depends_on:
      - webserver
      - postgres
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__FERNET_KEY: "$(python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())')"
      AIRFLOW__CORE__LOAD_EXAMPLES: "True"
    volumes:
      - ./dags:/opt/airflow/dags
      - ./logs:/opt/airflow/logs
      - ./plugins:/opt/airflow/plugins
    command: scheduler
    logging:
      options:
        max-size: 10m
        max-file: "3"
```

Este arquivo define os serviços necessários para o Apache Airflow: PostgreSQL como banco de dados, o webserver e o scheduler do Airflow.

## Passo 3: Iniciar o Apache Airflow

### Inicialize o banco de dados

Antes de iniciar os serviços, você precisa inicializar o banco de dados do Airflow:

```sh
docker-compose up airflow-init
```

Este comando criará as tabelas necessárias no banco de dados PostgreSQL. Depois de completar a inicialização, você pode parar o serviço pressionando `Ctrl+C`.

### Iniciar os serviços do Airflow

Inicie todos os serviços definidos no `docker-compose.yml`:

```sh
docker-compose up
```

Isso iniciará os contêineres do PostgreSQL, webserver e scheduler.

## Passo 4: Acessar a Interface Web do Airflow

Uma vez que os serviços estejam em execução, você pode acessar a interface web do Airflow navegando até `http://localhost:8080` em seu navegador.

Você deve ver a interface de login do Airflow. Use as credenciais padrão:

- **Username:** `airflow`
- **Password:** `airflow`

## Conclusão

Seguindo estes passos, você deve conseguir instalar e configurar o Apache Airflow em um ambiente Docker. Esta configuração básica pode ser expandida e customizada conforme necessário, adicionando DAGs, configurando diferentes executores e ajustando parâmetros de configuração de acordo com suas necessidades.

Dockeriza seu ambiente de Airflow não só simplifica a gestão dos serviços, mas também oferece uma forma escalável e portátil de executar workflows complexos.