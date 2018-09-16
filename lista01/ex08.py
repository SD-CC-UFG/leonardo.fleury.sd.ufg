import socketserver


def credito(saldo):
    if saldo <= 200:
        return 0
    elif saldo <= 400:
        return saldo * 0.2
    elif saldo <= 600:
        return saldo * 0.3
    else:
        return saldo * 0.4


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        saldo = self.request.recv(1024).decode('utf-8').split(',')

        data = "{}".format(credito(saldo))

        self.request.sendall(data.encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Roda eternamente
        server.serve_forever()
