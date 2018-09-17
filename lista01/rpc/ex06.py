import socketserver


class Pessoa():
    def __init__(self, nome, nivel, salario, nro_dependentes):
        self.nome = nome
        self.nivel = nivel
        self.salario = salario
        self.dependentes = nro_dependentes

    def salario_liquido(self):
        if self.nivel == "A":
            if self.dependentes:
                return self.salario * 0.97
            else:
                return self.salario * 0.92
        elif self.nivel == "B":
            if self.dependentes:
                return self.salario * 0.95
            else:
                return self.salario * 0.90
        elif self.nivel == "C":
            if self.dependentes:
                return self.salario * 0.98
            else:
                return self.salario * 0.85
        elif self.nivel == "D":
            if self.dependentes:
                return self.salario * 0.90
            else:
                return self.salario * 0.83

    def __str__(self):
        return "{}, {}, {}".format(self.nome, self.nivel, self.salario_liquido())


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        nome, nivel, salario, nro_dependentes = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        pessoa = Pessoa(nome.strip(), nivel.strip(), float(salario), int(nro_dependentes))

        self.request.sendall(pessoa.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
