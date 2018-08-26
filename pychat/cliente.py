import socket
import logging
import sys
from threading import Thread

HOST = "127.0.0.1"
PORT = 8080
ADDR = (HOST, PORT)
BUFFERSIZE = 4096


def print_chat(text):
    """Imprime a mensagem de maneira bonita"""
    sys.stdout.write("\u001b[1L\u001b[1A\u001b[1B\u001b[1000D")
    sys.stdout.write(text)
    sys.stdout.write("\u001b[1B\u001b[1000D\u001b[7C")
    sys.stdout.flush()


def receive():
    """Recebe e imprime as mensagens dos outros usuário"""
    while True:
        try:
            data = sock.recv(BUFFERSIZE)
            print_chat(str(data, "utf-8"))
        except Exception as e:
            logging.info("Erro de conexão")
            logging.error(e)
            break


def send():
    """Envia a mensagem para o servidor"""
    while True:
        msg = input("Você > ")
        data = "{}".format(msg)
        sock.send(bytes(data, "utf-8"))


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    user_name = input("Username: ")

    # Cria uma conexão com o servidor e se apresenta
    sock.connect(ADDR)
    sock.send(bytes(user_name, "utf-8"))

    logging.info("Conectado ao servidor.")

    # Cria e inicia as threads para receber e enviar mensagens
    # dessa maneira, o usuário não fica bloqueado enquanto envia ou recebe mensagens
    thread_send = Thread(target=send)
    thread_recv = Thread(target=receive)

    thread_send.start()
    thread_recv.start()
