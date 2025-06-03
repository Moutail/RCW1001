import requests
url = "http://localhost:8000/test"
response = requests.get(url)
response = response.json()
print(response['message'])