import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Establecer el título de la aplicación
st.header('Lista de vehículos en venta en USA')

# Crearemos un histograma
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crearemos un gráfico de dispersión
disp_button = st.checkbox(
    'Construir gráfico de dispersión para reflejar las ventas de coches')  # crear un botón

if disp_button:  # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el dataset de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
