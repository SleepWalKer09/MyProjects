from selenium import webdriver
from bs4 import BeautifulSoup

#clase para el parseo de direcciones
def get_address(data):
    part = data.split(",")
    partAmount = len(part)
    if(partAmount == 3):
        return {'address' : part[0],'city' : part[1], 'region' : part[2]}
    elif(partAmount > 3):
        return {'address' : " ".join(part[:len(part)-3]), 'city' : part[partAmount-2], 'region' : part[partAmount-1]}
    elif(partAmount < 3):
        for i in range(0,100):
            print("error:")
            print(data)
        return {'address' : 'FAIL','city' : 'FAIL', 'region' : data}


url = 'https://listado.mercadolibre.com.mx/apartamentos-inmuebles'
#se abre un navegador para poder manejarlo desde python usando el geckodriver de firefox
driver = webdriver.Firefox(executable_path='geckodriver')
driver.get(url)
#trae todo el codigo html
html_code = driver.page_source

#se obtienen los datos importantes del html (hacer scraping)
#bs4 encuentra mas facilmente el codigo html requerido
#creando un objeto de BS4 a partir del html con el parser "lxml"
soup = BeautifulSoup(html_code, 'lxml')
#dentro de la url los objetos necesarios se llaman "li"
#encontrar todos los "li" que contengan la clase "ui-search-layout_item"
todas_casas_li = soup.find_all("li", class_="ui-search-layout_item")
#casas_li = todas_casas_li[0]


def casas_li_html_to_obj(casas_li_html):
    #se obtienen las imagenes de las etiquetas html de donde se encuentran
    img = casas_li_html.find("img")
    try:
        img_url = img["data-src"]
    except:
        img_url = img["src"]

    #obtener precios de casas 
    precio = casas_li_html.find(class_= "price-tag-fraction").text.replace(".","")
    #obtener titulo de casa
    titulo = casas_li_html.find(class_= "ui-search-item_title").text
    #obtener direccion
    loc = casas_li_html.find( class_ = "ui-search-item_location ").text
    loc = get_address(loc)
    #obtiene tamaño y/o cantidad habitaciones
    todos_atributos = casas_li_html.find_all (class_ = "ui-search-card-attribute")
    size = ""
    recamara = ""
    if (len(todos_atributos) > 0):
        if("cubiertos" in todos_atributos[0].text):
            size = todos_atributos[0].text
        else:
            recamara = todos_atributos[0].text
    if (len(todos_atributos) > 1):
        recamara = recamara  = todos_atributos[1].text
    #link al html de la publicacion
    url = casas_li_html.find("a")["href"]
    #devuelve el objeto
    return {"img_url": img_url, "precio": precio , "titulo": titulo,'address': loc['address'], 'city': loc['city'],'region': loc['region'], "size" : size, "recamara ": recamara , "url": url}


for casas_li in todas_casas_li:
    print(casas_li_html_to_obj(casas_li))