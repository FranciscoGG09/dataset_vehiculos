# 🚗 Análisis Exploratorio de Datos (EDA) - Dataset de Vehículos

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-313131?style=flat&logo=matplotlib&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-34A853?style=flat&logo=seaborn&logoColor=white" alt="Seaborn">
</p>

Este repositorio contiene un **Análisis Exploratorio de Datos (EDA)** completo realizado sobre un conjunto de datos de vehículos (probablemente de segunda mano). El objetivo principal es limpiar, analizar y visualizar los datos para descubrir patrones, tendencias y correlaciones que puedan afectar el precio o las características de los vehículos.

## 🎯 Objetivos del Análisis

El análisis se centra en responder preguntas clave como:
* ¿Cómo se distribuyen los precios de los vehículos?
* ¿Cuáles son las marcas y modelos más comunes en el dataset?
* ¿Cómo afecta el año de fabricación y el kilometraje al precio?
* ¿Qué correlación existe entre las diferentes características (motor, año, kilometraje, precio)?
* ¿Existen valores atípicos (outliers) que deban ser tratados?

## 📊 Proceso de Análisis

El proyecto sigue una metodología estándar de análisis de datos:

1.  **Carga y Limpieza de Datos (Data Cleaning):**
    * Importación del dataset (ej. `.csv` o `.json`).
    * Manejo de valores nulos (NaN).
    * Corrección de tipos de datos (ej. convertir 'precio' a numérico).
    * Eliminación de duplicados.

2.  **Análisis Exploratorio de Datos (EDA):**
    * Análisis estadístico descriptivo (medias, medianas, percentiles).
    * Identificación de la distribución de variables clave (ej. histogramas de precio).
    * Análisis de correlación entre variables (usando mapas de calor).

3.  **Visualización de Datos (Data Visualization):**
    * Creación de gráficos (boxplots, scatter plots, bar charts) para ilustrar los hallazgos.
    * Identificación de tendencias entre el precio y otras características.

4.  **Conclusiones y Hallazgos:**
    * Resumen de los *insights* más importantes descubiertos durante el análisis.

## 🛠️ Stack Tecnológico

* **Lenguaje:** **Python 3.x**
* **Entorno:** **Jupyter Notebook** (o Jupyter Lab)
* **Librerías de Análisis:** **Pandas** y **NumPy**
* **Librerías de Visualización:** **Matplotlib** y **Seaborn**

## 🚀 Cómo Empezar

Para ejecutar este análisis en tu máquina local, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/FranciscoGG09/dataset_vehiculos.git](https://github.com/FranciscoGG09/dataset_vehiculos.git)
    cd dataset_vehiculos
    ```

2.  **(Recomendado) Crear un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**
    <p>Asegúrate de tener instaladas las librerías principales:</p>
    <pre><code>pip install pandas numpy matplotlib seaborn jupyter</code></pre>


4.  **Iniciar Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    *Abre el archivo `.ipynb` principal (ej. `analisis_vehiculos.ipynb`) y ejecuta las celdas.*

## 👨‍💻 Autor

Desarrollado por **Francisco González**.

* **LinkedIn:** [linkedin.com/in/francisco-gonzalez](https://linkedin.com/in/francisco-gonzalez)
* **GitHub:** [@FranciscoGG09](https://github.com/FranciscoGG09)
