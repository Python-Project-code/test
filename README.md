# Preguntas tipo para pruebas técnicas 


1. [Manejo de datos](#schema1)
2. [Funciones](#schema2)
3. [Listas y Diccionarios](#schema3)
4. [Uso de Pandas](#schema4)



8. [Resources](#schemaref)


# Python

<hr>
<a name='schema1'></a>

## 1 Manejo de datos

1.  Dado el siguiente diccionario de datos, convierte los datos en una lista de tuplas y ordénalas por el segundo elemento de cada tupla en orden descendente.
    - `data.items()`: Convierte el diccionario en una lista de tuplas
```python
data = {"Alice": 90, "Bob": 85, "Charlie": 95, "Diana": 80}
```

2. Escribe una función que reciba una lista de números y devuelva una nueva lista con solo los números pares mayores que 10.

```python
nums = [4, 12, 9, 18, 7, 20]
```


<hr>
<a name='schema2'></a>

## 2 Funciones


- Crea una función que reciba una lista de cadenas y devuelva un diccionario donde las claves sean las cadenas y los valores la longitud de cada una.

```python
words = ["data", "engineering", "python", "spark"]
```

<hr>
<a name='schema3'></a>


## 3 Listas y Diccionarios
- Dado un diccionario que contiene productos y sus precios, filtra los productos con precios mayores a 50 y ordénalos alfabéticamente por nombre.

```python
products = {"Laptop": 800, "Mouse": 25, "Keyboard": 45, "Monitor": 150}
```
- Usa una comprensión de listas para encontrar los cuadrados de los números impares en una lista.

```python
nums = [1, 2, 3, 4, 5, 6, 7]
```

<hr>
<a name='schema4'></a>

## 4. Uso de Pandas

- Dado el siguiente DataFrame, calcula el promedio de edad por género.

```python
import pandas as pd
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "Gender": ["F", "M", "M", "F"]
})
```
- Escribe un código para eliminar duplicados en un DataFrame y contar cuántos registros únicos quedan.