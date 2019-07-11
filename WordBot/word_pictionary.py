import sys
from google_images_download import google_images_download as gImg
import pygame
import json

sys.path.append("../Utils/")
from getWord import getWord as getWord
from getColor import getColor as gc
from getColor import hexToRGB as h2rgb


def getImg(selCategory = None):
    word = getWord(category = selCategory)
    args = {
        "keywords": word,
        "limit": 1
    }
    response = gImg.googleimagesdownload()
    absolutePath = response.download(args)[0]
    return absolutePath[word][0]

def word_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 1000), pygame.RESIZABLE)
    done = False
    rave = False
    screen.fill(h2rgb(gc()))
    pygame.display.set_caption("CATNOOP")
        
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True   
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                    rave = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    image = pygame.image.load(getImg())       
                    screen.blit(image, (0,0))
                if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
                    rave = False
        if rave:
            screen.fill(h2rgb(gc()))
        
        pygame.display.flip()

word_game()
