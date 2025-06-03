# client.py - Version pour Azure
import requests

# URL de votre application Azure
url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net/test"

try:
    print(f"🚀 Connexion à: {url}")
    response = requests.get(url, timeout=30)
    
    if response.status_code == 200:
        response_data = response.json()
        print(f"✅ Succès: {response_data['message']}")
    else:
        print(f"❌ Erreur {response.status_code}: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ Erreur de connexion - Vérifiez votre connexion internet")
except requests.exceptions.Timeout:
    print("❌ Timeout - L'application prend trop de temps à répondre")
except requests.exceptions.RequestException as e:
    print(f"❌ Erreur de requête: {e}")
except KeyError:
    print("❌ Réponse inattendue du serveur")
    print(f"Réponse reçue: {response.text}")
except Exception as e:
    print(f"❌ Erreur inattendue: {e}")