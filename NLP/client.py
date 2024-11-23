import requests

url = 'http://127.0.0.1:5000/process'
text_input = "Привет, как дела? Я хочу узнать о вашем продукте."

response = requests.post(url, json={'text': text_input})

if response.status_code == 200:
    print("Очищенные токены:", response.json())
else:
    print("Ошибка:", response.status_code)