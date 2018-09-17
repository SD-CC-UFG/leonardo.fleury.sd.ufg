from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


def peso_ideal(altura, sexo):
    if sexo == "masculino":
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

if __name__ == '__main__':
    HOST, PORT = "localhost", 9991

    # Tenta criar um serivdor TCP
    with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(peso_ideal)

        server.serve_forever()

