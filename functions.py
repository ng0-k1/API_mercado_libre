from bs4 import BeautifulSoup
from lxml import etree
import requests

def productos(productos):
    lista_titulos = []
    lista_url = []
    lista_precios = []
    
    siguiente = f'https://listado.mercadolibre.com.co/{productos}'
    print(siguiente)
    while True:
        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')       
            #Titulos
            titulo = soup.find_all('h2',{'class':"ui-search-item__title"})
            titulo = [i.text for i in titulo]
            lista_titulos.extend(titulo)
            #Url
            url = soup.find_all('a', {'class' : "ui-search-item__group__element ui-search-link"})
            url = [j.get('href') for j in url]
            lista_url.extend(url)
            #Precios
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//ol/li/div/div/div[2]/div/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            #inicial
            inicio = soup.find('span', {'class':"andes-pagination__link"})
            inicio = int(inicio.text)
            #Fin
            fin = soup.find('li', {'class':"andes-pagination__page-count"}).text
            fin = int(fin.split(" ")[1])
        else:
            print('No se puede acceder a la pagina socilitada')
            break
        print(inicio, fin)
        if inicio == fin:
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination"]/ul/li[contains(@class, "button--next")]/a')[0].get('href')  
    return lista_titulos, lista_url, lista_precios

def limiteProducto(productos, limite):
    lista_titulos = []
    lista_url = []
    lista_precios = []
    
    siguiente = f'https://listado.mercadolibre.com.co/{productos}'
    print(siguiente)
    while True:
        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')       
            #Titulos
            titulo = soup.find_all('h2',{'class':"ui-search-item__title"})
            titulo = [i.text for i in titulo]
            lista_titulos.extend(titulo)
            #Url
            url = soup.find_all('a', {'class' : "ui-search-item__group__element ui-search-link"})
            url = [j.get('href') for j in url]
            lista_url.extend(url)
            #Precios
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//ol/li/div/div/div[2]/div/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            #inicial
            inicio = soup.find('span', {'class':"andes-pagination__link"})
            inicio = int(inicio.text)
            #Fin
            fin = soup.find('li', {'class':"andes-pagination__page-count"}).text
            fin = int(fin.split(" ")[1])
        else:
            print('No se puede acceder a la pagina socilitada')
            break
        print(inicio, fin)
        if len(lista_titulos)>=int(limite):
            return lista_titulos[:limite], lista_url[:limite], lista_precios[:limite]
        if inicio == fin:
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination"]/ul/li[contains(@class, "button--next")]/a')[0].get('href')  
    return lista_titulos, lista_url, lista_precios












