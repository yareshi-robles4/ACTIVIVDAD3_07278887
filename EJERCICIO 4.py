print("Ejercicio 4: La caja registradora de la cafeteria")
print("Nombre: Yareshi Guadalupe Robles Torres")
print("Matricula: 07278887")
print()

#Empezamos con el total y los productos en 0
total = 0
productos = 0

#Al inicio todavia NO terminamos de registrar
termine = False

# Mientras NO hayamos terminado, se repite
while termine == False:
    print("===== Nuevo producto =====")
    nombre = input("Producto (escribe fin para cobrar): ")

    #¿Escribio "fin"?
    if nombre == "fin":
         termine = True
    else:
         # Pedimos el precio y la cantidad (los convertimos a numero)
         precio = int(input("Precio de " + nombre + ": $"))
         cantidad = int(input("¿Cuantos quiere? "))

         #Calculamos el subtotal de este producto
         subtotal = precio * cantidad

         #Calculamos el total y contamos los productos
         total = total + subtotal
         productos = productos + cantidad

         print("📝", cantidad, nombre, "= $", subtotal)
         print("💰llevas $", total)

# Ya fuera del while: mostramos el ticket
print()
print("=== TICKET ===")
print("Total de productos:", productos)
print("Total a pagar: $", total)

# ¿El total es de 200 o mas?
if total > 200:
     total = total - 200
     print("🎉 Descuento de $20 aplicado")
     print("Total con pagas $", total)

#Podiamos con cuantos para
pago = int(input("¿Con cuantos pagas? $"))

# Mientras el pago sea MENOR que el total, no alcanza
while pago < total:
     print("❌ No alcanza. Faltan $", total - pago)
     pago = int(input("¿Con cuanto pagas? $"))

# Ya alcanzo: calculamos el cambio
cambio = pago - total
print("✅ Pago recibido. Tu cambio es: $", cambio)
print("☕ ¡Gracias por tu compra!")

       