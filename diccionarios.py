from collections import Counter

print("\nCambiar la ciudad a 'Barcelona'.")
data = {"name": "Alice", "age": 30, "city": "Madrid"}

data["city"] = "Barcelona"

print(data)

print('\nVerificar si la clave "country" está en el diccionario; si no está, agrégala con el valor "Spain".')

data = {"name": "Alice", "age": 30, "city": "Barcelona"}

# Agregar "country" con el valor "Spain" si no existe
#data.setdefault("country", "Spain")
if "country" not in data:
    data["country"] = "Spain"
print(data)




print("\nObtener todas las claves y valores en formato de lista.")

keys_list = list(data.keys())
print(keys_list)

values_list = list(data.values())
print(values_list)
items_list = list(data.items())
print(items_list)


print('\nDado el texto text = "data engineering is amazing", cuenta cuántas veces aparece cada letra y almacena el resultado en un diccionario.')

text = "data engineering is amazing"
letter_count = {}
letter_count_counter = {}
for letter in text:
    if letter != " ":
        letter_count[letter] = letter_count.get(letter, 0) +1

print(letter_count)

letter_count_counter = Counter(text.replace(" ", ""))

print(letter_count_counter)

print("\nFiltra solo los productos cuyo precio sea menor a 100.")

products = {"Laptop": 800, "Mouse": 25, "Keyboard": 50, "Monitor": 200}

filtered_products =  {product: price for product,price in products.items() if price < 100}

print(filtered_products)