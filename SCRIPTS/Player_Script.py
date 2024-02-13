import pygame, sys, time, os
from pygame.locals import *

#pygame.init()

class Player:
    def __init__(self, x, y, image, length, width):
        self.pos = [x, y]
        self.body = pygame.Rect(x, y, length, width)
        self.img = image
        self.movement = [0,0]
        self.gravity = 0.075#0.1
        self.health = 100
        self.delta_time = 0
        self.jumps = 3

    def main(self, DISPLAY, tiles, delta_time, scroll, angle):
        self.delta_time = delta_time
        
        self.movement[1] += self.gravity * self.delta_time
        
        if self.movement[1] > 3.5: self.movement[1] = 3.5
        if self.movement[1] < -3.5: self.movement[1] = -3.5

        collisions = self.move(tiles)

        DISPLAY.blit(self.img,(int(self.pos[0]-scroll[0]), int(self.pos[1]-scroll[1])))
        #pygame.draw.rect(DISPLAY, (255, 0, 255), pygame.Rect(int(self.pos[0]-scroll[0]), int(self.pos[1]-scroll[1]), self.body.width, self.body.height))

    def collision_test(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.body.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, tiles):
        collision_types = {"top": False, "bottom": False, "right": False, "left": False}
        
        self.pos[0] += self.movement[0]*self.delta_time
        self.body.x = int(self.pos[0])
        hit_list = self.collision_test(tiles)
        
        for tile in hit_list:
            
            if self.movement[0] > 0:
                self.body.right = tile.left
                collision_types["right"] = True
                
            elif self.movement[0] < 0:
                self.body.left = tile.right
                collision_types["left"] = True

        if len(hit_list) > 0:
            self.pos[0] = self.body.x
                
        self.pos[1] += self.movement[1]*self.delta_time
        self.body.y = int(self.pos[1])
        hit_list = self.collision_test(tiles)
        
        for tile in hit_list:
            
            if self.movement[1] > 0:
                self.body.bottom = tile.top
                collision_types["bottom"] = True
                self.movement[1] = 0
                self.jumps = 3
                
            elif self.movement[1] < 0:
                self.body.top = tile.bottom
                collision_types["top"] = True
                self.movement[1] = 0

        if len(hit_list) > 0:
            self.pos[1] = self.body.y
                
        return collision_types
