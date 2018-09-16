import socketserver


class Aluno():
    def __init__(self, notas):
        self.notas = notas

    def e_aprovado(self):
        media = self.notas[0] + self.notas[1]

        if media >= 7.0:
            return "Aprovado"
        elif media >= 3.0:
            return "Deve fazer N3"
        else:
            return "Reprovado"


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        n1, n2, n3 = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        aluno = Aluno([float(n1.strip()), float(n1.strip()), float(n1.strip())])

        # Converte o funcionário em String e envia para o cliente
        data = aluno.e_aprovado()
        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
