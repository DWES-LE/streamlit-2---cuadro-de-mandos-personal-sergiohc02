import pandas as pd
import streamlit as st

# Load data

df = pd.read_csv("races.csv")

#Título de la página

st.title("F1 World Championship")

# Mostramos los datos de la tabla

st.subheader("Todos los datos de la tabla")

st.write(df)

# Hago un gráfico de barras para saber los campeonatos celebrados en cada circuito

st.subheader("Campeonatos celebrados en cada circuito")

datos=(df.groupby("name").count()["year"].sort_values(ascending=False))

st.bar_chart(datos)

# Hacemos que el usuario pueda filtrar los campeonatos por año

st.subheader("Filtrar por año")

# Crear widget de entrada de texto para el año
year = st.text_input('Introduzca el año a filtrar: ')

# Verificar que el valor de entrada no está vacío
if year != '':
    # Filtrar datos por año
    filtered_data = df[df['year'] == int(year)]

    # Mostrar datos filtrados
    st.write(filtered_data)
else:
    # Si el valor de entrada está vacío, mostrar un mensaje de error
    st.write('Introduce un año válido')