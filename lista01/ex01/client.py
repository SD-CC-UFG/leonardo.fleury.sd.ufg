import socket

HOST, PORT = "localhost", 9991

# Tenta criar um socket, caso consiga, prossegue com execução
# caso falhe, termina o programa
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Conectando ao servidor
    sock.connect((HOST, PORT))

    # Lendo dados passados pelo usuário
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")

    # Formatando os dados para que o servidor possa entender (valores separados por virgula)
    data = "{}, {}, {}".format(nome, cargo, salario)

    # Envia os dados formatados
    sock.sendall(bytes(data + "\n", "utf-8"))
    # Recebe uma resposta do servidor
    received = str(sock.recv(1024), "utf-8")

    print("\n{}".format(received))
