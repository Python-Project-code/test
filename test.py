
## 1 Manejo de datos

data = {"Alice": 90, "Bob": 85, "Charlie": 95, "Diana": 80}

print(data)

# Convertir a lista de tuplas y ordenar por el segundo elemento en orden descendente
res = sorted(data.items(), key=lambda x: x[1], reverse = True)

print(res)