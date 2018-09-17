from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

def atualiza_salario(nome, cargo, salario):
    """
    atualiza_salario(nome, cargo, salario) => \"Nome: {}\nSalário: {}\"

    Atualiza o salário do funcionário de acordo com o cargo.
    """    
    if cargo == "operador":
        salario *= 1.2
    elif cargo == "programador":
        salario *= 1.18

    return "Nome: {}\nSalário: {}".format(nome, salario)


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

if __name__ == '__main__':
    HOST, PORT = "localhost", 9991

    # Tenta criar um serivdor TCP
    with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(atualiza_salario)

        server.serve_forever()
