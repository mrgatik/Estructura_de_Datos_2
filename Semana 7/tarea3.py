

import requests

resp = requests.get("https://swapi.co/api/films/")
data = resp.json()
epinfo = data['results']
episodiouno = epinfo[0]
print("El primer episodio de STAR WARS titulado: " + episodiouno['title'] + ", tiene " + str(len(episodiouno['characters'])) + " personajes ")


mayor = 0
epindex = 0

cantidadpeliculas = data['count']

for x in range(cantidadpeliculas):
    ep = epinfo[x]
    crawling = ep['opening_crawl']

    for i in range(cantidadpeliculas):

        num = len(crawling)
        if num > mayor:
            mayor = num
            epindex = epinfo[x + 1]


print("La pelicula STAR WARS:" + epindex['title'] + " tiene el opening mas alto con " + str(mayor) + " letras")