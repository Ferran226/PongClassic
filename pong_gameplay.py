import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

# Puntuación
puntuacion_izquierda = 0
puntuacion_derecha = 0

# Configuracion del marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador Naranja: {}   Jugador Azul: {}".format(puntuacion_izquierda, puntuacion_derecha),
                align="center", font=("Courier", 24, "normal"))

# Paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("orange")
paleta_izquierda.shapesize(stretch_wid=6, stretch_len=2)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("blue")
paleta_derecha.shapesize(stretch_wid=6, stretch_len=2)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 5  # Velocidad en la dirección horizontal
pelota.dy = -5  # Velocidad en la dirección vertical


# Funciones para mover las paletas
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    y += 20
    paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    y -= 20
    paleta_izquierda.sety(y)

def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    y += 20
    paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    y -= 20
    paleta_derecha.sety(y)

# Función para actualizar el marcador
def actualizar_marcador():
    marcador.clear()   # Desactivar la actualización automática de la ventana
    marcador.color("white")  # Cambiamos el color del texto a blanco
    marcador.penup()
    marcador.goto(0,260)
    marcador.write("Jugador Naranja: {}   Jugador Azul: {}".format(puntuacion_izquierda, puntuacion_derecha),
                align="center", font=("Courier", 24, "normal"))
    
    ventana.update()  # Forzar la actualización de la pantalla
    

# Función para establecer la velocidad de la pelota
def establecer_velocidad():
    global pelota
    velocidad = turtle.textinput("Velocidad de la pelota", "Elige una velocidad (1-5):")
    try:
        velocidad = int(velocidad)
        if 1 <= velocidad <= 5:
            pelota.dx = velocidad 
            pelota.dy = -velocidad
        else:
            print("Por favor, elige un número entre 1 y 5.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Función para reiniciar el juego
def reiniciar_juego():
    global puntuacion_izquierda, puntuacion_derecha
    puntuacion_izquierda = 0
    puntuacion_derecha = 0
    pelota.goto(0, 0)
    establecer_velocidad()

# Llamada a la función para establecer la velocidad
establecer_velocidad()

# Asignación de teclas
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")

# Bucle principal del juego
while True:
    ventana.update()   # Actualizar pantalla solo cuando sea necesario

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebote en las paredes verticales
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1

    # Rebote en las paletas
    if (pelota.dx > 0) and (340 < pelota.xcor() < 350) and (paleta_derecha.ycor() + 50 > pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.color("blue") # Opcional: cambiar de color al colisionar
        pelota.dx *= -1

    elif (pelota.dx < 0) and (-350 > pelota.xcor() > -360) and (paleta_izquierda.ycor() + 50 > pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.color("orange")  # Opcional: cambiar de color al colisionar
        pelota.dx *= -1

    # Verificacion de la puntuación
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntuacion_izquierda += 1

    elif pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntuacion_derecha += 1

    # Límites superiores e inferiores de las paletas
    if paleta_izquierda.ycor() > 250:
        paleta_izquierda.sety(250)

    if paleta_izquierda.ycor() < -250:
        paleta_izquierda.sety(-250)

    if paleta_derecha.ycor() > 250:
        paleta_derecha.sety(250)

    if paleta_derecha.ycor() < -250:
        paleta_derecha.sety(-250)

    # Actualización de la puntuación en la ventana
    # (código de actualización de puntuación en la ventana)
    actualizar_marcador()

    # Verificación de la condición de victoria
    puntuacion_para_ganar = 5  # Puntuación deseada para ganar
    if puntuacion_izquierda == puntuacion_para_ganar:
        jugar_nueva_partida = turtle.textinput("¡Jugador naranja gana!", "¿Quieres jugar una nueva partida? (s/n):")
        if jugar_nueva_partida.lower() == "n":
            salir_juego = ventana.textinput("Salir", "¿Estás seguro de que deseas salir? (s/n):")
            if salir_juego.lower() == "s":
                break # Salir del bucle principal y cerrar el juego
        elif jugar_nueva_partida.lower() == "s":
            reiniciar_juego() # Reiniciar el juego
    elif puntuacion_derecha == puntuacion_para_ganar:
        jugar_nueva_partida = turtle.textinput("¡Jugador azul gana!", "¿Quieres jugar una nueva partida? (s/n):")
        if jugar_nueva_partida.lower() == "n":
            salir_juego = ventana.textinput("Salir", "¿Estás seguro de que deseas salir? (s/n):")
            if salir_juego.lower() == "s":
                break # Salir del bucle principal y cerrar el juego
        elif jugar_nueva_partida.lower() == "s":
            reiniciar_juego() # Reiniciar el juego



