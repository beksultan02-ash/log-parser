user_to_id = {
    "Bek": 101,
    "Alik": 101,
    "Dana": 103
}

id_to_user = {}

for names, id in user_to_id.items():
    if id not in id_to_user:
        id_to_user[id] = []

    id_to_user[id].append(names)

print(id_to_user)