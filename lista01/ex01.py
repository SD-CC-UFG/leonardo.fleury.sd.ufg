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
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        nome, cargo, salario = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        func = Funcionario(nome.strip(), cargo.strip(), float(salario.strip()))
        func.atualiza_salario()

        # Converte o funcionário em String e envia para o cliente
        data = str(func)
        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9991

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
