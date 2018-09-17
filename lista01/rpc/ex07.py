import socketserver


class Trabalhador():
    def __init__(self, idade, tempo_servico):
        self.idade = idade
        self.tempo = tempo_servico

    def pode_aposentar(self):
        if self.idade > 65:
            return True

        if self.tempo > 30:
            return True

        if self.idade > 60 and self.tempo > 25:
            return True

        return False


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        idade, tempo_servico = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        trab = Trabalhador(float(idade), float(tempo_servico))

        data = "Pode aposentar" if trab.pode_aposentar else "Não pode aposentar"

        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
