print("Ejercicio 8: Revisa tu gamertag")
print("Nombre: Yareshi Guadalupe Robles Torres")
print("Matricula: 07278887")
print()

# Pedimos el gamertag
gamertag = input("Escribe tu gamertag: ")

# Contadores: empiezan en 0
vocales = 0
numeros= 0
caracteres = 0

# "Parra cada" letra del gamertag...
for letra in gamertag:
    print("🔤", letra)

    # Contamos este caracter
    caracteres = caracteres + 1

    #¿La letra ESTA en el grupo de vocales?
    if letra in "aeiouAEIOU":
        vocales = vocales + 1

    #¿La letra ESTA en el grupo de numeros?
    if letra in "0123456789":
        numeros = numeros + 1

# Ya revisamos todas las letras: mostramos el resumen
print("===== RESUMEN =====")
print("Caracteres:", caracteres)
print("Vocales:", vocales)
print("Numeros:", numeros)

# ¿No tiene ningun numero?
if numeros == 0:
    print("💡 Consejo: agregale un numero para que sea unico")
else:
    print("✅ ¡Buen gamertag!")