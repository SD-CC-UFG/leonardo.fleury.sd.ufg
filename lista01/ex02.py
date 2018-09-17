import socketserver


class Pessoa():
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def e_maior(self):
        if self.sexo == "masculino":
            if self.idade >= 18:
                return True
            else:
                return False
        elif self.sexo == "feminino":
            if self.idade >= 21:
                return True
            else:
                return False

    def __str__(self):
        return "Nome: {}\nIdade: {}\nSexo: {}".format(self.nome, self.idade, self.sexo)


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        nome, sexo, idade = self.request.recv(1024).decode('utf-8').split(',')

        # Cria um Funcionário e atualiza seu salário de acordo com o cargo
        pess = Pessoa(nome.strip(), sexo.strip(), int(idade.strip()))

        # Converte o funcionário em String e envia para o cliente
        data = "Maior de idade" if pess.e_maior else "Menor de idade"
        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
