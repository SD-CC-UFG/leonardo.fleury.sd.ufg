import socketserver


class Funcionario():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def atualiza_salario(self):
        if self.cargo == "operador":
            self.salario *= 1.2
        elif self.cargo == "programador":
            self.salario *= 1.18

    def __str__(self):
        return "Nome: {}\nSalário: {}".format(self.nome, self.salario)


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        nome, cargo, salario = self.request.recv(1024).decode('utf-8').split(',')
        func = Funcionario(nome.strip(), cargo.strip(), float(salario.strip()))
        func.atualiza_salario()
        data = str(func)
        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9991

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()
