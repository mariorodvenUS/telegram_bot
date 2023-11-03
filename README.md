# telegram_bot
Bot de Telegram

# Guía de instalación para el usuario promedio en WINDOWS
Doy por hecho que tienes instalado el vscode(no el visual studio, el vscode, el que es azul) y que has instalado los plugins de python pertinentes, el python extension pack, pylance, intendator, rainbow color brackets... etc.
Si prefieres usar otro IDE, eres libre de hacerlo. Deberás instalar 100% python, desde la microsoft store esta bien. También deberéis descargar(por ultimo) github desktop. Desde github desktop iniciais sesion y seleccionais el repositorio de telegram_bot, seleccionais la branch o rama con vuestro nombre y lo clonais en vuestro PC, ahi solo tendreis que iniciar el vscode en esa carpeta. Antes de empezar a programar nuestro super bot de python to chulo tenemos que usar brevemente la teminal, para ello vamos al VScode en la carpeta del proyecto, abrimos la pestaña de teminal y le damos a nuevo terminal. Ahí escribimos lo siguiente:
```bash
pip install -r requirements     #Instalamos las dependencias de nuestro codigo
```
Para qué nos sirve esto? Muy simple, para que el gestor de paquetes pip instale las dependencias necesarias para que el programa funcione. Principalmente son dos, dotenv y telebot. Dicho esto, a programar!.

# Guía para gigachads que usan GNU/Linux
Vale, como somos unos heroes tenemos pre instalado python, solo tenemos que instalar el vscode y el git, porque si, no tenemos por que instalar el github desktop si no quieres(aunque, te recomiendo que si nunca antes has usado git, lo uses antes que el de terminal). Dando por hecho que tienes instalado linux mint, ubuntu o cualquier derivado de debian que use apt:
```bash
sudo apt install python3-pip git python3.11-venv    #Instalamos los paquetes 
```
Con esto descargamos pip y git. Por otro lado instala vscode o el editor que prefieras. Una vez tengamos todo, clonamos el repositorio(de tu rama, no de la rama main por favor) y escribimos lo siguiente en la terminal:
```bash
python3 -m venv .venv           #Creamos el entorno virtual
source .venv/bin/activate       #Lo activamos
pip install -r requirements     #Instalamos todas las dependencias
```
Y ya estaríamos listos para ponernos a programar. Debo aclarar que el venv hay que activarlo y desactivarlo cada vez que nos pongamos a trabajar, suena a coñazo, pero es por el bien de nuestro ordenador. 
```bash
source .venv/bin/activate   #Para activar el entorno virtual
deactivate                  #Para desacivarlo
```