import pandas as pd
import os

print("🔍 Analizando el dataset grande...")
file_size = os.path.getsize('vehicles_us.csv') / (1024 * 1024 * 1024)  # Tamaño en GB
print(f"📁 Tamaño del archivo original: {file_size:.2f} GB")

# Leer solo las primeras filas para análisis
print("📊 Leyendo primeras filas para análisis...")
df_sample = pd.read_csv('vehicles_us.csv', nrows=1000)
print(f"📋 Columnas disponibles: {list(df_sample.columns)}")
print(f"📏 Número de columnas: {len(df_sample.columns)}")

# Si el archivo es muy grande, crear una muestra
print("🔄 Creando muestra del dataset...")

# Método 1: Leer todo y muestrear (para archivos que caben en memoria)
try:
    df_full = pd.read_csv('vehicles_us.csv')
    sample_size = min(50000, len(df_full))  # Máximo 50,000 filas
    df_sample = df_full.sample(n=sample_size, random_state=42)
    print(f"✅ Muestra creada: {len(df_sample)} filas de {len(df_full)} totales")
    
except MemoryError:
    # Método 2: Para archivos muy grandes, leer por chunks
    print("⚠️  Archivo muy grande, usando lectura por chunks...")
    chunk_size = 10000
    chunks = []
    total_rows = 0
    
    for chunk in pd.read_csv('vehicles_us.csv', chunksize=chunk_size):
        chunks.append(chunk)
        total_rows += len(chunk)
        if total_rows >= 50000:
            break
    
    df_sample = pd.concat(chunks, ignore_index=True)
    print(f"✅ Muestra creada por chunks: {len(df_sample)} filas")

# Guardar la muestra
df_sample.to_csv('vehicles_us_sample.csv', index=False)
print("💾 Muestra guardada como 'vehicles_us_sample.csv'")

# Información sobre la muestra
print("\n📊 Información de la muestra:")
print(f"   - Filas: {len(df_sample)}")
print(f"   - Columnas: {len(df_sample.columns)}")
print(f"   - Tamaño estimado: {len(df_sample) * len(df_sample.columns) * 8 / (1024 * 1024):.2f} MB")