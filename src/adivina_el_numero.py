
print("Bienvenido al juego ¡Adivina el Número!")
print("Piensa en un número entre 1 y 100.")

jugar = input("¿Deseas jugar? (si/no): ").lower()

if jugar == "si":
    print("¡Genial! Empecemos.")
else:
    print("¡Está bien! Nos vemos la próxima vez.")

while jugar == "si":

    minimo = 1
    maximo = 100
    intentos = 0

    while True:

        intento = (minimo + maximo) // 2
        intentos += 1

        respuesta = input(
            f"¿Tu número es {intento}? (mayor/menor/correcto): "
        ).lower()

        if respuesta == "correcto":
            print("¡He adivinado tu número!")
            print(f"Lo logré en {intentos} intentos.")
            break

        elif respuesta == "mayor":
            minimo = intento + 1

        elif respuesta == "menor":
            maximo = intento - 1

        else:
            print(
                "Respuesta no válida. "
                "Por favor responde con mayor, menor o correcto."
            )

    jugar = input(
        "\n¿Quieres jugar de nuevo? (si/no): "
    ).lower()

    if jugar == "si":
        print("¡Genial! Empecemos de nuevo.")

print("¡Gracias por jugar!")
