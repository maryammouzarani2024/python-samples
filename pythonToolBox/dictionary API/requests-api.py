import requests

def api(word):
    resp = requests.get(f" http://127.0.0.1:8000/api/?w={word}")
    content = resp.text
    print(content)

word=input("type the word: ")
api(word)