import pygame as pg

pg.init()

SCR_W = 800
SCR_H = 600

screen = pg.display.set_mode((SCR_W, SCR_H))
pg.display.set_caption("Pong")

clock = pg.time.Clock()
running = True

lPaddle = pg.Rect(15, (SCR_H / 2) - 50, 20, 100)
rPaddle = pg.Rect(SCR_W - 35, (SCR_H / 2) - 50, 20, 100)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    keys = pg.key.get_pressed()

    if keys[pg.K_w] and lPaddle.y > 0:
        lPaddle.y -= 5
    if keys[pg.K_s] and lPaddle.y + lPaddle.height < SCR_H:
        lPaddle.y += 5

    if keys[pg.K_UP] and rPaddle.y > 0:
            rPaddle.y -= 5
    if keys[pg.K_DOWN] and rPaddle.y + rPaddle.height < SCR_H:
            rPaddle.y += 5

    pg.display.flip()

    screen.fill("gray")

    pg.draw.rect(screen, (24, 46, 111), lPaddle)
    pg.draw.rect(screen, (100, 0, 0), rPaddle)

    clock.tick(60)
pg.quit()
