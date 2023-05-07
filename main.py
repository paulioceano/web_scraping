import requests
from bs4 import BeautifulSoup

# Se define la URL y se lee el contenido
url = "https://www.recetasnestle.com.pe/recetas/galletas-con-chispas-de-chocolate"
response = requests.get(url)

# Se crea el objeto Beautiful Soup para analizar el contenido
soup = BeautifulSoup(response.content, 'html.parser')

ingredients_section = soup.find("div", attrs={"class": "recipeDetail__ingredients"})
ingredients_list = ingredients_section.find_all('ul')[0]

print(ingredients_list.get_text())
