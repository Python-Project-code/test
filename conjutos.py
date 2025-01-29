
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Encuentra la intersección de ambos conjuntos.")

intersection = set1 & set2
print(intersection)

print("\nObtén los elementos únicos que están solo en set1.")

unique_set1 = set1 - set2
print(unique_set1)
print("\nUne ambos conjuntos.")

union = set1 | set2
print(union)
print("\nDado el conjunto nums = {10, 20, 30, 40}, elimina el número 30 y agrega el número 50.")

nums = {10, 20, 30, 40}
nums.remove(30)
nums.add(50)
print(nums)