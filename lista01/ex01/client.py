import socket

HOST, PORT = "localhost", 9991

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")

    data = "{}, {}, {}".format(nome, cargo, salario)

    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

    print("\n{}".format(received))
