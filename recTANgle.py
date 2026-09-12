import pygame
pygame.init()

win = pygame.display.set_mode((400, 400))
win.fill((0, 100, 0))
green = ((144, 238, 144))
pygame.draw.rect(win, green, (300, 300, 50, 50))
pygame.display.update()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()