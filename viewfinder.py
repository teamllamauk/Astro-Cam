# Imports

import atexit
import cPickle as pickle
import errno
import fnmatch
import io
import os
import os.path
import picamera
import pygame
import stat
import threading
import time
import yuv2rgb
from pygame.locals import *
from subprocess import call  

# Globals

# Image size mode
fullRes = [1296, 972]
viewFinder = [320, 240]
 
 # Init
 
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')

rgb = bytearray(320 * 240 * 3)
yuv = bytearray(320 * 240 * 3 / 2)

pygame.init()
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
 
camera            = picamera.PiCamera()
atexit.register(camera.close)
camera.resolution = (viewFinder[0], viewFinder[1])
camera.crop       = (0.0, 0.0, 1.0, 1.0)

drawTargetRec = 0

# Main

while(True):
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            
            recSize = (mouseX - 10, mouseY - 10, 20, 20)
            drawTargetRec = 1
    
    if drawTargetRec == 1:
        pygame.draw.rect(screen, (255,0,0), recSize, 1)
    
    stream = io.BytesIO() # Capture into in-memory stream
    camera.capture(stream, use_video_port=True, format='raw')
    stream.seek(0)
    stream.readinto(yuv)  # stream -> YUV buffer
    stream.close()
    
    yuv2rgb.convert(yuv, rgb, viewFinder[0], viewFinder[1])
    
    img = pygame.image.frombuffer(rgb[0:(viewFinder[0] * viewFinder[1] * 3)], (viewFinder[0], viewFinder[1]), 'RGB')
    
    screen.blit(img, ((viewFinder[0] - img.get_width() ) / 2, (viewFinder[1] - img.get_height()) / 2))
    pygame.display.update()
