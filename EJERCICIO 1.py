print("Ejercicio 1: Inicia sesion en Roblox")
print("Nombre: Escribe aqui tu nombre completo")
print("Matricula: Escribe aqui tu matricula")
print()

# Guardamos el usuario y la contrasena correctos 
usuario_correcto = "gamer17"
contrasena_correcta = False

#Al inicio todavia NO ha iniciado sesion 
sesion_iniciada = False

#Mientras NO haya iniciado sesion, se repita
while sesion_iniciada == False:
    # Pedimos el usuario y la contrasena
    usuario = input("Usuario: ")
    contrasena = input ("Contrasena: ")

# ¿El usuario es IGUAL al correcto?
if usuario == usuario_correcto:
    # Si existe. ahora: ¿la contrasena es IGUAL a la correcta?
    if contrasena == contrasena_correcta:
        print("✅ ¡Bienvenido,", usuario, "!")
        #Ya entro: esto hace que el while se detenga
        sesion_iniciada = True
    else:
        print("❌ La contraseña es incorrecta")
else:
    print("❌ Ese usuario no existe")

#Esto se ejecuta cuando ya salio del while 
print("🎮 Cargo tus juegos...")