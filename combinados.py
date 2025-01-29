print("Dada la lista de nombres, crea un diccionario que cuente cuántas veces aparece cada nombre.")

names = ["Alice", "Bob", "Charlie", "Alice", "Diana", "Bob", "Alice"]
name_count = {}

for name in names:
    name_count[name] = name_count.get(name, 0) + 1


print(name_count)


print("\nDado un diccionario, crea un nuevo diccionario que contenga los promedios de cada estudiante.")

scores = {"Alice": [90, 85, 88], "Bob": [70, 80, 75], "Charlie": [95, 90, 92]}

average_scores = {student: sum(grades) / len(grades) for student, grades in scores.items()}

print(average_scores)


print("\nDados dos listas, combina las listas en un diccionario.")
keys = ["name", "age", "city"]
values = ["Alice", 30, "Madrid"]


combined_dict = dict(zip(keys,values))

print(combined_dict)


print("\nDada una lista de tuplas que representan productos:Por precio de menor a mayor. Por nombre alfabéticamente.")

products = [("Laptop", 800), ("Mouse", 25), ("Monitor", 150), ("Keyboard", 50)]

sorted_by_price = sorted(products, key=lambda x: x[1])

print("Ordenado por precio:", sorted_by_price)
sorted_by_name = sorted(products, key=lambda x: x[0])

print("Ordenado por nombre:", sorted_by_name)