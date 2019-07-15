import sys
import pygame
import json
import shutil
import os

dirname = os.path.dirname(__file__)
directory = os.path.join(dirname, '../Utils/')

sys.path.append(directory)
from getWord import getWord as getWord
from getColor import getColor as gc
from getColor import hexToRGB as h2rgb
from google_images_download import google_images_download as gImg

def getImg(selCategory = None):
    word = getWord(category = selCategory)
    args = {
        "keywords": word,
        "limit": 1,
        "f": 'jpg',
        "s": "medium"
    }
    response = gImg.googleimagesdownload()
    absolutePath = response.download(args)[0]
    return absolutePath[word][0]

def word_game():
    dirname = os.path.dirname(__file__) + "/downloads"

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
                    if os.path.exists(dirname):
                        shutil.rmtree(dirname)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    screen.fill(h2rgb(gc()))                    
                    image = pygame.image.load(getImg(selCategory='animals'))  
                    image = pygame.transform.scale(image, (1280,720))
                    image_rect = image.get_rect()
                    screen.blit(image, (800-image_rect.width/2, 500-image_rect.height/2))
                if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
                    rave = False
        if rave:
            screen.fill(h2rgb(gc()))
        
        pygame.display.flip()

word_game()
