print("Ejercicio 3: Desbloquea tu celular")
print("Nombre: Escribe aqui tu nombre completo")
print("Matricula: Escribe aqui tu matricula")
print()

# 1. Guardamos el PIN correcto
pin_correcto = "2580"

# 2. Empezamos con 0 intentos 
intentos = 0

# 3. Mientras lleve menos de 3 intentos, se repita
while intentos < 3:
    pin = input("🔐 Escribe tu PIN de 4 numeros")

    # ¿El PIN es IGUAL al correcto?
    if pin == pin_correcto:
        print("🔓 Celular desbloqueado")
        # Ya entro: break lo saca del while 
        break
    else:
        # Se equivoco: sumamos 1 intento
        intentos = intentos + 1
        # Calculamos cuantos intentos le quedan
        restantes = 3 - intentos
        print("❌ PIN incorrecto. Te quedan", restantes, "intentos")

    # 4. Ya fuera del while: ¿se acabaron los intentos?
    if intentos == 3:
        print("🔐 Celular bloqueado por 30 segundos")
        print("💡 Pista: son los numeros de la columna del centro")
else:
    # Si lo desbloqueo
    print("📱 Tienes 3 notificaciones nuevas")

    # 5. Preguntamos si quiere cambiar el PIN
    cambiar = input("¿Quieres cambiar tu PIN? (s/n): ")

    if cambiar == "S":
         # A l inicio los dos PIN todavia NO coinciden
         coinciden = False

        
        # Mientras NO coincidan, se repita
    while coinciden == False:
           nuevo = input("Escribe tu nuevo PIN: ")
           confirmacion = input("Vuelve a escribirlo para confirmar: ")

           # ¿Los dos son IGUALES?
           if nuevo == confirmacion:
                print("✅ Tu PIN se cambio correctamente")
                coinciden = True
           else:
                print("❌ No coinciden, intenta otra vez")
    else:
         print("👍🏽 Tu PIN  se queda igual")
         