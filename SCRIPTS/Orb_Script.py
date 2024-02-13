import pygame, sys, time, os, math
from pygame.locals import *

#pygame.init()

class Orb:
    def __init__(self, x, y, length, width, angle):
        self.pos = [x, y]
        self.body = pygame.Rect(x, y, length, width)
        self.vel = 2.5
        self.angle = angle
        self.movement = [-(self.vel * math.cos(math.radians(self.angle + 90))),(self.vel * math.sin(math.radians(self.angle + 90)))]
        self.delta_time = 0
        self.dead = False

    def main(self, DISPLAY, enemys, delta_time, scroll):
        self.delta_time = delta_time
        
        for enemy in enemys:
            if math.sqrt((abs(self.body.x-enemy.body.x)**2) + (abs(self.body.y-enemy.body.y)**2)) < 75:
                self.angle = -((180 / math.pi) * -math.atan2((enemy.body.x-self.body.x), (enemy.body.y-self.body.y)))
                if self.vel < 2.5: self.vel += 0.05
                
        self.move()
        #pygame.draw.rect(DISPLAY, (255, 0, 255), pygame.Rect(int(self.pos[0]-scroll[0]), int(self.pos[1]-scroll[1]), self.body.width, self.body.height))
        if self.vel < 0: self.dead = True
        return self.dead

    def move(self):
        self.movement = [-(self.vel * math.cos(math.radians(self.angle + 90))),(self.vel * math.sin(math.radians(self.angle + 90)))]
        
        self.pos[0] += self.movement[0]*self.delta_time
        self.body.x = int(self.pos[0])
                
        self.pos[1] += self.movement[1]*self.delta_time
        self.body.y = int(self.pos[1])

        self.vel -= 0.01
