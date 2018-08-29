import socket
import threading
import logging
from multiprocessing.pool import ThreadPool

HOST = "127.0.0.1"
PORT = 8080
ADDR = (HOST, PORT)
BUFFERSIZE = 4096
CONNECTIONLIST = []


def accept_client():
    """Aceita conexões de novos usuários"""
    pool = ThreadPool(processes=32)

    while True:
        cli_sock, cli_add = sock.accept()
        # Recebendo o nome de usuário do novo cliente
        user = str(cli_sock.recv(BUFFERSIZE), "utf-8")
        # Adicionando o socket do novo cliente a uma lista de clientes
        CONNECTIONLIST.append(cli_sock)

        logging.info("{} conectado".format(user))
        logging.debug("\t{}\n\t{}".format(cli_sock, cli_add))

        pool.apply_async(client, (user, cli_sock))


def client(username, cli_sock):
    """Recebe as mensagens do usuário e a envia para todos os outros usuários do chat"""
    logging.debug("Thread iniciada.")

    # Criando uma variável local para a thread
    data = threading.local()
    data.username = username

    msg = bytes("AVISO: {} se conectou.".format(data.username), "utf-8")
    send_broadcast(cli_sock, msg)

    while True:
        try:
            # Recebe a mensagem enviada pelo usuário e a converte em str
            data.msg = str(cli_sock.recv(BUFFERSIZE), "utf-8")

            logging.info("Mensagem recebida")
            logging.debug("\t{}: {}".format(data.username, data.msg))

            if not data.msg:
                """Se a mensagem for vazia, significa que o usuário se desconectou"""
                # Remove o usuário da lista de conexões
                CONNECTIONLIST.remove(cli_sock)
                # Avisa a todos que o usuário de desconectou
                msg = bytes("AVISO: {} se conectou.".format(data.username), "utf-8")
                send_broadcast(cli_sock, msg)
                logging.info("{} se desconectou.".format(data.username))
                # E sai do laço
                break

            # Formata a mensagem e envia para todos os outros usuários
            msg = bytes("{} > {}".format(data.username, data.msg), "utf-8")
            send_broadcast(cli_sock, msg)
        except Exception as x:
            logging.error("Erro ao receber mensagem")
            logging.debug(x)
            break


def send_broadcast(cli_sock, data):
    """Envia a mensagem em data para todos os usuários, exceto para o cli_sock"""
    for conn in CONNECTIONLIST:
        if conn != cli_sock:
            conn.send(data)


if __name__ == "__main__":
    """
    Um chat simples escrito em Python usando sockets e threads.
    """

    logging.basicConfig(level=logging.INFO)

    # socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    sock.bind(ADDR)

    # listen
    sock.listen(1)
    print('Servidor iniciado na porta {}'.format(str(PORT)))

    accept_client()
