import asyncio
import pandas as pd
import requests

# Define una función asíncrona para obtener productos de una API y exportarlos a un archivo Excel
async def obtener_productos_y_exportar():
    try:
        # Realiza la solicitud GET a la API y convierte la respuesta JSON en un diccionario
        response = await asyncio.to_thread(requests.get, 'https://dummyjson.com/products')
        json_productos = response.json()

        # Crea un DataFrame a partir del diccionario dentro del JSON
        datos_productos = pd.DataFrame(json_productos['products'])

        # Exporta el DataFrame a un archivo Excel
        nombre_archivo = "productos.xlsx"
        datos_productos.to_excel(nombre_archivo, index=False)
        print("DataFrame exportado a Excel como:", nombre_archivo)

    except Exception as e:
        print("Se ha producido un error:", e)

# Define una función asíncrona para cargar datos desde archivos CSV y Excel
async def cargar_datos_desde_archivos():
    # Carga datos desde archivos
    cancer_mama = pd.read_excel("breast_cancer.xlsx")
    titanic = pd.read_csv("titanic.csv")
    vino_rojo = pd.read_csv('red_wine.csv', sep=';')

    # Imprime algunas filas de vino_rojo
    print(vino_rojo.head(10))
    print(vino_rojo.tail())

# Define una función principal asíncrona para ejecutar las funciones anteriores
async def main():
    # Ejecuta las funciones obtener_productos_y_exportar y cargar_datos_desde_archivos de manera simultánea
    await asyncio.gather(
        obtener_productos_y_exportar(),
        cargar_datos_desde_archivos()
    )

    input("Presione cualquier tecla para salir: ");

# Ejecuta la función main utilizando asyncio.run() para configurar automáticamente el bucle de eventos
asyncio.run(main())
