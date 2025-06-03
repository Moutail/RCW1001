# client.py - Version complète pour Azure
import requests
import time

# URL de base de votre application Azure
BASE_URL = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net"

def test_endpoint(endpoint_path, description):
    """Tester un endpoint spécifique"""
    url = f"{BASE_URL}{endpoint_path}"
    
    try:
        print(f"🔗 {description}")
        print(f"   URL: {url}")
        
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            response_data = response.json()
            message = response_data.get('message', str(response_data))
            print(f"   ✅ Succès: {message}")
        else:
            print(f"   ❌ Erreur {response.status_code}: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Erreur de connexion")
    except requests.exceptions.Timeout:
        print("   ❌ Timeout")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    print("-" * 60)
    time.sleep(1)

def main():
    """Tester tous les endpoints"""
    print("🚀 Test de l'application RCW1001 sur Azure")
    print("=" * 60)
    
    # Test des différents endpoints
    test_endpoint("/", "Test de la page d'accueil")
    test_endpoint("/test", "Test de l'endpoint principal")
    test_endpoint("/health", "Test du health check")
    
    # Test spécifique comme votre code original
    print("🎯 Test spécifique de l'endpoint /test (comme votre code original):")
    try:
        url = f"{BASE_URL}/test"
        response = requests.get(url, timeout=30)
        response_data = response.json()
        print(f"Message: {response_data['message']}")
    except Exception as e:
        print(f"Erreur: {e}")
    
    print("\n📋 Informations utiles:")
    print(f"🌐 Application web: {BASE_URL}")
    print(f"📚 Documentation API: {BASE_URL}/docs")
    print(f"❤️  Health check: {BASE_URL}/health")

if __name__ == "__main__":
    main()