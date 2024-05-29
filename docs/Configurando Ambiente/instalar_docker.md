---
title: 1.0 Instalação do Docker
author: Oséias Farias

---

# Guia de Instalação do Docker em Linux, Windows e Mac

Docker é uma plataforma de software que permite criar, testar e implantar aplicativos rapidamente. O Docker empacota o software em unidades padronizadas chamadas contêineres que têm tudo o que o software precisa para funcionar, incluindo bibliotecas, ferramentas do sistema, código e runtime. A seguir, apresentamos um guia detalhado para a instalação do Docker nas principais plataformas: Linux, Windows e Mac.

## Índice
1. [Instalação no Linux](#instalação-no-linux)
2. [Instalação no Windows](#instalação-no-windows)
3. [Instalação no Mac](#instalação-no-mac)

## Instalação no Linux

### Passo 1: Atualize seu sistema
Primeiro, certifique-se de que seu sistema está atualizado:
```sh
sudo apt-get update
sudo apt-get upgrade
```

### Passo 2: Instale as dependências
Instale as dependências necessárias:
```sh
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```

### Passo 3: Adicione a chave GPG do Docker
Adicione a chave GPG oficial do Docker:
```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### Passo 4: Adicione o repositório do Docker
Adicione o repositório do Docker às suas fontes APT:
```sh
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Passo 5: Instale o Docker
Atualize as fontes APT e instale o Docker:
```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### Passo 6: Verifique a instalação
Verifique se a instalação foi bem-sucedida:
```sh
sudo docker --version
```

## Instalação no Windows

### Passo 1: Baixe o Docker Desktop
Baixe o Docker Desktop para Windows no [site oficial do Docker](https://www.docker.com/products/docker-desktop).

### Passo 2: Execute o instalador
Execute o instalador baixado e siga as instruções na tela.

### Passo 3: Inicie o Docker Desktop
Após a instalação, inicie o Docker Desktop a partir do menu Iniciar.

### Passo 4: Verifique a instalação
Abra um terminal do PowerShell e execute:
```sh
docker --version
```

## Instalação no Mac

### Passo 1: Baixe o Docker Desktop
Baixe o Docker Desktop para Mac no [site oficial do Docker](https://www.docker.com/products/docker-desktop).

### Passo 2: Instale o Docker Desktop
Abra o arquivo `.dmg` baixado e arraste o ícone do Docker para a pasta Aplicativos.

### Passo 3: Inicie o Docker Desktop
Abra o Docker Desktop a partir da pasta Aplicativos e siga as instruções para concluir a instalação.

### Passo 4: Verifique a instalação
Abra o Terminal e execute:
```sh
docker --version
```

## Conclusão
Seguindo estes passos, você deve conseguir instalar o Docker em máquinas com Linux, Windows e Mac. O Docker é uma ferramenta poderosa para o desenvolvimento e implantação de aplicativos, e a sua instalação é o primeiro passo para aproveitar todos os benefícios que ele oferece.