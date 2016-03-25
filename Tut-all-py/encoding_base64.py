import base64
encoded = base64.b64encode('Hello How are you!')
print(encoded)
data = base64.b64decode(encoded)

print(data)
