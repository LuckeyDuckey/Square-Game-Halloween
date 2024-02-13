import pygame, sys, time, os, math
from pygame.locals import *

#pygame.init()

class Ball:
    def __init__(self, x, y, length, width, angle):
        self.pos = [x, y]
        self.body = pygame.Rect(x, y, length, width)
        self.movement = [-(7.5 * math.cos(math.radians(angle + 90))),(7.5 * math.sin(math.radians(angle + 90)))]
        self.delta_time = 0
        self.dead = False
        self.bounces = 3

    def main(self, DISPLAY, tiles, delta_time, scroll, sound):
        self.delta_time = delta_time
        self.move(tiles, sound)
        #pygame.draw.rect(DISPLAY, (255, 0, 255), pygame.Rect(int(self.pos[0]-scroll[0]), int(self.pos[1]-scroll[1]), self.body.width, self.body.height))
        if self.bounces < 0: self.dead = True
        return self.dead

    def collision_test(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.body.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, tiles, sound):
        self.pos[0] += self.movement[0]*self.delta_time
        self.body.x = int(self.pos[0])
        hit_list = self.collision_test(tiles)
        
        for tile in hit_list:
            
            if self.movement[0] > 0:
                self.body.right = tile.left
                self.movement[0] = -self.movement[0]
                
            elif self.movement[0] < 0:
                self.body.left = tile.right
                self.movement[0] = -self.movement[0]

        if len(hit_list) > 0:
            pygame.mixer.Sound.play(sound)
            self.pos[0] = self.body.x
            self.bounces -= 1
                
        self.pos[1] += self.movement[1]*self.delta_time
        self.body.y = int(self.pos[1])
        hit_list = self.collision_test(tiles)
        
        for tile in hit_list:
            
            if self.movement[1] > 0:
                self.body.bottom = tile.top
                self.movement[1] = -self.movement[1]
                
            elif self.movement[1] < 0:
                self.body.top = tile.bottom
                self.movement[1] = -self.movement[1]

        if len(hit_list) > 0:
            pygame.mixer.Sound.play(sound)
            self.pos[1] = self.body.y
            self.bounces -= 1
