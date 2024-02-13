import pygame, time, math, random
from pygame.locals import *

#pygame.init()

class Enemy:
    def __init__(self, x, y, image, length, width, hard):
        self.pos = [x, y]
        self.body = pygame.Rect(x, y, length, width) # 60 , 100 24 40
        self.playercollider = pygame.Rect(x, y, 16, 28) # 40 , 70
        self.img = image
        self.movement = [0,0]
        self.health = 200 if hard else 100
        self.radius = 200 if hard else 100
        self.delta_time = 0
        self.angle = random.randint(0, 360)
        self.speed = 1.50 if hard else 1.25
        
    def main(self, DISPLAY, delta_time, scroll, player_x, player_y, render):
        
        if self.health > 0:
            
            self.delta_time = delta_time
            
            if math.sqrt((abs(self.body.x-player_x)**2) + (abs(self.body.y-player_y)**2)) < self.radius:
                self.angle = (180 / math.pi) * -math.atan2((player_x-self.body.x), (player_y-self.body.y))
                self.move(True)
            else:
                self.angle += random.randint(-5,5)
                self.move(False)

            self.playercollider.x = self.body.x+4
            self.playercollider.y = self.body.y+6
            
            if render: DISPLAY.blit(self.img,(self.body.x-scroll[0],self.body.y-scroll[1]))
            #pygame.draw.rect(DISPLAY, (255, 0, 0), pygame.Rect(self.body.x-scroll[0], self.body.y-scroll[1], self.body.w, self.body.h))
            return False
            
        elif self.health <= 0:
            #self.particles.append([[self.body.x, self.body.y],[random.randint(-10,10)/10, random.randint(-10,10)/10],[size,size],[255,255,255],[100,100,100]])
            return True

    def move(self, focused):
        if focused == True:
            self.movement[0] = (self.speed*2) * math.cos(math.radians(self.angle + 90))
            self.movement[1] = (self.speed*2) * math.sin(math.radians(self.angle + 90))

        if focused == False:
            self.movement[0] = self.speed * math.cos(math.radians(self.angle + 90))
            self.movement[1] = self.speed * math.sin(math.radians(self.angle + 90))
            
        self.pos[0] += self.movement[0] * self.delta_time
        self.pos[1] += self.movement[1] * self.delta_time

        self.body.x = self.pos[0]
        self.body.y = self.pos[1]
            
        if self.pos[0] > 1024: self.pos[0] = -24
        elif self.pos[0] < -24: self.pos[0] = 1024
        #if self.pos[1] < -340: self.pos[1] = 40
        #elif self.pos[1] > 40: self.pos[1] = -340
        if self.pos[1] < -270: self.angle = 0
        elif self.pos[1] > -30: self.angle = 180

    def hit(self, damage):
        self.health = self.health - damage
