# Imports
import pygame as pg

# Init pygame
pg.init()

# Constants and variables
SCR_W = 800
SCR_H = 600

screen = pg.display.set_mode((SCR_W, SCR_H))
pg.display.set_caption("Pong")

clock = pg.time.Clock()
running = True

lPaddle = pg.Rect(15, (SCR_H / 2) - 50, 20, 100)
lPaddleColor = (144,213,255)

rPaddle = pg.Rect(SCR_W - 35, (SCR_H / 2) - 50, 20, 100)
rPaddleColor = (255, 71, 77)

# Game loop
while running:
    # Handle quitting the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # Input for both paddles
    keys = pg.key.get_pressed()

    if keys[pg.K_w] and lPaddle.y > 0:
        lPaddle.y -= 5
    if keys[pg.K_s] and lPaddle.y + lPaddle.height < SCR_H:
        lPaddle.y += 5

    if keys[pg.K_UP] and rPaddle.y > 0:
        rPaddle.y -= 5
    if keys[pg.K_DOWN] and rPaddle.y + rPaddle.height < SCR_H:
        rPaddle.y += 5

    # Update the screen
    pg.display.flip()

    # Clean the background
    screen.fill("black")

    # Draw both paddles
    pg.draw.rect(screen, lPaddleColor, lPaddle)
    pg.draw.rect(screen, rPaddleColor, rPaddle)

    # Lock fps to 60
    clock.tick(60)
# Exit game
pg.quit()
