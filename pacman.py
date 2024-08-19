#DEVELOPED BY <PRIYANSHUL SHARMA>
#Webpage priyanshul.is-a.dev

import random 
import pygame
import time
from pygame.locals import   *

screen_width=800
screen_height=600
pygame.init()
pygame.display.set_caption("PAC-MAN")
screen=pygame.display.set_mode((screen_width,screen_height))

def change_bg(img):
    background=pygame.image.load(img)

    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image-pygame.image.load("pacman.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=(screen_width/2,screen_height/2)
        self.speed=5
        self.score=0
        self.lives=3

class Fruits(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        self.speed=random.randint(1,7)
        self.rect.center=(random.randint(0,screen_width),random.randint(0,screen_height))
        self.score=10

class Ghost(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        
        

