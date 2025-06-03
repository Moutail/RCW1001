# diagnostic_client.py
import requests

# Votre vraie URL Azure
AZURE_URL = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net"

def diagnose_azure_app():
    """Diagnostiquer l'application Azure"""
    
    endpoints = ["/", "/test", "/health", "/docs"]
    
    print("🔍 Diagnostic de l'application Azure")
    print(f"Base URL: {AZURE_URL}")
    print("=" * 60)
    
    for endpoint in endpoints:
        try:
            url = f"{AZURE_URL}{endpoint}"
            print(f"\n📡 Testing: {endpoint}")
            print(f"URL complète: {url}")
            
            response = requests.get(url, timeout=30)
            
            print(f"Status Code: {response.status_code}")
            print(f"Content-Type: {response.headers.get('content-type', 'Non spécifié')}")
            print(f"Content-Length: {len(response.content)} bytes")
            
            # Afficher le début de la réponse
            content_preview = response.text[:500]
            print(f"Content Preview:\n{content_preview}")
            
            # Essayer de parser en JSON seulement si c'est du JSON
            content_type = response.headers.get('content-type', '')
            if 'application/json' in content_type:
                try:
                    json_data = response.json()
                    print(f"✅ JSON valide: {json_data}")
                except:
                    print("❌ JSON invalide malgré le Content-Type")
            elif response.status_code == 200:
                print("ℹ️  Réponse non-JSON (probablement HTML)")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de connexion: {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            
        print("-" * 60)

def test_specific_endpoint():
    """Tester spécifiquement l'endpoint /test"""
    
    url = f"{AZURE_URL}/test"
    print(f"\n🎯 Test spécifique de /test")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Raw Content: {response.text[:1000]}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                message = data.get('message', 'Pas de message')
                print(f"✅ Message extrait: {message}")
                return message
            except:
                print("❌ Impossible de parser en JSON")
                print("🔍 Contenu brut:", response.text[:200])
        else:
            print(f"❌ Erreur HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    return None

if __name__ == "__main__":
    print("🚀 Diagnostic complet de l'application Azure")
    
    # Diagnostic général
    diagnose_azure_app()
    
    # Test spécifique
    test_specific_endpoint()
    
    print("\n💡 Solutions possibles:")
    print("1. L'application n'est pas encore complètement déployée")
    print("2. Il y a une erreur dans votre code main.py")
    print("3. Les dépendances ne sont pas correctement installées")
    print("4. Problème de configuration Azure")
    
    print(f"\n🔗 Liens utiles:")
    print(f"App: {AZURE_URL}")
    print(f"Health: {AZURE_URL}/health")
    print(f"Docs: {AZURE_URL}/docs")