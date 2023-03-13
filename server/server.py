import xmlrpc.server


def add(x, y):
    return x + y


server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 8020))
print("Listening (0.0.0.0) on port 8020...")
server.register_function(add, "add")
server.serve_forever()
