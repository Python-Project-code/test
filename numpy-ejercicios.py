import numpy as np

# 1. Crea la matriz con valores entre 50 y 500.

np.random.seed(42)  # Para que el resultado sea reproducible
matriz = np.random.randint(50,501, size=(5,4))
print(matriz)

# 2. Calcula la media de cada columna.
media_columnas = np.mean(matriz,axis=0)
medias_filas = np.mean(matriz, axis=1)

print("\nMedia de cada columna:")
print(media_columnas)
print("\n Media de filas")
print(medias_filas)

# 3. Encuentra la región con la mayor venta promedio.

region_mayor_promedio = np.argmax(media_columnas)
print(f"\nRegión con mayor venta promedio: Región {region_mayor_promedio + 1}")

# 4. Aplica una normalización Min-Max a cada columna.

min_vals = np.min(matriz, axis=0)
max_vals = np.max(matriz, axis=0)
matriz_normalizada = (matriz - min_vals) / (max_vals - min_vals)

print("\nMatriz Normalizada (Min-Max):")
print(matriz_normalizada)
