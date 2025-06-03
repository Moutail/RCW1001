# test_azure_config.py
import requests
import time

def test_azure_after_config():
    """Tester Azure après avoir configuré la commande de démarrage"""
    
    base_url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net"
    
    print("🔄 Test après configuration Azure...")
    print("⚠️  IMPORTANT: Assurez-vous d'avoir configuré:")
    print("   - Commande de démarrage: python -m uvicorn main:app --host 0.0.0.0 --port 8000")
    print("   - Variable PORT = 8000")
    print("   - Variable WEBSITE_RUN_FROM_PACKAGE = 1")
    print()
    
    endpoints = ["/", "/test"]
    
    for i in range(3):  # Essayer 3 fois avec pause
        print(f"🔄 Tentative {i+1}/3...")
        
        for endpoint in endpoints:
            try:
                url = f"{base_url}{endpoint}"
                print(f"📡 Test: {endpoint}")
                
                response = requests.get(url, timeout=30)
                
                print(f"   Status: {response.status_code}")
                
                if response.status_code == 200:
                    content_type = response.headers.get('content-type', '')
                    
                    if 'application/json' in content_type:
                        try:
                            data = response.json()
                            print(f"   ✅ JSON: {data}")
                            
                            if endpoint == "/test":
                                message = data.get('message')
                                print(f"   🎉 SUCCESS! Message: {message}")
                                return True
                                
                        except:
                            print(f"   ❌ JSON malformé")
                    else:
                        print(f"   ⚠️  Content-Type: {content_type}")
                        if response.text.strip().startswith('<'):
                            print(f"   ❌ Encore du HTML (erreur)")
                        
                elif response.status_code == 503:
                    print(f"   ❌ Service non disponible (503)")
                else:
                    print(f"   ⚠️  Status inattendu: {response.status_code}")
                    
            except Exception as e:
                print(f"   ❌ Erreur: {e}")
        
        if i < 2:  # Pause sauf à la dernière tentative
            print("   ⏳ Attente 30 secondes avant retry...")
            time.sleep(30)
        
        print("-" * 50)
    
    return False

def quick_manual_test():
    """Test manuel rapide de l'endpoint /test"""
    
    url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net/test"
    
    try:
        print(f"\n🎯 Test manuel de /test")
        print(f"URL: {url}")
        
        response = requests.get(url, timeout=30)
        
        print(f"Status: {response.status_code}")
        print(f"Content-Type: {response.headers.get('content-type', 'Non spécifié')}")
        print(f"Contenu: {response.text[:200]}...")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"✅ JSON parsé: {data}")
                print(f"✅ Message: {data.get('message', 'Pas de message')}")
                return True
            except:
                print("❌ Pas du JSON valide")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    return False

if __name__ == "__main__":
    print("🚀 Test de configuration Azure")
    print("=" * 60)
    
    # Test complet
    success = test_azure_after_config()
    
    if not success:
        print("\n🔍 Test manuel supplémentaire:")
        quick_manual_test()
        
        print("\n💡 Si ça ne marche toujours pas:")
        print("1. Vérifiez que la commande de démarrage est bien configurée")
        print("2. Redémarrez l'App Service dans Azure")
        print("3. Attendez 2-3 minutes supplémentaires")
        print("4. Vérifiez les logs dans Azure Portal")