import requests
# url = "http://localhost:8000/test"
url = 'https://app-rcw-cmgwamd3dbc2h7aa.canadaeast-01.azurewebsites.net'
 
response = requests.get(url)
 
try:
    response = response.json()
    print(response['message'])
   
 
except Exception as e:
    print("Error: Response is not in JSON format",e)