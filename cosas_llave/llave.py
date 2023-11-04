import json


#def nuevo_llavero():

#leemos del json
with open("llave.json") as archivo:
    dict_datos = json.load(archivo)
    archivo.close()
print(dict_datos)    
#chequear si la fecha y la hora son posibles
#chequeo anio
if dict_datos["fecha"]["anio"]<2023:    
    print("año feo")
#cheqeuo mes    
if dict_datos["fecha"]["mes"]>13:
   print("mes feo")     
#cheqeuo dia   
if dict_datos["fecha"]["mes"] in [1, 3, 5, 7, 8, 10, 12] and dict_datos["fecha"]["dia"]>31:
    print("dia feo")   
elif dict_datos["fecha"]["mes"] in [4, 6, 9, 11] and dict_datos["fecha"]["dia"]>30:
    print("dia feo")
elif dict_datos["fecha"]["mes"] == 2 and dict_datos["fecha"]["dia"]>29:
    print("dia feo")        
#cheqeuo hora
if dict_datos["tiempo"]["hora"]>24:
    print("hora fea")
if dict_datos["tiempo"]["minuto"]>59:
    print("minuto feo")
if dict_datos["tiempo"]["segundo"]>59:
    print("segundo feo")        
#escribimos en el json    
with open("llave.json", "w") as archivo:
    json.dump(dict_datos, archivo, indent=4)
    archivo.close()
    














