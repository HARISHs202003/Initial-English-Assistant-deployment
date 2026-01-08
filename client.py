import requests

response = requests.post(
    "http://127.0.0.1:5000/correct",
    json={"text": "i no like english"}
)

print(response.json())
