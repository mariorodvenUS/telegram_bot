import json
import datetime

#def nuevo_llavero():


#leemos del json
with open("llave.json") as archivo:
    datos_llave = json.load(archivo)
    archivo.close()

print(datos_llave)    
escritor = "Alvarito"


#conseguimos la fecha cuando se escribio el mensaje y le cambiamos el formato para adaptarlo al .json y librarnos de los microsegundos
fecha_mensaje = datetime.datetime.now()
fecha_json =datetime.datetime.strftime(fecha_mensaje, "%Y,%m,%d %H,%M,%S")
print(fecha_json)

#divimos el string del datetime para poder meterlo guay en un diccionario
# Split the date and time string by space
date_str, time_str = fecha_json.split(" ")

# Split the date string by comma
year, month, day = date_str.split(",")

# Split the time string by comma
hour, minute, second = time_str.split(",")

# Modificamos el diccionario
datos_llave = {
    "llavero": escritor,
    "fecha":{ 
            "anio": year,
            "mes": month,
            "dia": day,
    },                  #todas estas variables yo creo que en string estan bien
    "tiempo": {   
            "hora": hour,
            "minuto": minute,
            "segundo": second
    }
}
print(datos_llave)


#escribimos en el json    
with open("llave.json", "w") as archivo:
    json.dump(datos_llave, archivo, indent=4)
    archivo.close()
    
