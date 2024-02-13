import pygame, sys, time, os, math
from pygame.locals import *

#pygame.init()

class Fireball:
    def __init__(self, x, y, length, width, angle):
        self.pos = [x, y]
        self.body = pygame.Rect(x, y, length, width)
        self.movement = [-(7.5 * math.cos(math.radians(angle + 90))),(7.5 * math.sin(math.radians(angle + 90)))]
        self.delta_time = 0
        self.dead = False

    def main(self, DISPLAY, tiles, delta_time, scroll):
        self.delta_time = delta_time

        self.pos[0] += self.movement[0]*self.delta_time
        self.body.x = int(self.pos[0])
        self.pos[1] += self.movement[1]*self.delta_time
        self.body.y = int(self.pos[1])
        
        hit_list = self.collision_test(tiles)

        #pygame.draw.rect(DISPLAY, (255, 0, 255), pygame.Rect(int(self.pos[0]-scroll[0]), int(self.pos[1]-scroll[1]), self.body.width, self.body.height))
        
        if len(hit_list) > 0: self.dead = True

        return self.dead

    def collision_test(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.body.colliderect(tile):
                hit_list.append(tile)
        return hit_list
