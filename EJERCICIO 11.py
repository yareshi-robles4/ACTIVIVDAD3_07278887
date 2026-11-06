print("Ejercicio 11: Buscador de la tienda de sneakers")
print("Nombre: Yareshi Guadalupe Robles Torres")
print("Matricula: 072788872")
print()

# El inventario de la tienda
inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

# Contadores
busquedas = 0
encontrados = 0

# El buscador se repite hasta que el cliente escriba "salir"
while True:
    print()
    buscando = input("🔍 ¿Que modelo buscas? (escribe salir para terminar): ")
    # ¿Escribio "salir"?
    if buscando == "salir":
        break

    # Contamos esta busqueda
    busquedas = busquedas + 1

    # "Para cada" modelo del inventario...
    for modelo in inventario:
        # ¿Este modelo es IGUAL al que busca?
        if modelo == buscando:
            print("✅ ¡Si tenemos", modelo, "!")
            encontrados = encontrados + 1
            # Ya lo encontramos: dejamos de buscar 
            break
   else: