import os
import sys
import time

import random
import dircache
import pygame
dir = 'songs/anger/'
filename = random.choice(dircache.listdir(dir))
print "filename",filename
path = os.path.join(dir, filename)
print "path",path
#os.system("ffplay %s"%path)
#time.sleep(10)
#os.system("sudo killall ffplay")
#filename = 'some.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("%s"%path)
pygame.mixer.music.play()
pygame.event.wait()
