import pygame
pygame.init()

win = pygame.display.set_mode((400, 400))
win.fill((0, 0, 130))
blu = (135, 206, 235)
pygame.draw.circle(win, blu, (300, 300), 50)
pygame.draw.circle(win, blu, (100, 100), 50, 3)
pygame.display.update()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()