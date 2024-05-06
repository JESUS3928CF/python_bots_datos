import pandas as pd
import requests

# Carga datos desde archivos
cancer_mama = pd.read_excel("breast_cancer.xlsx")
titanic = pd.read_csv("titanic.csv")
vino_rojo = pd.read_csv('red_wine.csv', sep=';')

# Imprime algunas filas de vino_rojo
print(vino_rojo.head(10))
print(vino_rojo.tail())

 # Realiza la solicitud GET a la API y convierte la respuesta JSON en un diccionario
response = requests.get('https://dummyjson.com/products')
json_productos = response.json()

# Crea un DataFrame a partir del diccionario dentro del JSON
datos_productos = pd.DataFrame(json_productos['products'])

print(datos_productos)