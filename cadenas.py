print('Dada la cadena text = "Python is Fun!", realiza las siguientes operaciones:')
print("Convierte todo el texto a minúsculas.")
text = "Python is Fun!"

lower_text = text.lower()
print(lower_text)



print('\nReemplaza "Fun" por "Amazing".')
updated_text = text.replace("Fun", "Amazing")

print(updated_text)

print("\nInvierte la cadena.")

reversed_text = text[::-1]

print(reversed_text)

print('\nDada la cadena email = "user@example.com", extrae el nombre de usuario (antes de @) y el dominio (después de @).')
email = "user@example.com"

username, domain = email.split("@")

print("Username", username)
print("Domain",domain)