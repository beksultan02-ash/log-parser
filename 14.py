user_to_id = {
    "Bek": 101,
    "Alik": 102,
    "Dana": 103
}

id_to_user = {}

for names, id in user_to_id.items():
    id_to_user[id] = names

print(id_to_user)