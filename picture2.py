import pygame
from pygame.draw import *

pygame.init()
FPS = 30

screen = pygame.display.set_mode((400, 400))
pygame.draw.rect(screen,(0, 238, 238, 255),(0,0,400,200))
pygame.draw.rect(screen,(154, 205, 50, 255),(0,200,400,200))
#дерево
pygame.draw.rect(screen,(115,0,0),(50,200,30,100))
pygame.draw.ellipse(screen,(0,255,0),(20,100,100,70))
pygame.draw.ellipse(screen,(0,255,0),(20,150,100,70))
pygame.draw.ellipse(screen,(0,255,0),(70,120,100,70))
pygame.draw.ellipse(screen,(0,255,0),(-10,120,100,70))
pygame.draw.ellipse(screen,(255,255,0),(300,0,100,100))
pygame.draw.ellipse(screen,(255,0,230),(100,120,10,10))
pygame.draw.ellipse(screen,(255,0,230),(50,110,10,10))
pygame.draw.ellipse(screen,(255,0,230),(90,180,10,10))
pygame.draw.ellipse(screen,(255,0,230),(100,200,10,10))

#дерево 3
pam=pygame.Surface((400,400))
pam.set_colorkey((0,0,0))
pygame.draw.rect(pam,(115,0,0),(50,200,30,100))
pygame.draw.ellipse(pam,(0,255,0),(20,100,100,70))
pygame.draw.ellipse(pam,(0,255,0),(20,150,100,70))
pygame.draw.ellipse(pam,(0,255,0),(70,120,100,70))
pygame.draw.ellipse(pam,(0,255,0),(-10,120,100,70))
pygame.draw.ellipse(pam,(255,0,230),(100,120,10,10))
pygame.draw.ellipse(pam,(255,0,230),(50,110,10,10))
pygame.draw.ellipse(pam,(255,0,230),(90,180,10,10))
pygame.draw.ellipse(pam,(255,0,230),(100,200,10,10))
pam=pygame.transform.scale(pam,(300,300))
pam=pygame.transform.flip(pam,0,0)
screen.blit(pam,(0,-50))
#дерево 4
pam=pygame.Surface((400,400))
pam.set_colorkey((0,0,0))
pygame.draw.rect(pam,(115,0,0),(50,200,30,100))
pygame.draw.ellipse(pam,(0,255,0),(20,100,100,70))
pygame.draw.ellipse(pam,(0,255,0),(20,150,100,70))
pygame.draw.ellipse(pam,(0,255,0),(70,120,100,70))
pygame.draw.ellipse(pam,(0,255,0),(-10,120,100,70))
pygame.draw.ellipse(pam,(255,0,230),(100,120,10,10))
pygame.draw.ellipse(pam,(255,0,230),(50,110,10,10))
pygame.draw.ellipse(pam,(255,0,230),(90,180,10,10))
pygame.draw.ellipse(pam,(255,0,230),(100,200,10,10))
pam=pygame.transform.scale(pam,(400,400))
pam=pygame.transform.flip(pam,0,0)
screen.blit(pam,(0,150))
#дерево 2
pam=pygame.Surface((400,400))
pam.set_colorkey((0,0,0))
pygame.draw.rect(pam,(115,0,0),(50,200,30,100))
pygame.draw.ellipse(pam,(0,255,0),(20,100,100,70))
pygame.draw.ellipse(pam,(0,255,0),(20,150,100,70))
pygame.draw.ellipse(pam,(0,255,0),(70,120,100,70))
pygame.draw.ellipse(pam,(0,255,0),(-10,120,100,70))
pygame.draw.ellipse(pam,(255,0,230),(100,120,10,10))
pygame.draw.ellipse(pam,(255,0,230),(50,110,10,10))
pygame.draw.ellipse(pam,(255,0,230),(90,180,10,10))
pygame.draw.ellipse(pam,(255,0,230),(100,200,10,10))
pam=pygame.transform.scale(pam,(100,100))
pam=pygame.transform.flip(pam,1,0)
screen.blit(pam,(0,350))
#единорог
pygame.draw.ellipse(screen,(255,255,255),(240,250,100,70))
pygame.draw.ellipse(screen,(255,255,255),(290,200,50,30))
pygame.draw.ellipse(screen,(255,255,255),(328,215,20,15))
pygame.draw.rect(screen,(255,255,255),(300,210,20,50))
pygame.draw.rect(screen,(255,255,255),(315,310,10,40))
pygame.draw.rect(screen,(255,255,255),(300,300,10,40))
pygame.draw.rect(screen,(255,255,255),(280,310,10,40))
pygame.draw.rect(screen,(255,255,255),(260,300,10,40))
pygame.draw.ellipse(screen,(255,100,180),(320,210,10,10))
pygame.draw.ellipse(screen,(0,1,0),(322,210,5,5))
pygame.draw.polygon(screen,(230,220,170),[(320, 170), (326, 200), (318, 202)])
pygame.draw.ellipse(screen,(255, 131, 250, 255),(200,280,50,20))
pygame.draw.ellipse(screen,(255, 131, 250, 255),(230,250,50,20))
pygame.draw.ellipse(screen,(255, 131, 250, 255),(250,200,50,20))
pygame.draw.ellipse(screen,(255, 131, 250, 255),(220,300,50,20))
pygame.draw.ellipse(screen,(224, 238, 224, 255),(210,270,50,20))
pygame.draw.ellipse(screen,(224, 238, 224, 255),(250,300,50,20))
pygame.draw.ellipse(screen,(224, 238, 224, 255),(240,200,50,20))
pygame.draw.ellipse(screen,(224, 238, 224, 255),(250,220,50,20))
pygame.draw.ellipse(screen,(255, 165, 0, 255),(250,220,30,10))
pygame.draw.ellipse(screen,(255, 165, 0, 255),(270,240,30,10))
pygame.draw.ellipse(screen,(255, 165, 0, 255),(260,250,30,10))
pygame.draw.ellipse(screen,(255, 165, 0, 255),(240,300,30,10))
pygame.draw.ellipse(screen,(255, 165, 0, 255),(220,280,30,10))
pygame.draw.ellipse(screen,(238, 207, 161, 255),(250,200,40,10))
pygame.draw.ellipse(screen,(238, 207, 161, 255),(270,240,40,10))
pygame.draw.ellipse(screen,(238, 207, 161, 255),(260,280,40,10))
pygame.draw.ellipse(screen,(238, 207, 161, 255),(240,310,40,10))
pygame.draw.ellipse(screen,(238, 207, 161, 255),(210,290,40,10))
#единорог меньше
pam=pygame.Surface((400,400))
pam.set_colorkey((0,0,0))
pygame.draw.ellipse(pam,(255,255,255),(240,250,100,70))
pygame.draw.ellipse(pam,(255,255,255),(290,200,50,30))
pygame.draw.ellipse(pam,(255,255,255),(328,215,20,15))
pygame.draw.rect(pam,(255,255,255),(300,210,20,50))
pygame.draw.rect(pam,(255,255,255),(315,310,10,40))
pygame.draw.rect(pam,(255,255,255),(300,300,10,40))
pygame.draw.rect(pam,(255,255,255),(280,310,10,40))
pygame.draw.rect(pam,(255,255,255),(260,300,10,40))
pygame.draw.ellipse(pam,(255,100,180),(320,210,10,10))
pygame.draw.ellipse(pam,(0,1,0),(322,210,5,5))
pygame.draw.polygon(pam,(230,220,170),[(320, 170), (326, 200), (318, 202)])
pygame.draw.ellipse(pam,(255, 131, 250, 255),(200,280,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(230,250,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(250,200,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(220,300,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(210,270,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(250,300,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(240,200,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(250,220,50,20))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(250,220,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(270,240,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(260,250,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(240,300,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(220,280,30,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(250,200,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(270,240,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(260,280,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(240,310,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(210,290,40,10))
pam=pygame.transform.scale(pam,(100,100))
pam=pygame.transform.flip(pam,1,0)
screen.blit(pam,(350,150))
#единорог меньше 2
pam=pygame.Surface((400,400))
pam.set_colorkey((0,0,0))
pygame.draw.ellipse(pam,(255,255,255),(240,250,100,70))
pygame.draw.ellipse(pam,(255,255,255),(290,200,50,30))
pygame.draw.ellipse(pam,(255,255,255),(328,215,20,15))
pygame.draw.rect(pam,(255,255,255),(300,210,20,50))
pygame.draw.rect(pam,(255,255,255),(315,310,10,40))
pygame.draw.rect(pam,(255,255,255),(300,300,10,40))
pygame.draw.rect(pam,(255,255,255),(280,310,10,40))
pygame.draw.rect(pam,(255,255,255),(260,300,10,40))
pygame.draw.ellipse(pam,(255,100,180),(320,210,10,10))
pygame.draw.ellipse(pam,(0,1,0),(322,210,5,5))
pygame.draw.polygon(pam,(230,220,170),[(320, 170), (326, 200), (318, 202)])
pygame.draw.ellipse(pam,(255, 131, 250, 255),(200,280,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(230,250,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(250,200,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(220,300,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(210,270,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(250,300,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(240,200,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(250,220,50,20))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(250,220,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(270,240,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(260,250,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(240,300,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(220,280,30,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(250,200,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(270,240,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(260,280,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(240,310,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(210,290,40,10))
pam=pygame.transform.scale(pam,(200,200))
pam=pygame.transform.flip(pam,0,0)
screen.blit(pam,(50,100))
#единорог меньше 3
pam=pygame.Surface((400,400))
pam.set_colorkey((0,0,0))
pygame.draw.ellipse(pam,(255,255,255),(240,250,100,70))
pygame.draw.ellipse(pam,(255,255,255),(290,200,50,30))
pygame.draw.ellipse(pam,(255,255,255),(328,215,20,15))
pygame.draw.rect(pam,(255,255,255),(300,210,20,50))
pygame.draw.rect(pam,(255,255,255),(315,310,10,40))
pygame.draw.rect(pam,(255,255,255),(300,300,10,40))
pygame.draw.rect(pam,(255,255,255),(280,310,10,40))
pygame.draw.rect(pam,(255,255,255),(260,300,10,40))
pygame.draw.ellipse(pam,(255,100,180),(320,210,10,10))
pygame.draw.ellipse(pam,(0,1,0),(322,210,5,5))
pygame.draw.polygon(pam,(230,220,170),[(320, 170), (326, 200), (318, 202)])
pygame.draw.ellipse(pam,(255, 131, 250, 255),(200,280,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(230,250,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(250,200,50,20))
pygame.draw.ellipse(pam,(255, 131, 250, 255),(220,300,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(210,270,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(250,300,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(240,200,50,20))
pygame.draw.ellipse(pam,(224, 238, 224, 255),(250,220,50,20))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(250,220,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(270,240,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(260,250,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(240,300,30,10))
pygame.draw.ellipse(pam,(255, 165, 0, 255),(220,280,30,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(250,200,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(270,240,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(260,280,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(240,310,40,10))
pygame.draw.ellipse(pam,(238, 207, 161, 255),(210,290,40,10))
pam=pygame.transform.scale(pam,(300,300))
pam=pygame.transform.flip(pam,1,0)
screen.blit(pam,(70,100))
# pygame.Rect.move(10,10)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()