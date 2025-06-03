# deep_diagnostic.py - Diagnostic final
import requests
import time

def check_azure_logs():
    """Accéder aux logs Azure via l'API"""
    
    print("🔍 Diagnostic approfondi Azure")
    print("=" * 60)
    
    # URLs importantes
    app_url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net"
    scm_url = "https://rcw1001-dhdjeqb7cyfvhkh8.scm.canadacentral-01.azurewebsites.net"
    
    print(f"App URL: {app_url}")
    print(f"SCM URL: {scm_url}")
    print()
    
    # Test 1: Application principale
    print("📱 Test application principale:")
    test_endpoint(app_url + "/")
    
    print("\n📱 Test endpoint /test:")
    test_endpoint(app_url + "/test")
    
    # Test 2: Status Kudu
    print("\n🔧 Test console Kudu (SCM):")
    test_endpoint(scm_url)
    
    print("\n💡 Actions recommandées:")
    print("1. Accédez à la console Azure :")
    print(f"   {scm_url}/DebugConsole")
    print("2. Vérifiez les logs :")
    print(f"   {scm_url}/api/logs/docker")
    print("3. Vérifiez la structure :")
    print("   Dans la console : ls -la /home/site/wwwroot/")

def test_endpoint(url):
    """Tester un endpoint spécifique"""
    try:
        response = requests.get(url, timeout=10)
        print(f"   URL: {url}")
        print(f"   Status: {response.status_code}")
        print(f"   Content-Type: {response.headers.get('content-type', 'Non spécifié')}")
        
        if response.status_code == 503:
            print("   ❌ Service Unavailable - App ne démarre pas")
        elif response.status_code == 200:
            print("   ✅ OK - Service répond")
        else:
            print(f"   ⚠️ Status inattendu: {response.status_code}")
            
        # Aperçu du contenu
        content_preview = response.text[:200].replace('\n', ' ')
        print(f"   Contenu: {content_preview}...")
        
    except Exception as e:
        print(f"   ❌ Erreur: {e}")

def suggest_fixes():
    """Suggestions de corrections"""
    
    print("\n🔧 SOLUTIONS POSSIBLES:")
    print()
    
    print("1. COMMANDE DE DÉMARRAGE (testez ces variantes):")
    print("   Option A: gunicorn -k uvicorn.workers.UvicornWorker main:app")
    print("   Option B: python -m uvicorn main:app --host 0.0.0.0 --port 8000")
    print("   Option C: uvicorn main:app --host 0.0.0.0 --port 8000")
    print()
    
    print("2. VARIABLES D'ENVIRONNEMENT à ajouter:")
    print("   PORT = 8000")
    print("   WEBSITES_PORT = 8000")
    print("   WEBSITE_RUN_FROM_PACKAGE = 1")
    print()
    
    print("3. VÉRIFICATION MAIN.PY:")
    print("   - Assurez-vous qu'il n'y a pas d'erreur de syntaxe")
    print("   - Pas de fonctions avec le même nom")
    print("   - main.py est bien à la racine du projet")
    print()
    
    print("4. REDÉMARRAGE COMPLET:")
    print("   - Arrêter l'App Service")
    print("   - Attendre 30 secondes")
    print("   - Redémarrer")
    print("   - Attendre 2-3 minutes")

if __name__ == "__main__":
    check_azure_logs()
    suggest_fixes()
    
    print("\n🎯 PROCHAINES ÉTAPES:")
    print("1. Accédez à la console Azure Kudu")
    print("2. Vérifiez que main.py existe dans /home/site/wwwroot/")
    print("3. Testez différentes commandes de démarrage")
    print("4. Consultez les logs Docker si disponibles")