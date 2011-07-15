# Hamaad Markhiani
# cPickle highScore interactive editing system
# Today's a beautiful day...yay.
# Go!
# 
import pygame
from pygame.locals import *
import cPickle
import random
import time

score = [400, 350, 300, 250, 200]
Name = ['Rimshaa', 'Hamaad', 'Jason', 'Tommy', 'Christy']

def mainMenu():
    print 'Hello! Welcome to the Ham-Blocks System_Files editor!'
    option = raw_input("Would you like to\n1:Edit Names\n2:Edit Numbers\n:")

##file = open("System_Files\\font.hamaad","r+")
##highScore = cPickle.load(file)
##print highScore
##file.close()

##file = open("System_Files\\font.hamaad","r+")
##highScore[0] = 400 # If change is needed
##cPickle.dump(highScore, file)
##file.close()

##file = open("System_Files\\sound.hamaad","r+")
##highScoreName = cPickle.load(file)
##print highScoreName[1]
##file.close()

##file = open("System_Files\\sound.hamaad","r+")
##highScoreName[0] = 'Rimshaa' # If change is needed, else use variable 'Name'
##cPickle.dump(Name, file)
##file.close()
