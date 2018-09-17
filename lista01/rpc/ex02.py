from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


def e_maior(nome, sexo, idade):
    if sexo == "masculino":
        if idade >= 18:
            return True
        else:
            return False
    elif sexo == "feminino":
        if idade >= 21:
            return True
        else:
            return False


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


if __name__ == '__main__':
    HOST, PORT = "localhost", 9992

    # Tenta criar um serivdor TCP
    with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(e_maior)

        server.serve_forever()
