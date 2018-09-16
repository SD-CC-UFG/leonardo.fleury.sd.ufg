import socket
from flask import Flask, request
app = Flask(__name__)


@app.route('/ex01', methods=['GET'])
def ex01():
    nome = request.args.get('nome')
    cargo = request.args.get('cargo')
    salario = request.args.get('salario')

    data = "{}, {}, {}\n".format(nome, cargo, salario)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9991))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex02', methods=['GET'])
def ex02():
    nome = request.args.get('nome')
    sexo = request.args.get('sexo')
    idade = request.args.get('idade')

    data = "{}, {}, {}\n".format(nome, sexo, idade)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9992))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex03', methods=['GET'])
def ex03():
    data = "{}, {}, {}\n".format()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9993))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex04', methods=['GET'])
def ex04():
    sexo = request.args.get('sexo')
    altura = request.args.get('altura')

    data = "{}, {}, {}\n".format(sexo, altura)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9994))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex05/<float:idade:', methods=['GET'])
def ex05(idade):
    data = "{}\n".format(idade)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9995))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex06', methods=['GET'])
def ex06():
    nome = request.args.get('nome')
    nivel = request.args.get('nivel')
    salario = request.args.get('salario')
    dependentes = request.args.get('dependentes')

    data = "{}, {}, {}, {}\n".format(nome, nivel, salario, dependentes)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9996))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex07', methods=['GET'])
def ex07():
    idade = request.args.get('idade')
    tempo_servico = request.args.get('tempo_servico')

    data = "{}, {}\n".format(idade, tempo_servico)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9997))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex08/<float:saldo>', methods=['GET'])
def ex08(saldo):
    data = "{}\n".format(saldo)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9998))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


@app.route('/ex09/<int:valor>/<int:naipe>', methods=['GET'])
def ex09(valor, naipe):
    data = "{}, {}\n".format(valor, naipe)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectando ao servidor
        sock.connect(("localhost", 9999))
        # Envia os dados formatados
        sock.sendall(bytes(data, "utf-8"))
        # Recebe uma resposta do servidor
        return str(sock.recv(1024), "utf-8")


if __name__ == '__main__':
    app.run(debug=True)
