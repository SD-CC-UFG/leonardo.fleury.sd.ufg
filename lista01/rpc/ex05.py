import socketserver


class Nadador():
    def __init__(self, idade):
        self.idade = idade

    def classificacao(self):
        if self.idade < 5:
            return "Não pode participar"
        elif self.idade < 8:
            return "infantil A"
        elif self.idade < 11:
            return "infantil B"
        elif self.idade < 14:
            return "juvenil A"
        elif self.idade < 18:
            return "juvenil B"
        else:
            return "adulto"


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        idade = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        data = Nadador(float(idade)).classificacao()

        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
