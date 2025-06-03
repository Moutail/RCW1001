# quick_debug.py - Voir exactement ce que retourne Azure
import requests

url = "https://rcw1001-dhdjeqb7cyfvhkh8.canadacentral-01.azurewebsites.net/test"

print("🔍 Debug rapide - Que retourne vraiment Azure ?")
print(f"URL: {url}")
print("=" * 60)

try:
    response = requests.get(url)
    
    print(f"📊 Status Code: {response.status_code}")
    print(f"📄 Content-Type: {response.headers.get('content-type', 'Non spécifié')}")
    print(f"📏 Taille: {len(response.content)} bytes")
    print()
    
    print("📝 CONTENU BRUT:")
    print("-" * 30)
    print(response.text)
    print("-" * 30)
    
    # Analyse du contenu
    if response.status_code == 200:
        print("✅ Status 200 - L'application répond")
        
        if response.text.strip().startswith('{'):
            print("✅ Semble être du JSON")
            try:
                data = response.json()
                print(f"✅ JSON valide: {data}")
            except:
                print("❌ JSON malformé")
        else:
            print("❌ Ce n'est PAS du JSON")
            if response.text.strip().startswith('<'):
                print("🌐 C'est du HTML (probablement une page d'erreur)")
    else:
        print(f"❌ Erreur HTTP {response.status_code}")
        print("🔍 Votre application Azure a un problème")
    
except Exception as e:
    print(f"❌ Erreur de connexion: {e}")

print("\n💡 INTERPRÉTATION:")
print("Si vous voyez du HTML au lieu de JSON, cela signifie:")
print("1. Votre app Azure ne démarre pas correctement")
print("2. Il y a une erreur dans votre code Python")
print("3. Azure retourne une page d'erreur")