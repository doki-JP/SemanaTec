"""
Cañón, impactando objetivos con proyectiles.

Ejercicios:

1. Llevar la cuenta de los impactos en los objetivos.
2. Variar el efecto de la gravedad.
3. Aplicar gravedad a los objetivos.
4. Cambiar la velocidad de la bola.
"""

from random import randrange
from turtle import (
    Screen, clear, goto, dot, update, ontimer, setup,
    hideturtle, up, tracer, onscreenclick, done
)
from freegames import vector

# Posición inicial de la bola y su velocidad
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Responde al clic en la pantalla.

    Si la bola está fuera de la pantalla, reinicia la posición
    y ajusta la velocidad en función del clic.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Devuelve True si xy está dentro de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja la bola y los objetivos en la pantalla."""
    clear()

    # Dibuja cada objetivo como un punto azul
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Dibuja la bola como un punto rojo si está en la pantalla
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Mueve la bola y los objetivos en la pantalla."""
    # Agrega un nuevo objetivo en una posición aleatoria
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Mueve los objetivos hacia la izquierda
    for target in targets:
        target.x -= 0.5

    # Aplica la gravedad a la bola si está dentro de la pantalla
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Elimina objetivos que han sido impactados
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Si algún objetivo está fuera de la pantalla, termina el juego
    for target in targets:
        if not inside(target):
            return

    # Programa la siguiente actualización del movimiento
    ontimer(move, 50)


# Configuración de la pantalla
screen = Screen()
screen.setup(width=420, height=420, startx=370, starty=0)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
