#Instrucciones:
#Hacer scrapping a la web de timejobs y traer datos sobre alguna vacante de interes
#1.Las vacantes deben ser recientes
#2.El usuario pone habilidades desconocidas para que filtre custom
#3.Se deben guardar los resultados en otro archivo diferente

from bs4 import BeautifulSoup
import requests
import time

print('Escribe una habilidad que NO domines')
unfamiliar = input('>')
print(f'Filtrado Eliminado: {unfamiliar}')

def busqueda():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    trabajos = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #por cada vacante en toda la pagina
    for index, trabajo in enumerate (trabajos):
        #se pone la fecha primero para evitar gasto de recursos en caso que la fecha no sea reciente
        fecha_publi = trabajo.find('span', class_ = 'sim-posted').span.text #entrar en la etiqueta "span"
        if 'few' in fecha_publi:
            empresa = trabajo.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            habilidades = trabajo.find('span', class_ = 'srp-skills').text.replace(' ','')    
            info = trabajo.header.h2.a['href'] #link para saber mas acerca del trabajo
            
            #filtro para desaperecer habilidades que no domina
            if unfamiliar not in habilidades:
                with open(f'Vacantes/{index}.txt', 'w') as f:
                    #se agrega un poco de formato a los resultados
                    f.write(f"Empresa: {empresa.strip()} \n")
                    f.write(f"Habilidades Necesarias: {habilidades.strip()} \n")
                    f.write(f"Publicado: {empresa.strip()} \n")
                    f.write(f"Info: {info.strip()} \n")
                print(f'Archivo guardado: {index}')
                    

if __name__ == '__main__':
    #para evitar problemas el programa se ejecuta cada 10 min
    while True:
        busqueda()
        espera = 10 #minutos
        print(f"Esperando {espera} minutos...")
        time.sleep(espera * 60)#|