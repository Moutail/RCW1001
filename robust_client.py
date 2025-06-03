# robust_client.py
import requests
import json

# Votre URL Azure mise à jour
url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net/test"

def safe_get_message():
    """Version sécurisée de votre client original"""
    
    try:
        print(f"🔗 Connexion à: {url}")
        
        # Faire la requête avec timeout
        response = requests.get(url, timeout=30)
        
        print(f"📊 Status Code: {response.status_code}")
        
        # Vérifier le status code
        if response.status_code != 200:
            print(f"❌ Erreur HTTP {response.status_code}")
            print(f"Réponse: {response.text[:500]}")
            return None
        
        # Vérifier le Content-Type
        content_type = response.headers.get('content-type', '')
        print(f"📄 Content-Type: {content_type}")
        
        # Essayer de parser en JSON
        try:
            response_json = response.json()
            
            # Vérifier si 'message' existe
            if 'message' in response_json:
                message = response_json['message']
                print(f"✅ Message reçu: {message}")
                return message
            else:
                print(f"⚠️  Pas de clé 'message' dans la réponse")
                print(f"Réponse complète: {response_json}")
                return str(response_json)
                
        except json.JSONDecodeError as e:
            print(f"❌ Erreur JSON: {e}")
            print(f"Contenu brut: {response.text[:500]}")
            
            # Vérifier si c'est du HTML (page d'erreur)
            if response.text.strip().startswith('<!DOCTYPE html>') or response.text.strip().startswith('<html'):
                print("🌐 La réponse semble être une page HTML (probablement une erreur)")
                # Extraire le titre si possible
                if '<title>' in response.text:
                    start = response.text.find('<title>') + 7
                    end = response.text.find('</title>')
                    title = response.text[start:end] if end > start else "Titre non trouvé"
                    print(f"📄 Titre de la page: {title}")
            
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ Erreur de connexion - Vérifiez votre internet ou l'URL")
        return None
        
    except requests.exceptions.Timeout:
        print("❌ Timeout - L'application met trop de temps à répondre")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de requête: {e}")
        return None
        
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return None

def test_alternative_endpoints():
    """Tester d'autres endpoints pour diagnostiquer"""
    
    base_url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net"
    endpoints = ["/", "/health", "/docs"]
    
    print(f"\n🔍 Test d'autres endpoints pour diagnostiquer:")
    
    for endpoint in endpoints:
        try:
            test_url = f"{base_url}{endpoint}"
            print(f"\n📡 Test: {endpoint}")
            
            response = requests.get(test_url, timeout=10)
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                # Afficher un aperçu du contenu
                content_preview = response.text[:200].replace('\n', ' ')
                print(f"Aperçu: {content_preview}...")
                
        except Exception as e:
            print(f"Erreur: {e}")

if __name__ == "__main__":
    print("🚀 Client robuste pour RCW1001")
    print("=" * 50)
    
    # Test principal
    message = safe_get_message()
    
    if message:
        print(f"\n🎉 Succès! Message final: {message}")
    else:
        print(f"\n🔧 Échec du test principal. Diagnostic supplémentaire:")
        test_alternative_endpoints()
        
        print(f"\n💡 Actions recommandées:")
        print("1. Vérifiez les logs de déploiement Azure")
        print("2. Vérifiez que votre main.py est correct")
        print("3. Vérifiez que requirements.txt contient fastapi et uvicorn")
        print("4. Redéployez l'application si nécessaire")