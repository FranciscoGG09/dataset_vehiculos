import pandas as pd
import plotly.express as px
import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos - CarDekho", layout="wide")

# Título de la aplicación
st.title('🚗 Análisis de Vehículos Usados - Dataset CarDekho')
st.header('Exploración de Datos de Vehículos de la India')

# Cargar los datos
@st.cache_data
def load_data():
    if os.path.exists('vehicles_us.csv'):
        data = pd.read_csv('vehicles_us.csv')
        
        # Optimizar tipos de datos
        numeric_columns = ['price', 'year', 'odometer']
        for col in numeric_columns:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col], errors='coerce')
        
        return data
    else:
        st.error("❌ No se encontró el archivo 'vehicles_us.csv'")
        return pd.DataFrame()

car_data = load_data()

# Mostrar información del dataset
if not car_data.empty:
    st.sidebar.subheader('📊 Información del Dataset')
    st.sidebar.write(f"**Vehículos:** {len(car_data):,}")
    st.sidebar.write(f"**Fabricantes:** {car_data['manufacturer'].nunique()}")
    st.sidebar.write(f"**Años:** {car_data['year'].min()} - {car_data['year'].max()}")
    st.sidebar.write(f"**Precios:** ₹{car_data['price'].min():,} - ₹{car_data['price'].max():,}")

# Mostrar datos raw si el usuario lo desea
if st.checkbox('📋 Mostrar datos raw'):
    st.subheader('Datos Raw')
    st.write(car_data)

# Encontrar columnas numéricas automáticamente
numeric_columns = car_data.select_dtypes(include=['int64', 'float64']).columns.tolist()

if not car_data.empty and numeric_columns:
    st.subheader('📈 Análisis Visual de Datos')
    
    # Selección de tipo de gráfico
    plot_type = st.radio('Selecciona el tipo de gráfico:', 
                         ['Histograma', 'Gráfico de Dispersión', 'Gráfico de Barras'], 
                         horizontal=True)

    # Histograma
    if plot_type == 'Histograma':
        st.write('**Distribución de una variable numérica**')
        selected_column = st.selectbox('Selecciona la columna:', numeric_columns)
        
        if selected_column:
            fig = px.histogram(car_data, x=selected_column, 
                              title=f'Distribución de {selected_column}')
            st.plotly_chart(fig, use_container_width=True)

    # Gráfico de Dispersión
    elif plot_type == 'Gráfico de Dispersión':
        st.write('**Relación entre dos variables numéricas**')
        
        if len(numeric_columns) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                x_column = st.selectbox('Eje X:', numeric_columns)
            with col2:
                y_options = [col for col in numeric_columns if col != x_column]
                y_column = st.selectbox('Eje Y:', y_options)
            
            if x_column and y_column:
                fig = px.scatter(car_data, x=x_column, y=y_column,
                                title=f'{x_column} vs {y_column}')
                st.plotly_chart(fig, use_container_width=True)

    # Gráfico de Barras
    else:
        st.write('**Distribución por categorías**')
        categorical_columns = ['manufacturer', 'fuel', 'transmission', 'type', 'condition']
        available_categorical = [col for col in categorical_columns if col in car_data.columns]
        
        if available_categorical:
            selected_column = st.selectbox('Selecciona categoría:', available_categorical)
            
            if selected_column:
                value_counts = car_data[selected_column].value_counts().head(15)
                fig = px.bar(x=value_counts.index, y=value_counts.values,
                            title=f'Distribución de {selected_column}')
                fig.update_layout(xaxis_title=selected_column, yaxis_title='Cantidad')
                st.plotly_chart(fig, use_container_width=True)

# Información adicional sobre el dataset
if not car_data.empty:
    st.subheader('🔍 Información Adicional')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Fabricantes más comunes:**")
        top_manufacturers = car_data['manufacturer'].value_counts().head(5)
        for manufacturer, count in top_manufacturers.items():
            st.write(f"- {manufacturer}: {count:,} vehículos")
    
    with col2:
        st.write("**Tipos de combustible:**")
        fuel_counts = car_data['fuel'].value_counts()
        for fuel, count in fuel_counts.items():
            st.write(f"- {fuel}: {count:,} vehículos")

else:
    st.warning("No hay datos disponibles. Por favor, ejecuta el script de transformación primero.")