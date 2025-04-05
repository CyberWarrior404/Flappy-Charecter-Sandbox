import pygame,time
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode((1200,800))
catx=600
caty=100
cat=pygame.image.load("flappy_bird.png")

while caty <=800:
    screen.fill("white")
    screen.blit(cat,(catx, caty))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if i.type==pygame.KEYDOWN:
            if i.key==K_UP:
                caty-=10
            elif i.key==K_DOWN:
                caty+=10
            elif i.key==K_LEFT:
                catx-=10
            elif i.key==K_RIGHT:
                catx+=10
    caty +=2
    time.sleep(0.1)
print("GAME OVER")