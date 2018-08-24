import socketserver


class Carta():

    VALORES = ['Ás',
               'Dois',
               'Três',
               'Quatro',
               'Cinco',
               'Seis',
               'Sete',
               'Oito',
               'Nove',
               'Dez',
               'Valete',
               'Rainha',
               'Rei']
    NAIPES = ['Ouros',
              'Paus',
              'Copas',
              'Espadas']

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return "{} de {}".format(self.VALORES[self.valor-1], self.NAIPES[self.naipe-1])


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recebe uma string de um cliente e a divide nas variaveis apropriadas
        valor, naipe = self.request.recv(1024).decode('utf-8').split(',')
        carta = Carta(int(valor.strip()), int(naipe.strip()))

        # Converte a carta em String e envia para o cliente
        self.request.sendall(str(carta).encode("utf-8"))


if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()