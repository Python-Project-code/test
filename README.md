# Preguntas tipo para pruebas técnicas 


1. [Manejo de datos](#schema1)
2. [Funciones](#schema2)
3. [Listas y Diccionarios](#schema3)
4. [Uso de Pandas](#schema4)
5. [Lectura de datos](#schema5)
6. [Transformación de DataFrames](#schema6)
7. [Consultas con SQL](#schema7)
8. [Uso de funciones map() y filter()](#schema8)
9. [Agregaciones](#schema9)
10. [Manejo de Listas](#schema10)
11. [Manejo de Diccionarios](#schema11)
12. [Manejo de Cadenas](#schema12)
13. [Conjuntos](#schema13)


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


# PySpark

<hr>
<a name='schema5'></a>

## 5 Lectura de datos
- Escribe un código para leer un archivo CSV con PySpark y mostrar las primeras 5 filas. El archivo se llama `data.csv`.


<hr>
<a name='schema6'></a>

## 6 Transformación de DataFrames
- Dado un DataFrame con información de ventas, agrega una nueva columna que calcule el total multiplicando la cantidad por el precio unitario.

<hr>
<a name='schema7'></a>

## 7 Consultas con SQL
- Registra el DataFrame anterior como una tabla SQL y escribe una consulta para obtener los productos cuyo precio total (cantidad * precio unitario) sea mayor a 20.


<hr>
<a name='schema8'></a>

## 8 Uso de funciones map() y filter()

- Usa `rdd.map()` para convertir una lista de tuplas de (producto, cantidad) en (producto, "Alto") si la cantidad es mayor a 5 o (producto, "Bajo") en caso contrario.

```python
data = [("Apple", 5), ("Banana", 10), ("Orange", 3)]
```
- Usa `rdd.filter()` para quedarte solo con los productos que tienen una cantidad mayor a 5.



<hr>
<a name='schema9'></a>


## 9 Agregaciones

- Dado un DataFrame de ventas, calcula el total de ventas por producto utilizando `groupBy` y `agg`.

```python

data = [("Apple", 5), ("Banana", 10), ("Orange", 8), ("Apple", 3)]
columns = ["Product", "Quantity"]
df = spark.createDataFrame(data, columns)
```
- Usando RDD, calcula el promedio de cantidad por producto en una lista de tuplas.

<hr>
<a name='schema10'></a>

## 10 Manejo de Listas

1. Acceso y Manipulación:

- Dada la lista nums = [10, 20, 30, 40, 50], escribe un código para:
    - Obtener los tres últimos elementos.
    - Insertar el número 25 entre 20 y 30.
    - Eliminar el número 40.
    - Revertir el orden de la lista.

2. Combinación de Listas:

- Combina las listas list1 = [1, 2, 3] y list2 = [4, 5, 6] en una sola lista. Después, elimina los números que sean mayores a 4.

3. Eliminación de Duplicados:

- Dada la lista nums = [1, 2, 2, 3, 4, 4, 5], elimina los números duplicados manteniendo el orden original.




<hr>
<a name='schema11'></a>

## 11 Manejo de Diccionarios
1. Búsqueda y Actualización:
    - Dado el diccionario, escribe un código para:
        ``` python
            data = {"name": "Alice", "age": 30, "city": "Madrid"}
        ```
        - Cambiar la ciudad a "Barcelona".
        - Verificar si la clave "country" está en el diccionario; si no está, agrégala con el valor "Spain".
        - Obtener todas las claves y valores en formato de lista.
3. Conteo de Elementos:
    - Dado el texto text = "data engineering is amazing", cuenta cuántas veces aparece cada letra y almacena el resultado en un diccionario.

4. Filtrar un Diccionario:
    - Dado el diccionario:
        ```python
            products = {"Laptop": 800, "Mouse": 25, "Keyboard": 50, "Monitor": 200}
        ```
        - Filtra solo los productos cuyo precio sea menor a 100.

<hr>
<a name='schema12'></a>


## 12 Manejo de Cadenas
1. Manipulación Básica:
    - Dada la cadena text = "Python is Fun!", realiza las siguientes operaciones:
        - Convierte todo el texto a minúsculas.
        - Reemplaza "Fun" por "Amazing".
        - Invierte la cadena.
2. Extracción de Información:
    - Dada la cadena email = "user@example.com", extrae el nombre de usuario (antes de @) y el dominio (después de @).


<hr>
<a name='schema13'></a>

## 13 Manejo de Conjutos

1. Operaciones Básicas:
- Dados los conjuntos:
    ```python
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
    ```
    - Realiza las siguientes operaciones:
        - Encuentra la intersección de ambos conjuntos.
        - Obtén los elementos únicos que están solo en set1.
        - Une ambos conjuntos.
2. Eliminación de Elementos:
- Dado el conjunto nums = {10, 20, 30, 40}, elimina el número 30 y agrega el número 50.
