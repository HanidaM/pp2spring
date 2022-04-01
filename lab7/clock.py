import imp
import pygame
import math
import datetime

pygame.init()

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()
bg = pygame.image.load("mk.xcf")

def ticker(R, th):
    y = math.cos(2 * math.pi * th / 360) * R
    x = math.sin(2 * math.pi * th / 360) * R
    return x + 400, -(y-400)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        cur_time = datetime.datetime.now()
        hour = cur_time.hour
        min = cur_time.minute
        sec = cur_time.second


        display.blit(bg, (0, 0))
        #min
        R = 300
        th = min * (360/60)
        pygame.draw.line(display, (0, 0, 0),(400, 400), ticker(R, th), 10)
        #hour
        R = 250
        th = hour * 30
        pygame.draw.line(display, (0, 0, 0),(400, 400), ticker(R, th), 10)

        #sec
        R = 350
        th = sec * (360/60)
        pygame.draw.line(display, (0, 0, 0),(400, 400), ticker(R, th), 8)
        
        pygame.display.update()
        clock.tick(60)
game()
pygame.quit()


