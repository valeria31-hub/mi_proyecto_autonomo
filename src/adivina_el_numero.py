print("Bienvenido al juego ¡Adivina el Número!")
print("Piensa en un número entre 1 y 100.")

jugar = input("¿Deseas jugar? (si/no): ").lower()

if jugar == "si":
    print(";Genial! Empecemos.")
else:
    print("¡Está bien! Nos vemos la próxima vez.")

# Estructura repetitiva principal para controlar los reinicios del juego
while jugar == "si":
    
    # Configuración inicial de variables y límites del rango
    minimo = 1
    maximo = 100
    intentos = 0
    
    # Bucle interno para el proceso de adivinanza en la partida actual
    while True:
        # Algoritmo de búsqueda binaria: cálculo del punto medio exacto
        intento = (minimo + maximo) // 2
        intentos += 1
        
        respuesta = input(
            f"¿Tu número es {intento}? (mayor/menor/correcto): "
        ).lower()
        
        # Estructuras condicionales para evaluar la respuesta del usuario
        if respuesta == "correcto":
            print("¡He adivinado tu número!")
            print(f"Lo logré en {intentos} intentos.")
            break # Rompe el bucle de adivinanza porque ya ganó
            
        elif respuesta == "mayor":
            # Si el número del usuario es mayor, ajusta el límite inferior
            minimo = intento + 1
            
        elif respuesta == "menor":
            # Si el número del usuario es menor, ajusta el límite superior
            maximo = intento - 1
            
        else:
            print("Respuesta no válida.")
            print("Por favor responde con mayor, menor o correcto.")
            intentos -= 1 # No cuenta el intento si hubo un error

    # Pregunta de reinicio de juego (actualiza la condición del bucle principal)
    jugar = input("\n¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar == "si":
        print("¡Genial! Empecemos de nuevo.")

print("¡Gracias por jugar!")
