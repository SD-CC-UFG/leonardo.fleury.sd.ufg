# PyChat

Programa de chat escrito em Python 3.

Este chat funciona em terminal e permite que seus usuários se comuniquem dentro de uma mesma rede.

## Dependencias

O PyChat depende apenas do Python 3.

### Linux
Muito provavelmente sua distribuição já possui o Python 3 instalado, mas caso não possua, instale com o seguinte comando:

``# apt install python3``

### MacOS

Para instalar o Python 3, siga as instruções disponiveis em [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/starting/install3/osx/).

### Windows

Baixe o instalador [aqui](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe) ou siga as instruções disponíveis em  ou siga as instruções em [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/starting/install3/win/)


## Executando

Para executar este programa, primeiro se deve subir um servidor:

``$ python3 server.py``

Então os usuários podem se conectar, executando:

``$ python3 client.py``

## Sobre os requisitos para o curso

- [x] Multhread
- [x] Dispatcher e threads pré alocadas