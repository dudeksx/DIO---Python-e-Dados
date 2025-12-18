# Esse projeto faz parte do desafio do Bootcamp da Dio - Python e Dados
import pandas as pd
import requests
import json

# Declaração de Funções


def get_user_data(user_ids):
    response = requests.get(f'{url}/users/{user_ids}')
    return response.json() if response.status_code == 200 else None


def update_user(user):
    response = requests.put(f'{url}/users/{user["id"]}', json=user)
    return True if response.status_code == 200 else False
# -------------------------------------------


# Declaração de Variáveis
df = pd.read_csv("dados.csv")

user_ids = df["UserId"].tolist()

url = "http://127.0.0.1:8000"
# -------------------------------------------


users = [
    user
    for user_id in user_ids
    if (user := get_user_data(user_id)) is not None
]

# print(json.dumps(user, indent=4))

for user in users:
    success = update_user(user)

    print(f"User {user['name']} update status: {success}")
