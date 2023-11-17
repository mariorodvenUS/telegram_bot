import json
import datetime

# esto se puede optimizar en memoria pero no lo hago para mantener la legibilidad
def coger(llavero):
    #conseguimos la fecha cuando se escribio el mensaje y le cambiamos el formato para adaptarlo al .json y librarnos de los microsegundos
    fecha_mensaje = datetime.datetime.now()
    fecha_json = datetime.datetime.strftime(fecha_mensaje, "%Y,%m,%d %H,%M,%S")
    fecha_mensaje = datetime.datetime.strftime(fecha_mensaje, "%H:%M:%S")

    #divimos el string del datetime para poder meterlo guay en un diccionario
    # Split the date and time string by space
    date_str, time_str = fecha_json.split(" ")

    # Split the date string by comma
    year, month, day = date_str.split(",")

    # Split the time string by comma
    hour, minute, second = time_str.split(",")

    # Modificamos el diccionario
    datos_llave = {
        "llavero": llavero,
        "fecha":{ 
                "anio": year,
                "mes": month,
                "dia": day,
        },                  
        "tiempo": {   
            "hora": hour,
            "minuto": minute,
            "segundo": second
        }
    }
    #escribimos en el json    
    with open("llave.json", "w") as archivo:
        json.dump(datos_llave, archivo, indent=4)
    return fecha_mensaje

def consultar():
    try:
        with open("llave.json", "r") as archivo:
            datos_llave = json.load(archivo)
        return datos_llave["llavero"]
    except FileNotFoundError:
        print("Ha pasado algo, y es que el archivo no existe, escribe el comando //llave o //llavent para crearlo")
        return -1

def dejar():
    try:
        with open("llave.json", "r") as archivo:
            dict = json.load(archivo)
    except FileNotFoundError:
        print("Ha pasado algo, y es que el archivo no existe, escribe el comando //llave o //llavent para crearlo")
        return -1   
    if "conserjeria" in dict.values():
        print("Han intentado dejar la llave donde ya está, en consejeria")
        return -2
    else:
        #conseguimos la fecha cuando se escribio el mensaje y le cambiamos el formato para adaptarlo al .json y librarnos de los microsegundos
        fecha_mensaje = datetime.datetime.now()
        fecha_json = datetime.datetime.strftime(fecha_mensaje, "%Y,%m,%d %H,%M,%S")
        fecha_mensaje = datetime.datetime.strftime(fecha_mensaje, "%H:%M:%S")

        #divimos el string del datetime para poder meterlo guay en un diccionario
        # Split the date and time string by space
        date_str, time_str = fecha_json.split(" ")

        # Split the date string by comma
        year, month, day = date_str.split(",")

        # Split the time string by comma
        hour, minute, second = time_str.split(",")

        # Modificamos el diccionario
        datos_llave = {
            "llavero": "conserjeria",
            "fecha":{ 
                    "anio": year,
                    "mes": month,
                    "dia": day,
            },                  
            "tiempo": {   
                "hora": hour,
                "minuto": minute,
                "segundo": second
            }
        }
        #escribimos en el json    
        with open("llave.json", "w") as archivo:
            json.dump(datos_llave, archivo, indent=4)
        return fecha_mensaje