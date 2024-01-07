import json
from bs4 import BeautifulSoup
import requests
import html_to_json

def importarLoterias():
    url = "https://loteriasdigital.com/modelo/loterias_consulta.php"
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')

    # Encontrar todas las filas de la tabla
    rows = soup.find_all('tr')

    data = []

    # Iterar sobre las filas y extraer los datos
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:  # Asegurarse de que hay 3 celdas por fila
            number = cells[0].text.strip()
            name = cells[1].text.strip()
            data.append({
                'id': number,
                'name': name
            })

    # Convertir los datos a formato JSON
    json_data = json.dumps(data, indent=4)
    return json_data

def obtenerLoteriasReal():
    url = "https://loteriasdominicanas.com/"
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')

    # Encontrar todas las filas de la tabla
    rows = soup.find_all('tr')

    data = []

    # Iterar sobre las filas y extraer los datos
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:  # Asegurarse de que hay 3 celdas por fila
            number = cells[0].text.strip()
            name = cells[1].text.strip()
            data.append({
                'id': number,
                'name': name
            })

    # Convertir los datos a formato JSON
    json_data = json.dumps(data, indent=4)
    return json_data

url = "https://loteriasdominicanas.com/"
response = requests.get(url)
html_text = response.text


# Parsear el HTML usando BeautifulSoup
soup = BeautifulSoup(html_text, 'html.parser')

# Encontrar todos los elementos con la clase especificada
elements_with_class = soup.find_all(class_="game-block mb-3 col-xl-4 col-md-6 col-sm-12 company-block-11")

data = []

# Iterar sobre los elementos y dividir la información en secciones
for element in elements_with_class:
    game_data = {}

    # Encontrar las secciones dentro de cada elemento
    company_title = element.find(class_="company-title")
    game_info = element.find(class_="game-info")
    game_scores = element.find(class_="game-scores")

    # Extraer la información de cada sección
    if company_title:
        game_data['company_title'] = company_title.text.strip()

    if game_info:
        date_element = game_info.find(class_="session-date")
        if date_element:
            game_data['date'] = date_element.text.strip()
        game_title = game_info.find(class_="game-title")
        if game_title:
            game_data['game_title'] = game_title.text.strip()

    if game_scores:
        scores = [score.text.strip() for score in game_scores.find_all(class_="score")]
        game_data['scores'] = scores

    data.append(game_data)

# Convertir los datos a formato JSON
json_data = json.dumps(data, indent=4)
print(json_data)

