import requests

r = requests.get("https://google.co.kr")
print(r.text)
