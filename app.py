"""
Proyecto Sprint 7
-----------------
Este módulo carga un archivo de la carpeta data y realiza el análisis exploratorio de 
datos

Functions
---------
cargar_datos(ruta)
    Carga un archivo CSV con datos de inventario.
calcular_margen(df)
    Calcula el margen de ganancia por producto.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def main() -> None:
    """
    Función principal del programa.
    Se encarga de ejecutar la lógica principal.
    """
    # Leer los datos del archivo.csv
    car_data = pd.read_csv('data/vehicles_us.csv')
    st.header('Lanzar una moneda')
    st.write('Esta aplicación aún no es funcional. En construcción.')
    # Crear un botón en la aplicación Streamlit
    hist_button = st.button('Construir histograma')
    scatter_button = st.button('Construir gráifca de dispersión')
    
    # Lógica a ejecutar cuando se hace clic en el botón
    if hist_button:
        # Escribir un mensaje en la aplicación
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

        # Crear un histograma utilizando plotly.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

        # Opcional: Puedes añadir un título al gráfico si lo deseas
        fig.update_layout(title_text='Distribución del Odómetro')

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)
     
    # Lógica a ejecutar cuando se hace clic en el botón
    if scatter_button:
        # Escribir un mensaje en la aplicación
        st.write('Creación de una gráfica de dispersión para comparar kilometraje contra precio')
        # Crear un scatter plot utilizando plotly.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de scatter
        fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

        # Opcional: Puedes añadir un título al gráfico si lo deseas
        fig.update_layout(title_text='Relación entre Odómetro y Precio')

        # Mostrar el gráfico Plotly
        fig.show()

# Punto de entrada del script
if __name__ == "__main__":
    main()