import multiprocessing
import xmlrpc.server
from fastapi import FastAPI
import uvicorn


def xmlrpc_server():
    def add(x, y):
        return x + y

    server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 8020))
    server.register_function(add, "add")
    server.serve_forever()


def fastapi_server():
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "Worldmp"}

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=xmlrpc_server)
    p2 = multiprocessing.Process(target=fastapi_server)
    p1.start()
    p2.start()
