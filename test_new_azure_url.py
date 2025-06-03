# test_new_azure_url.py
import requests

# Nouvelle URL détectée dans les logs
NEW_URL = "https://app-rcw-cmgwamd3dbc2h7aa.canadaeast-01.azurewebsites.net"

def test_new_app():
    """Tester la nouvelle application Azure"""
    
    print("🚀 Test de la NOUVELLE URL Azure")
    print(f"URL: {NEW_URL}")
    print("=" * 60)
    
    endpoints = ["/", "/test"]
    
    for endpoint in endpoints:
        try:
            url = f"{NEW_URL}{endpoint}"
            print(f"\n📡 Test: {endpoint}")
            print(f"URL complète: {url}")
            
            response = requests.get(url, timeout=30)
            
            print(f"Status: {response.status_code}")
            print(f"Content-Type: {response.headers.get('content-type', 'Non spécifié')}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"✅ SUCCESS! JSON: {data}")
                    message = data.get('message', 'Pas de message')
                    print(f"📝 Message: {message}")
                except:
                    print(f"⚠️ Pas du JSON: {response.text[:200]}...")
            elif response.status_code == 503:
                print("❌ Service Unavailable (503)")
                print(f"Contenu: {response.text[:200]}...")
            else:
                print(f"⚠️ Status {response.status_code}")
                print(f"Contenu: {response.text[:200]}...")
                
        except requests.exceptions.Timeout:
            print("⏳ Timeout - App possiblement en train de démarrer")
        except Exception as e:
            print(f"❌ Erreur: {e}")
        
        print("-" * 40)

def compare_urls():
    """Comparer les deux URLs"""
    
    old_url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net"
    new_url = "https://app-rcw-cmgwamd3dbc2h7aa.canadaeast-01.azurewebsites.net"
    
    print(f"\n🔍 COMPARAISON DES URLs:")
    print(f"Ancienne: {old_url}")
    print(f"Nouvelle: {new_url}")
    print()
    print("Différences:")
    print("- Nom: rcw1001 → app-rcw")
    print("- Région: canadacentral → canadaeast")
    print("- ID: dhdjeqb7cyfvhkh8 → cmgwamd3dbc2h7aa")

if __name__ == "__main__":
    compare_urls()
    test_new_app()
    
    print(f"\n💡 ACTIONS:")
    print("1. Utilisez maintenant cette nouvelle URL pour vos tests")
    print("2. Mettez à jour votre client.py avec la nouvelle URL")
    print("3. Vérifiez si cette nouvelle app fonctionne mieux")