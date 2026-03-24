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
    st.header('¡Autos! Autos!!')
    st.write('Se tiene un conjunto de datos sobre ventas de autos, el precio junto con características del vehículo.')
    st.write('Exploremos características interesantes.')
    # st state
    if "hist_button" not in st.session_state:
        st.session_state.hist_button = False
    if "scatter_button" not in st.session_state:
        st.session_state.scatter_button = False
    if "miles_chechbox" not in st.session_state:
        st.session_state.miles_checkbox = False
    # Botones
    if st.button("Construir histograma"):
        st.session_state.hist_button = True

    if st.button("Construir gráfica de dispersión"):
        st.session_state.scatter_button = True

    if st.checkbox("¿mostrar autos con más de 100 000 millas?"):
        st.session_state.miles_checkbox = True

    col1, col2 = st.columns(2)

    with col1:  
    # Lógica a ejecutar cuando se hace clic en el botón
        if st.session_state.hist_button:
            # Escribir un mensaje en la aplicación
            st.write('Histograma de datos de odómetro')

            # Crear un histograma utilizando plotly.graph_objects
            # Se crea una figura vacía y luego se añade un rastro de histograma
            if st.session_state.miles_checkbox:
                fig1 = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
            else:
                fig1 = go.Figure(data=[go.Histogram(x=car_data[car_data['odometer'] < 100000.0]['odometer'])])
            fig1.update_layout(title_text='Distribución del Odómetro')
            st.plotly_chart(fig1, use_container_width=True)
#            st.session_state.hist_button = False

    with col2:      
        # Lógica a ejecutar cuando se hace clic en el botón
        if st.session_state.scatter_button:
            # Escribir un mensaje en la aplicación
            st.write('Gráfica de dispersión kilometraje contra precio')
            # Crear un scatter plot utilizando plotly.graph_objects
            if st.session_state.miles_checkbox:
                fig2 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
            else:
                fig2 = go.Figure(data=[go.Scatter(x=car_data[car_data['odometer'] < 100000.0]['odometer'], y=car_data[car_data['odometer'] < 100000.0]['price'], mode='markers')])
            fig2.update_layout(title_text='Relación entre Odómetro y Precio')
            st.plotly_chart(fig2, use_container_width=True)

# Punto de entrada del script
if __name__ == "__main__":
    main()