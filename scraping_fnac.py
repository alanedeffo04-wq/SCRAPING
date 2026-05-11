
import requests
from bs4 import BeautifulSoup
import csv

URL de la page à scraper
url = "https://www.fnac.com/SearchResult/ResultList.aspx?Search=chargeur+iphone&sft=1&sa=1"

 Headers pour simuler un vrai navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers)