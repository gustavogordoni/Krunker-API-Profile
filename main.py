from krunker_api import krunker_api
import json

print("Bem-vindo ao KrunkerAPI!")
print("Por favor, digite o nome do usuário que deseja consultar:")
username = input()

data = krunker_api(username, debug=True)
json_string = json.dumps(data)
print(json_string)

filename = f"data/{username}_profile.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
