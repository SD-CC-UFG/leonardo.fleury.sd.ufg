import xmlrpc.client


def main():
    s = xmlrpc.client.ServerProxy('http://localhost:9991')

    nome = input("Nome: ")
    cargo = input("Cargo (programador, operador): ") 
    salario = float(input("Salário: "))

    print("\n\n{}".format(s.atualiza_salario(nome, cargo, salario)))


if __name__ == '__main__':
    main()
