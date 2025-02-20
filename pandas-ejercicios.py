import pandas as pd
import numpy as np

data = {
    "Fecha": ["2024-01-01", "2024/01/02", None, "2024-01-04"],
    "Producto": ["Laptop", "Mouse", "Teclado", np.nan],
    "Precio": [1000, 25, 50, 30],
    "Cantidad": [1, 2, np.nan, 3]
}

df = pd.DataFrame(data)


# 1. Normaliza la columna "Fecha" al formato YYYY-MM-DD.

df["Fecha"] = df["Fecha"].str.replace("/", "-", regex=False)
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce", format="%Y-%m-%d")

# 2. Llena los valores nulos de la columna "Cantidad" con la mediana.

df["Cantidad"].fillna(df["Cantidad"].median(), inplace=True)

# 3. Reemplaza valores nulos en "Producto" con "Desconocido".
df["Producto"].fillna("Desconocido", inplace=True)

# 4. Crea una nueva columna "Total" multiplicando "Precio" * "Cantidad".
df["Total"] = df["Precio"] * df["Cantidad"]


print(df)