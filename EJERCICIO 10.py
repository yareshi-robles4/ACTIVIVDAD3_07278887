print("Ejercicio 10: Tu playlist en el camion")
print("Nombre: Yareshi Guadalupe Robles Torres")
print("Matricula: 07278887")
print()

# Nuestra playlist
playlit = ["Flowers", "Calm Down", "Ella Baila Sola", "Anti-Hero", "Titi Me Pregunto", "Daylight"]

# Mostramos la playlist numerada
print("===== 🎧 MI PLAYLIST =====")
numero = 1
class playlist:
    ...

for cancion in playlist:
    print(numero, ".", cancion)
    numero = numero + 1

# Preguntamos que saltar y donde bajarse (escribelas igual que en la lista)
saltar = input("¿Que cancion quieres saltar? ")
parada = input("¿En que cancion llegas a tu parada? ")

# "Para cada" cancion de la playlist...
for cancion in playlit:

    # ¿Es la cancion que queremos saltar?
    if cancion == saltar:
        print("⏭️ Saltando", cancion)
        # continue: pasa a la siguiente cancion sin escuchar esta continue

    # Si no la saltamos, la escuchamos
    print("🎵 Escuchando", cancion)
    escuchadas = escuchadas + 1