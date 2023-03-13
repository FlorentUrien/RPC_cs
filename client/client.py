import xmlrpc.client

print("toto")
print("bonjour 8020")
proxy = xmlrpc.client.ServerProxy("http://serveur:8020/")
result = proxy.add(7, 3)
print(f"7 + 3 = {result}")
result = proxy.add(9, 4)
print(f"9 + 4 = {result}")
