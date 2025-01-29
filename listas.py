nums = [10,20,30,40,50]

print("Obtener los tres últimos elementos.")

def last3(nums):
    return nums[-3:]

print(last3(nums))

print("Insertar el número 25 entre 20 y 30.")
   
nums.insert(2,25)
print(nums)
 
print("Eliminar el número 40.")
   
nums.remove(40)
print(nums)

print("Revertir el orden de la lista.")
nums.reverse()
print(nums)

print("Combina las listas list1 y list2  en una sola lista. Después, elimina los números que sean mayores a 4.")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def combined (l1,l2):
    return sorted(l1+l2)

combined_list = combined(list1,list2)
print(combined_list)
filtered_list = [x for x in combined_list if x <=4]
print(filtered_list)

print("Dada la lista, elimina los números duplicados manteniendo el orden original.")

nums = [1, 2, 2, 3, 4, 4, 5]

seen = set()

unique_nums = [x for x in nums if not (x in seen or seen.add(x))]

print(unique_nums)