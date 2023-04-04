import pygame 
pygame.init()
from locale import *
canvas = pygame.display.set_mode([600,400])
img = pygame.image.load('run.bmp')
canvas.fill((255,255,255))
r=1

def pp():
    x=0
    y=0
Clock = pygame.time.Clock()
while r:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = 0
    img = pygame.transform.rotate(img, 90) #旋转图片
    canvas.blit(img,[0,0])
    pygame.time.delay(100)
    pygame.display.update()
    Clock.tick(30)
    print(Clock.get_fps())
