import socket

HOST, PORT = "localhost", 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    valor = input("Valor: ")
    naipe = input("Naipe: ")

    data = "{}, {}".format(valor, naipe)

    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

    print("\n{}".format(received))