import pygame, sys, time, os, math
from pygame.locals import *

#pygame.init()

class Particle:
    def __init__(self, x, y, movement, gravity, l, w, g_s, c, gc, dr, layers, min_len):
        self.x = x
        self.y = y
        self.movement = movement
        self.gravity = gravity
        self.length = l
        self.width = w
        self.glow_size= g_s
        self.color = c
        self.glow_color = gc
        self.decay_rate = dr
        self.delta_time = 0
        self.layers = layers
        self.min_len = min_len
        
    def main(self, DISPLAY, delta_time, scroll, render):
        self.delta_time = delta_time
        self.length -= self.decay_rate*self.delta_time
        self.width -= self.decay_rate*self.delta_time
        if self.length > self.min_len:
            if self.movement[1] < 5: self.movement[1] += self.gravity * self.delta_time
            self.x += self.movement[0]*self.delta_time
            self.y += self.movement[1]*self.delta_time
            if self.glow_size > 0.1: self.glow_size -= (self.decay_rate*0.75)*self.delta_time
            if render: pygame.draw.circle(DISPLAY,self.color,[self.x+(self.length*0.5)-scroll[0],self.y+(self.length*0.5)-scroll[1]],self.length)
            if render: DISPLAY.blit(self.GLOW(self.glow_size*6,self.glow_color),((self.x-self.glow_size*6+(self.length*0.5))-scroll[0],(self.y-self.glow_size*6+(self.length*0.5))-scroll[1]),special_flags=BLEND_RGB_ADD)
        else: return 0

    def GLOW(self,size,color):
        surf = pygame.Surface((size*2,size*2))
        if self.layers > 2: pygame.draw.circle(surf,(Color(color)//Color(2,2,2)),(size,size),size)
        if self.layers > 1: pygame.draw.circle(surf,(Color(color)//Color(4,4,4))*Color(3,3,3),(size,size),size*0.66)
        if self.layers > 0: pygame.draw.circle(surf,color,(size,size),size*0.33)
        surf.set_colorkey((0,0,0))
        return surf
