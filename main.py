import os, time
import errno
import requests 
from bs4 import BeautifulSoup as bs

try:
  # Verificamos el modulo de google
  from googlesearch import search
except ImportError:
  os.system('pip install google')
  print('Installing google... ')
  os.system('clear')
  # exit()

# Almacenamos el nombre del equipo/jugador deportivo: mcgregor
query = input("Buscar Informacion del Equipo/Atleta: ")
print("Buscando...")
time.sleep(2)
os.system('clear')

try:
  # Creamos una carpeta para almacenar la urls de lo que se esta investigando
  os.mkdir('url')
except OSError as e:
  if e.errno != errno.EEXIST:
    raise

# Iniciamos el numero de urls
urls = 0
# Creamos el archivo para almacenar las urls
file = open("url/urls.txt", "w")

for enlace in search(query, tld="com.mx"):
  # Dentro del archivo escribimos los urls
  file.write(enlace+os.linesep)
  # El numero de urls permitido
  if urls == 20:
    file.close()
    break
  urls += 1

# Verificar el contenido del archivo con las urls
file = open("url/urls.txt", "r")
read = file.readlines()
for url in read:
  # Se imprime las urls de la investigacion
  pagina = requests.get(url)  
  if pagina.status_code != 200:
    print(url," estatus: ", pagina.status_code)   
  else:
    soup = bs(pagina.content, 'html.parser')
    print(url," estatus: ", pagina.status_code)