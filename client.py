import requests
url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net/test"
response = requests.get(url)
response = response.json()
print(response['message'])