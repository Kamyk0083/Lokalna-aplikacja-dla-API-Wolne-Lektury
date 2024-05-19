import requests

def add_book(data):
    response = requests.post('http://localhost:5000/books', json=data)
    return response.json()

def add_categories(data, category_type):
    response = requests.post(f'http://localhost:5000/categories/{category_type}', json=data)
    return response.json()
