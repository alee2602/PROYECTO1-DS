import os
from bs4 import BeautifulSoup #pip install beautifulsoup4 lxml
import pandas as pd

# Ruta de tu carpeta con los archivos .xls
carpeta_entrada = "data/raw"
carpeta_salida = "data/csv"

os.makedirs(carpeta_salida, exist_ok=True)

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith('.xls'):
        nombre_departamento = os.path.splitext(archivo)[0]
        ruta_archivo = os.path.join(carpeta_entrada, archivo)

        with open(ruta_archivo, 'r', encoding='latin1') as f:
            contenido = f.read()

        # Parsear HTML
        soup = BeautifulSoup(contenido, 'lxml')

        # Encontrar la tabla principal por ID
        tabla = soup.find('table', id="_ctl0_ContentPlaceHolder1_dgResultado")

        # Extraer filas
        filas = []
        for fila in tabla.find_all('tr'):
            columnas = [col.get_text(strip=True) for col in fila.find_all('td')]
            if columnas and any(c.strip() for c in columnas):
                filas.append(columnas)

        df = pd.DataFrame(filas[1:], columns=filas[0])

        ruta_csv = os.path.join(carpeta_salida, f"{nombre_departamento}.csv")
        df.to_csv(ruta_csv, index=False, encoding='utf-8-sig')
        print(f"{archivo} convertido y guardado en: {ruta_csv}")
