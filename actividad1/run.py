import csv
import PySimpleGUI as sg
import json


def buscar_info(ruta):
        arch = open(ruta,'r')
        data = list(csv.reader(arch))
        return data

layout =[[sg.Text('Elija la informacion que desea ver')],
         [sg.Button(button_text="Regiones que buscaron coronavirus")],
         [sg.Button(button_text="Calendario de eventos")],
         [sg.Cancel()]]

window = sg.Window('Enunciado Actividad  1 (TEORIA) ', layout, margins=(200, 150))
while True:
    
    event, values = window.read()
    if event == None or event =='Cancel':
        break

    
    """google busqueda coronavirus argentina
        Consulta en qué ubicación se ha usado con más frecuencia tu término de búsqueda durante el periodo especificado. 
        Los valores se calculan en una escala del 0 al 100, en la que 100 indica la ubicación con mayor frecuencia 
        de búsquedas en proporción al total de búsquedas realizadas en esa ubicación, mientras que los valores 
        de 50 y 0 indican las ubicaciones donde la popularidad del término es la mitad con relación al valor máximo o 
        en las que no había suficientes datos del término, respectivamente.
    """
    if event == 'Regiones que buscaron coronavirus':
        data = buscar_info('./geoMap.csv')
        lista = []  
        for linea in data:
                lista.append(linea)
        
        with open("file.json", "w", encoding="utf8") as file:
            json.dump(lista,file, indent=4, separators=(',',';'), ensure_ascii=False)
        print("En file.json se guardan los datos de todos los paises ")

    
    #La idea es que guarde en el file.json los nombres de los eventos(linea[2]) de los dias sabados(linea[4]), pero no supe como arreglarlo
    
    elif event == 'Calendario de eventos':
        data = buscar_info('./calendario-de-eventos-dir-gral-de-musica.csv')
        lista = []  
        for linea in data:
            if linea[4] == "SABADO":
                lista.append(linea[2])
        with open("file.json", "w", encoding="utf8") as file:
            json.dump(lista,file, indent=4, separators=(';'), ensure_ascii=False)
            
    
    


