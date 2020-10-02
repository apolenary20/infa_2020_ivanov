import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
pygame.draw.rect(screen,(0, 238, 238, 255),(0,0,400,200))
pygame.draw.rect(screen,(154, 205, 50, 255),(0,200,400,200))
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
pygame.draw.ellipse(screen,(255, 131, 250, 255),(260,200,50,20))
pygame.draw.ellipse(screen,(255, 131, 250, 255),(220,300,50,20))
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
