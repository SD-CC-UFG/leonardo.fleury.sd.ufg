import socketserver


class Pessoa():
    def __init__(self, altura, sexo):
        self.altura = altura
        self.sexo = sexo

    def peso_ideal(self):
        if self.sexo == "masculino":
            return (72.7 * self.altura) - 58
        else:
            return (62.1 * self.altura) - 44.7


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        altura, sexo = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        pessoa = Pessoa(float(altura), sexo.strip())

        # Converte o funcionário em String e envia para o cliente
        data = pessoa.peso_ideal()
        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
