import base64

msg = "Murilo"

cripto = base64.b64encode(msg)
print(cripto)

print(base64.b64decode(cripto))