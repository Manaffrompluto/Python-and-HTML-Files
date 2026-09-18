import pygame
import random
pygame.init()

sprcol = pygame.USEREVENT + 1
bgcol = pygame.USEREVENT + 2

r = pygame.Color('red')
o = pygame.Color('orange')
y = pygame.Color('yellow')
g = pygame.Color('lightgreen')

dg = pygame.Color('darkgreen')
b = pygame.Color('lightblue')
db = pygame.Color('darkblue')
p = pygame.Color('purple')

class Sprite(pygame.sprite.Sprite):

    def __init__(self, height, width, colour):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            hit = True
        if hit:
            pygame.event.post(pygame.event.Event(sprcol))
            pygame.event.post(pygame.event.Event(bgcol))

    def chcol(self):
        self.image.fill(random.choice([r, o, y, g]))

def chcol1():
    global cbg
    cbg = random.choice([dg, b, db, p])

all = pygame.sprite.Group()
sp = Sprite(20, 30, g)
sp.rect.x = random.randint(0, 480)
sp.rect.y = random.randint(0, 370)
all.add(sp)

scr = pygame.display.set_mode((500, 400))
pygame.display.set_caption("A Moving Sprite")
cbg = b
scr.fill(cbg)

exit = False
cl = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit = True

        elif event.type == sprcol:
            sp.chcol()

        elif event.type == pygame.USEREVENT + 2:
            chcol1()

    all.update()
    scr.fill(bgcol)
    all.draw(scr)

    pygame.display.flip()
    cl.tick(240)

pygame.quit()