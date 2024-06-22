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

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: "Imagen.jpeg";
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Con formato de Markdown centramos y agrandamos la letra del título de la web en streamlit
st.markdown("<h1 style='text-align: center; color: #006633;'>¡Bienvenido al Conjugador de Verbos en Quechua!</h1>", unsafe_allow_html=True)
st.write("¡Explora la riqueza del quechua conjugando verbos en diferentes tiempos y personas!")
# st.markdown("<h1 style='text-align: center;'>Conjugador de verbos en quechua</h1>", unsafe_allow_html=True)
# style='text-align: center;' es para centrar el título
# unsafe_allow_html=True es para permitir el uso de HTML en Streamlit
# <h1> es para el tamaño de la letra del título


# Creamos una variable file_name para guardar la ruta de la base de datos de quechua
#file_name = "/Users/jamesmedinavanini/Downloads/Tarea 4/Copia de quechuaCA.xlsx"
file_name = "\\Users\\jamesmedinavanini\\Downloads\\Tarea 4\\Copia de quechuaCA.xlsx"

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

# Definir el diccionario con los tiempos verbales y sus descripciones
tiempos_con_descripciones = [
    ("Presente simple", "Indica acciones que ocurren en el presente sin indicar duración específica."),
    ("Presente progresivo", "Indica acciones que están en progreso en el presente."),
    ("Presente habitual", "Se utiliza para expresar acciones que se repiten con frecuencia en el presente."),
    ("Participio pasado", "Es la forma del verbo utilizada para formar tiempos compuestos o expresar acciones finalizadas en el pasado."),
    ("Pasado experimentado simple", "Expresa acciones pasadas que fueron experimentadas personalmente por el hablante."),
    ("Pasado experimentado progresivo", "Indica acciones que estaban en progreso en el pasado y fueron experimentadas personalmente por el hablante."),
    ("Pasado experimentado habitual", "Se utiliza para expresar acciones habituales en el pasado, experimentadas personalmente por el hablante."),
    ("Pasado no experimentado simple", "Expresa acciones que ocurrieron en el pasado pero no fueron experimentadas personalmente por el hablante."),
    ("Pasado no experimentado progresivo", "Indica acciones que estaban en progreso en el pasado pero no fueron experimentadas personalmente por el hablante."),
    ("Pasado no experimentado habitual", "Se utiliza para expresar acciones habituales en el pasado que no fueron experimentadas personalmente por el hablante.")
]



# Número de elementos por fila
elementos_por_fila = 3

# Crear una lista de títulos, descripciones y dataframes
titulos = [tiempos_con_descripciones[i][0] for i in range(len(tiempos_con_descripciones))]
descripciones = [tiempos_con_descripciones[i][1] for i in range(len(tiempos_con_descripciones))]
dataframes = [pd.DataFrame(data) for hoja, data in D.items()]

# Iterar sobre los dataframes y mostrar en tres filas
for i in range(0, len(titulos), elementos_por_fila):
    col1, col2, col3 = st.columns(3)  # Crear tres columnas
    for j, col in enumerate([col1, col2, col3]):
        index = i + j
        if index < len(titulos):
            col.header(titulos[index])  # Mostrar título
            col.write(descripciones[index])  # Mostrar descripción
            col.write(dataframes[index])  # Mostrar dataframe



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
#file_name_2 = "/Users/jamesmedinavanini/Downloads/Tarea 4/Copia de pronombresCA.xlsx"
file_name_2 = "\\Users\\jamesmedinavanini\\Downloads\\Tarea 4\\Copia de pronombresCA.xlsx"

# Leemos el DataFrame de la base de datos de pronombres en quechua con la función read_excel de Pandas
pronombres_hojas = pd.ExcelFile("Copia de pronombresCA.xlsx")
# "Copia de pronombresCA.xlsx" es el nombre de la base de datos de pronombres en quechua
# pd.ExcelFile es para leer la base de datos de pronombres en quechua

# Creamos un diccionario vacío DP
DP = {}
for hoja in pronombres_hojas.sheet_names:
    dfp = pd.read_excel("Copia de pronombresCA.xlsx", sheet_name=hoja)
    c = dfp.columns
    dfp.set_index(c[0], inplace=True)
    dp = dfp.to_dict()
    DP[hoja] = dp


# Mostramos todos los dataframes de los pronombres en quechua (opcional)
st.write("### Los pronombres en quechua son:", dfp)

# Creamos una función conjtotal para conjugar verbos en quechua con pronombres
def pronombre(numero, persona):
    return DP['Hoja 1'][numero][persona]

# La función conjtotal recibe cuatro parámetros: base, número, persona y tiempo
# La función conjtotal devuelve la conjugación del verbo en quechua con pronombres
vocales = ['a', 'i', 'u']
def conjtotal(base, numero, persona, tiempo):
    if base[-1] not in vocales:
        base = base[:-1]
    return base + D[tiempo][numero][persona]

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
tiempo = st.selectbox("Seleccione el tiempo:", ['Presente simple', 'Presente progresivo','Presente habitual', 'Participio pasado', 'Pasado experimentado simple', 'Pasado experimentado progresivo', 'Pasado experimentado habitual ', 'Pasado no experimentado simple', 'Pasado noexperimentado progresi', 'Pasado noexperimentado habitual'])

# Creamos una condición para conjugar verbos en quechua
# Si la base y la persona y el número y el tiempo son verdaderos
# Entonces creamos una función conjugador para conjugar verbos en quechua
if st.button("Conjugar"):
        if base and persona and numero and tiempo:
            try:
                palabra_conjugada = conjtotal(base, numero, persona, tiempo)
                pronombre_conjugado = pronombre(numero, persona)
                st.write(f'El verbo conjugado es: {pronombre_conjugado} {palabra_conjugada}')
            except Exception as e:
                st.warning("La conjugación no es posible.")
                st.warning(":(")
        else:
            st.warning("Por favor, complete todos los campos.")


st.write("Limitaciones:")
st.write("- Algunos verbos pueden tener formas irregulares que no están cubiertas.")

# Mensaje de agradecimiento
st.write("## ¡Gracias por explorar el conjugador de verbos en quechua! 🌟 Esperamos que hayas disfrutado utilizando esta herramienta. 🌷")



