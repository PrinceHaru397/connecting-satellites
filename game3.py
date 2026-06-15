import pgzrun
import pgzero.screen
import random

# Window Size
WIDTH = 800
HEIGHT = 600

# Actor
player = Actor("satellite", (300, 200))
asteroid = Actor("asteroid", (100, 100))

# Variables
score = 0

# Draw Everything
def draw():
    screen.clear()
    screen.fill("black")
    player.draw()
    asteroid.draw()
    screen.draw.text("Score: " + str(score), (10, 10), color = "white")

# Keyboard Controls
def update():
    global score
    if player.colliderect(asteroid):
        asteroid.x = random.randint(50, 550)
        asteroid.y = random.randint(50, 550)
        score+=1

def on_mouse_move(pos):
    player.pos = pos

# Start
pgzrun.go()