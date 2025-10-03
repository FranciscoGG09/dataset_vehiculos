# 🚗 Panel de Control de Análisis de Vehículos

## 📊 Descripción
Aplicación web interactiva para análisis exploratorio de datos de vehículos usados, utilizando el dataset de CarDekho. Construida con Streamlit y Plotly.

## 🌐 Aplicación Desplegada
**URL:** [https://vehicle-analysis-dashboard.onrender.com](https://vehicle-analysis-dashboard.onrender.com)

## 🛠️ Tecnologías Utilizadas
- **Frontend:** Streamlit
- **Visualizaciones:** Plotly Express
- **Procesamiento de datos:** Pandas
- **Despliegue:** Render

## 📈 Funcionalidades
- Visualización de datos raw
- Histogramas interactivos
- Gráficos de dispersión
- Gráficos de barras categóricos
- Estadísticas descriptivas
- Filtrado interactivo de datos

## 🗃️ Dataset
- **Fuente:** [CarDekho Dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)
- **Registros:** ~5,000 vehículos
- **Características:** precio, año, fabricante, modelo, combustible, transmisión, etc.

## 🚀 Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/FranciscoGG09/dataset_vehicles.git
cd dataset_vehicles

# Crear entorno virtual
python -m venv vehicles_env

# Activar entorno virtual (Windows)
vehicles_env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run app.py
# dataset_vehicles
Las tareas incluyen la creación y gestión de entornos virtuales de Python y el desarrollo de una aplicación web.
