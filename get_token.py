token = "Bearer "

with open("token.txt", "r") as file:
    token += file.read()
print("Passei aqui: get")
