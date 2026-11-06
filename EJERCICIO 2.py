print("Ejercicio 2: Menu de la Cafeteria Cute")
print("Nombre: Escribe aqui tu nombre completo")
print("Matricula: Escribe aqui tu matricula")

#while True: el menu se repite siempre; la unica salida es el break 
while True:
    # Mostramos el menu
    print()
    print("===== ☕ CAFETERIA CUTE =====")
    print("1. Ver bebidas")
    print("2. Ver postres")
    print("3. Ver horario")
    print("4. Salir")

# Pedimos la opcion
opcion = input("Elige una opcion: ")

# Revisamos que opcion eligio
if opcion == "1":
    print("🧋 Frappe de cajeta ..... $65")
    print("🍵 Matcha latte ......... $70")
    print("🍓 Smoothie de fresa .... $55")
elif opcion == "2":
    print("🍪 Galleta red velvet .... $35")
    print("🧁 Cupcake de Oreo ....... $40")
    print("🍩 Dona glaseada ......... $30")
elif opcion == "3":
    print("⏱️ Lunes a viernes: 7:00 a 20:00")
    print("⏱️ Sabados: 9:00 a 14:00")
elif opcion == "4":
    print("👋🏼 ¡Gracias por visitarnos!")
    # El cliente eligio Salir: break nos saca del while
    breakpoint
else:
    print("❌ Opcion no valida, elige del 1 al 4") 
    