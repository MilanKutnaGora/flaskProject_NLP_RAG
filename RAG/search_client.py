import requests

url = 'http://127.0.0.1:5001/search'
query_input = "хочу узнать о продукте"

response = requests.post(url, json={'query': query_input})

if response.status_code == 200:
    print("Наиболее релевантные отзывы:", response.json())
else:
    print("Ошибка:", response.status_code)