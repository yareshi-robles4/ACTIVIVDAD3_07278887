print("Ejercicio 7: Boletos para el concierto")
print("Nombre: Yareshi Guadalupe Robles Torres")
print("Matricula: 07278887")
print()

# Pedidos el artista y cuantos bolteos quiere
artista = input("¿De quien es el concierto")
cantidad = int(input("¿Cuantos boletos quieres? "))

# range(1, cantidad + 1): de 1 hasta cantidad
# (le sumamos 1 porque range se detiene ANTES del ultimo numero)
for boleto in range(1, cantidad + 1):
   # Pedimos el nombre de quien va a usar este boleto
   asistente = input("Nombre del asistente " + str(boleto) + ": ")

   #Mostramos el boleto 
   print("🎟️ Boleto", boleto, "de", cantidad)
   print("  🎤", artista, ". Asistente:", asistente)


# Esto se ejecuta cuando el for ya dio todas sus vueltas
print("✅ Se generaron", cantidad, "boletos. ¡Disfruten el concierto!")