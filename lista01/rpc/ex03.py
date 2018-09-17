from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


def aprovado(notas):
    media = (notas[0] + notas[1])/2

    if media >= 7.0:
        return "Aprovado"
    elif media >= 3.0:
        return "Deve fazer N3"
    else:
        return "Reprovado"


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

if __name__ == '__main__':
    HOST, PORT = "localhost", 9991

    # Tenta criar um serivdor TCP
    with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(aprovado)

        server.serve_forever()
