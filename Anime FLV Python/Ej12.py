"""Anime FLV Propio"""
"""NO FUNCIONAL"""

from animeflv import AnimeFLV
with AnimeFLV() as api:
    
    
    elementos = api.search(input("Ingrese nombre del Anime: "))
    for i, elemento in enumerate(elementos):
        print(f"{i}, {elemento.title}")
    try:
        eleccion= int(input("Seleccione opcion: "))
        info = api.get_anime_info(elementos[eleccion].id)
        info.episodes.reverse()
        for n, episode in enumerate(info.episodes):
            print(f"{n}| Episodio - {episode.id}")
        indice_episodio = int(input("Seleccione episodio: "))
        serie = elementos[eleccion].id
        capitulo = info.episodes[indice_episodio].id
        resultados = api.get_links(serie, capitulo)
        for resultado in resultados:
            print(f"{resultado.server}-{resultado.url}")
    except Exception as e:
        print(e)
            
        

