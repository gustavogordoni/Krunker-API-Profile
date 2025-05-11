from krunker_api import krunker_api

print("Bem-vindo ao KrunkerAPI!")
print("Por favor, digite o nome do usuário que deseja consultar:")
username = input()

data = krunker_api(username, debug=True)

print(data)
