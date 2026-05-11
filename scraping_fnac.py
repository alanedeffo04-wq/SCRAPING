
import requests
from bs4 import BeautifulSoup
import csv

 # URL de la page à scraper # type: ignore
url = "https://www.fnac.com/SearchResult/ResultList.aspx?Search=chargeur+iphone&sft=1&sa=1"

 #Headers pour simuler un vrai navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers)

 #Vérification
if response.status_code == 200:

    #  Analyse du HTML
    soup = BeautifulSoup(response.text, "lxml")

    # 6. Récupération des blocs produits
    produits = soup.find_all("article")

    resultats = []

    # Extraction des données
    for produit in produits:
        nom = produit.find("h2")
        prix = produit.find("span", class_="Article-price")

        if nom and prix:
            resultats.append({
                "nom_produit": nom.get_text(strip=True),
                "prix": prix.get_text(strip=True)
            })

    # Export en CSV
    with open("fnac_chargeur_iphone.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=["nom_produit", "prix"])
        writer.writeheader()
        writer.writerows(resultats)

    print(" Scraping terminé. Fichier créé.")

else:
    print(" Erreur HTTP :", response.status_code)
