import xmlrpc.client

print("bonjour 8020")
proxy = xmlrpc.client.ServerProxy("http://server:8020/")
result = proxy.add(7, 3)
print(f"7 + 3 = {result}")
