import json

with open("src/utils/ip_addres.json", 'r') as file:
    json_data = json.load(file)

IP = f'http://{json_data["ip"]}'
