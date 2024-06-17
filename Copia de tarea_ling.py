# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.

# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra 
# tus archivos en el terminal Python
# cd ruta_de_tu_carpeta 
# o abrir la carpeta donde se encuentra tus archivos con open folder y 
# crear un archivo de Python (your_script.py) 

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

import streamlit as st  
#Importamos Streamlit: esta biblioteca de Python facilita la creación y visualización de páginas web interactivas 
import pandas as pd  
#Importamos Pandas: esta biblioteca sirve para el análisis de datos tabulados en Python
import os 
#Esta librería proporciona una interfaz para interactuar con el sistema operativo (manipulación de rutas, la creación y eliminación de directorios, y la obtención de información sobre archivos)

# Con formato de Markdown centramos y agrandamos la letra del título de la web en streamlit
st.markdown("<h1 style='text-align: center;'>Conjugador de verbos en quechua</h1>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center;'>Conjugador de verbos en quechua</h1>", unsafe_allow_html=True)
# style='text-align: center;' es para centrar el título
# unsafe_allow_html=True es para permitir el uso de HTML en Streamlit
# <h1> es para el tamaño de la letra del título

# Creamos una variable file_name para guardar la ruta de la base de datos de quechua
file_name = "\\Users\\jamesmedinavanini\\Downloads\\Tarea 4\\Copia de quechuaCA.xlsx"
# "C:\\Users\\Luisa\\Desktop\\Camila_quechua\\Copia de quechuaCA.xlsx" es la ruta de la base de datos de quechua

# Leemos el DataFrame de la base de datos de quechua con la función read_excel de Pandas
quechua = pd.read_excel("Copia de quechuaCA.xlsx")  
# "Copia de quechuaCA.xlsx" es el nombre de la base de datos de quechua
# pd.read_excel es para leer la base de datos de quechua

# Mostramos el DataFrame de la base de datos de quechua (opcional)
# quechua

# Creamos otra variable para guardar 
quechua_hojas = pd.ExcelFile("Copia de quechuaCA.xlsx")
# "Copia de quechuaCA.xlsx" es el nombre de la base de datos de quechua
# pd.ExcelFile es para leer la base de datos de quechua

# Mostramos las hojas de la base de datos de quechua (opcional)
# quechua_hojas.sheet_names

# Creamos un diccionario vacío D
D = {}

# Leemos la base de datos de quechua y la guardamos en el diccionario D
for hoja in quechua_hojas.sheet_names:
    # Leemos la base de datos de quechua con la función read_excel de Pandas
    df = pd.read_excel("Copia de quechuaCA.xlsx", sheet_name = hoja)
    c = df.columns
    df.set_index(c[0], inplace = True)
    # Convertimos el DataFrame en un diccionario
    d = df.to_dict()
    # Guardamos el diccionario en el diccionario D
    D[hoja] = d

# Mostramos el diccionario de la base de datos de quechua (opcional)
# D

# Mostramos todos los dataframes de la base de datos de quechua (opcional)
for hoja, data in D.items():
  st.write(f"Conjugación del quechua en {hoja}:")
  st.write(pd.DataFrame(data))
# st.write(f"Conjugación del quechua en {hoja}:", pd.DataFrame(data))
# f"Conjugación del quechua en {hoja}:" es para mostrar el nombre de la hoja
# pd.DataFrame(data) es para mostrar el DataFrame de la hoja
# st.write es para mostrar el nombre de la hoja y el DataFrame de la hoja

# Creamos una función conjugador para conjugar verbos en quechua
# La función conjugador recibe cuatro parámetros: base, número, persona y tiempo
# La función conjugador devuelve la conjugación del verbo en quechua
def conjugador(base,numero,persona,tiempo):
  return base + D[tiempo][numero][persona]

# Creamos una variable palabra para guardar la conjugación de un verbo en quechua
palabra = conjugador('miku', 'singular', 'segunda', 'Presente habitual')
# 'miku' es la base del verbo en quechua
st.write("Ejemplo: La conjugación de 'miku' es", palabra)

# Creamos un espacio para ingresar la base de los pronombres en quechua
file_name_2 = "\\Users\\jamesmedinavanini\\Downloads\\Tarea 4\\Copia de pronombresCA.xlsx"

# Leemos el DataFrame de la base de datos de pronombres en quechua con la función read_excel de Pandas
pronombres = pd.ExcelFile("Copia de pronombresCA.xlsx")
# "Copia de pronombresCA.xlsx" es el nombre de la base de datos de pronombres en quechua
# pd.ExcelFile es para leer la base de datos de pronombres en quechua

# Creamos un diccionario vacío DP
DP = {}
# Leemos la base de datos de pronombres en quechua y la guardamos en el diccionario DP
for hoja in pronombres.sheet_names:
    dfp = pd.read_excel("Copia de quechuaCA.xlsx")
    c = df.columns
    dfp.set_index(c[0], inplace = True)
    dp = df.to_dict()

# Mostramos el diccionario de los pronombres en quechua (opcional)
# dp

# Mostramos todos los dataframes de los pronombres en quechua (opcional)
st.write("Los pronombres en quechua son:", dfp)

# Creamos una función conjtotal para conjugar verbos en quechua con pronombres
# La función conjtotal recibe cuatro parámetros: base, número, persona y tiempo
# La función conjtotal devuelve la conjugación del verbo en quechua con pronombres
def conjtotal(base,numero,persona,tiempo):
  return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]

# Creamos una variable palabra_conjugada para guardar la conjugación de un verbo en quechua con pronombres
palabra_conjugada = conjtotal('tiya','singular','tercera','Pasado experimentado simple')

# 'tiya' es la base del verbo en quechua
st.write("Ejemplo: La conjugación de 'tiya' y su pronombre es", palabra_conjugada)

# Creamos un espacio para ingresar la base de los verbos en quechua
base = st.text_input("Ingrese la base para conjugar:")

# Creamos un espacio para seleccionar la persona en quechua
persona = st.selectbox("Seleccione la persona:", ['primera', 'segunda', 'tercera', 'cuarta'])

# Creamos un espacio para seleccionar el número en quechua
numero = st.selectbox("Seleccione el número:", ['singular', 'plural'])

# Creamos un espacio para seleccionar el tiempo en quechua
tiempo = st.selectbox("Seleccione el tiempo:", ['Presente simple', 'Presente progresivo','Presente habitual', 'Participio pasado', 'Pasado experimentado simple', 'Pasado experimentado progresivo', 'Pasado experimentado habitual', 'Pasado no experimentado simple', 'Pasado noexperimentado progresi', ' Pasado noexperimentado habitual'])

# Creamos una condición para conjugar verbos en quechua
# Si la base y la persona y el número y el tiempo son verdaderos
# Entonces creamos una función conjugador para conjugar verbos en quechua
if base and persona and numero and tiempo:
    def conjugador(base,numero,persona,tiempo):
      return base + D[tiempo][numero][persona]
    
    # Creamos una variable palabra_conjugada para guardar la conjugación de un verbo en quechua
    palabra_conjugada = conjugador(base, numero, persona, tiempo)
    
    # Mostramos la conjugación del verbo en quechua
    st.write("La conjugación es:", palabra_conjugada)
