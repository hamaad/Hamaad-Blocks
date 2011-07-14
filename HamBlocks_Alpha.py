# HamBlocks Alpha 0.91
# Author: Hamaad Markhiani
# Email: hamaad.markhiani@gmail.com
# 

import pygame
import string
from pygame.locals import *
import time
import cPickle
import random

# --------------------------[RUN] VARIABLES--------------------------
# Define some colors
black    = (0,0,0)
white    = (255,255,255)
red      = (255,0,0)
blue     = (0,0,255)
green    = (0,255,0)
yellow   = (255,255,0)
brown    = (139,69,19)

timeLeft = 900 # How much time left / 60
timeLeftInSeconds = 0.0 # Time left in seconds, will change in main loop
begTime  = 900 # Time left
textHigh = '' # Random Text For High Score
score    = 0 # Score
username = 'GameDev' # What you is!
typed = '' # What they typed for username so far!
usernameCount = -1 # What position in username are you in so far? (If they backspace)
count    = 0 # For changing the size of new blocks
randomColor = 0 # Is randomized later on to determine who you use. (1-6)
randomColorCombo = '' # Is changed later on based on randomColor
cheat    = False # To allow input for the cheat code
musicOff = False # Is the music supposed to be turned off?

# Variables to determine cheat code (rimsha[a])
cheatr   = 0 
cheati   = 0
cheatm   = 0
cheats   = 0
cheath   = 0
cheata   = 0

version = 0.91 # Currently how many major updates done so far

screen_width = 800 
screen_height = 600 

# --------------------------[END] VARIABLES--------------------------

# The class for blocks
class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        
        pygame.sprite.Sprite.__init__(self) 

        if color == 'hankhill':
            self.image = pygame.image.load('Images\\hankhill.jpg')
            self.image.set_colorkey(black)
        elif color == 'bill':
            self.image = pygame.image.load('Images\\bill.jpg')
            self.image.set_colorkey(black)
        elif color == 'boomhauer':
            self.image = pygame.image.load('Images\\boomhauer.jpg')
            self.image.set_colorkey(black)
        elif color == 'dalegribble':
            self.image = pygame.image.load('Images\\dalegribble.jpg')
            self.image.set_colorkey(black)
        elif color == 'peggyhill':
            self.image = pygame.image.load('Images\\peggyhill.jpg')
            self.image.set_colorkey(black)
        elif color == 'luanneplatter':
            self.image = pygame.image.load('Images\\luanneplatter.jpg')
            self.image.set_colorkey(black)
        elif color == 'bobbyhill':
            self.image = pygame.image.load('Images\\bobbyhill.jpg')
            self.image.set_colorkey(black)
        else:
            self.image = pygame.Surface([width, height])
            self.image.fill(color)


        self.rect = self.image.get_rect()

# Initialize Pygame, and do not show the mouse!
# ^ This allows for using a "custom" cursor of Hank Hill, or a black box.
pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption('HamBlocks Version: ' + str(version)) # Caption
Surface = pygame.image.load("Images\\icon.jpg")
pygame.display.set_icon(Surface)
screen=pygame.display.set_mode([screen_width,screen_height])

# List of Sprites
block_list = pygame.sprite.RenderPlain()

# Renders all the sprites into a nice little list
all_sprites_list = pygame.sprite.RenderPlain()

for i in range(100):
    # This makes a block
    block = Block(black, 30, 30)

    # Set the location for the box...
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(40, screen_height)
    
    # Add the block to the magical list
    block_list.add(block)
    all_sprites_list.add(block)
    
    

# Create the Block for the player. (Default = Black)
player = Block(black, 30, 30)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# A Function to clear the screen!
def clear(color):
    screen.fill(color)

# A Function to tell them their score! [Needs some cleaning up]
def timeIsUp(score):
    clear(white)
    global highScore
    global highScoreName
    if (score > highScore[4]): # If you got 5th, try for 4th. 
        if (score > highScore[3]): # If you got 1st, try for 4th. 
            if (score > highScore[2]): # If you got 1st, try for 4th. 
                if (score > highScore[1]): # If you got 2nd, try for 1st. 
                    if (score > highScore[0]): # If you got 1st 
                        highScore[0] = score
                        highScoreName[0] = username
                        textHigh = 'You got 1st place in the high scores list! You ARE winning!'
                    else: 
                        highScore[1] = score
                        highScoreName[1] = username
                        textHigh = 'You got 2nd place in the high scores list!'
                else:
                    highScore[2] = score
                    highScoreName[2] = username
                    textHigh = 'You got 3rd place in the high scores list!'
            else:
                highScore[3] = score
                highScoreName[3] = username
                textHigh = 'You got 4th place in the high scores list!'
        else:
            highScore[4] = score
            highScoreName[4] = username
            textHigh = 'You got 5th place in the high scores list!'
    else:
        textHigh = 'You did not make it to the high scores list!'

    # Open the "font" file. It really is the highscore number file
    file = open("System_Files\\font.hamaad", 'r+')
    cPickle.dump(highScore, file)
    file.close()
    # Open the "sound" file. It really is the highscore name file
    file = open("System_Files\\sound.hamaad", 'r+')
    cPickle.dump(highScoreName, file)
    file.close()

    # Display the highscores
    font = pygame.font.Font(None,30)
    text = 'You got a score of ' + str(score) + '!'
    text2 = 'The system will now pause for 5 seconds and then quit!'
    text3 = textHigh
    text4 = 'High Scores List :'
    text5 = '1: ' + highScoreName[0] + '-' + str(highScore[0])
    text6 = '2: ' + highScoreName[1] + '-' + str(highScore[1])
    text7 = '3: ' + highScoreName[2] + '-' + str(highScore[2])
    text8 = '4: ' + highScoreName[3] + '-' + str(highScore[3])
    text9 = '5: ' + highScoreName[4] + '-' + str(highScore[4])
    ren = font.render(text, 1, red)
    ren2 = font.render(text2, 1, blue)
    ren3 = font.render(text3, 1, green)
    ren4 = font.render(text4, 1, black)
    ren5 = font.render(text5, 1, green)
    ren6 = font.render(text6, 1, green)
    ren7 = font.render(text7, 1, green)
    ren8 = font.render(text8, 1, green)
    ren9 = font.render(text9, 1, green)
    screen.blit(ren, (20,0))
    screen.blit(ren2, (20,18))
    screen.blit(ren3, (20,36))
    screen.blit(ren4, (20,54))
    screen.blit(ren5, (20,(4*18)))
    screen.blit(ren6, (20,(5*18)))
    screen.blit(ren7, (20,(6*18)))
    screen.blit(ren8, (20,(7*18)))
    screen.blit(ren9, (20,(8*18)))
                
    pygame.display.flip()
    time.sleep(5)
    done = True

# A Function to show them how to start!
def begin():
    global begTime
    clock.tick(100) # Set FPS to 100, so we can measure the time left
    
    # Collect the current highscore numbers. This is cleverly named "font"
    file = open("System_Files\\font.hamaad", 'r+')
    global highScore
    highScore = cPickle.load(file)
    file.close()
    
    # Collect the current highscore names. This is cleverly named "font"
    file = open("System_Files\\sound.hamaad", 'r+')
    global highScoreName
    highScoreName = cPickle.load(file)
    file.close()

    # Begin music playing! This will loop unless you press space during the game.
    begfont = pygame.font.Font(None,30)
    pygame.mixer.music.load("Sound\\boggle.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)
    
    while (begTime != 0):
        clear(white)
        begtext = str(username) + '! 15 seconds to collect the most boxes!'
        begren = begfont.render(begtext, 1, red)
        begtext2 = 'Waiting for ' + str(begTime/100) + ' more seconds!'
        begren2 = begfont.render(begtext2, 1, black)
        begtext3 = 'Try to beat the high score of player ' + highScoreName[0] + '-' + str(highScore[0]) + '!'
        begren3 = begfont.render(begtext3, 1, green)
        screen.blit(begren, (20,0))
        screen.blit(begren2, ((screen_width/4),30))
        screen.blit(begren3, (20,60))
        begTime -= 1
        pygame.display.flip()

# Takes input and returns a key. (For the name input)
def keysteal():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def name(screen):
  pygame.font.init()
  current_string = []
  display_box(screen, "Username:" + string.join(current_string,""))
  while 1:
    inkey = keysteal()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, "Username:" + string.join(current_string,""))
  return string.join(current_string,"")

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

screen = pygame.display.set_mode((320,240))
username = name(screen)
pygame.display.set_mode((800,600))

begin()

# --------------------------Main Loop--------------------------
while done==False:
    for event in pygame.event.get(): # If you did something
        if event.type == pygame.QUIT: # If you clicked x
            done=True # Exit the loop via the variable for the continuation

    # Clear the screen
    screen.fill(white)
    
    # Limit the FPS
    clock.tick(60)
    # Take some time off!
    timeLeft -= 1
    timeLeftInSeconds = timeLeft/60
    
    # Get the current mouse position.
    pos = pygame.mouse.get_pos()
    
    # Set the player object to the mouse location
    player.rect.x=pos[0]
    player.rect.y=pos[1]

    # Print some text!
    mainfont = pygame.font.Font(None,30)
    maintext = 'You have ' + str(timeLeftInSeconds) + ' seconds left! Score: ' + str(score) + '!'
    mainren = mainfont.render(maintext, 1, black)
    screen.blit(mainren, ((screen_width/4), 0))
    maintext2 = 'Hint: SPACE to pause music, & collect boxes with your mouse!'
    mainren2 = mainfont.render(maintext2, 1, black)
    screen.blit(mainren2, (50, 18))

    # Do you want your music off? Space key to turn it off!
    if musicOff == False:
        if pygame.key.get_pressed()[K_SPACE]:
            musicOff = True     
            pygame.mixer.music.stop()
    elif musicOff == True:
        if pygame.key.get_pressed()[K_SPACE]:
            musicOff = False
            pygame.mixer.music.load("Sound\\boggle.ogg")
            pygame.mixer.music.play(loops=-1, start=0.0)

    # Cheat codes!
    if cheat == False:
        if pygame.key.get_pressed()[K_r]:
            cheatr = 1
            print 'r'
        elif pygame.key.get_pressed()[K_i]:
            cheati = 1
            print 'i'
        elif pygame.key.get_pressed()[K_m]:
            cheatm = 1
            print 'm'
        elif pygame.key.get_pressed()[K_s]:
            cheats = 1
            print 's'
        elif pygame.key.get_pressed()[K_h]:
            cheath = 1
            print 'h'
        elif pygame.key.get_pressed()[K_a]:
            cheata = 1
            print 'a'
        elif (cheatr + cheati + cheatm + cheats + cheath + cheata == 6):
            for i in range(200):
                # This represents a block
                block = Block('hankhill', 30, 30)

                # Set a random location for the block
                block.rect.x = random.randrange(screen_width)
                block.rect.y = random.randrange(40, screen_height)
                
                # Add the block to the list of objects
                
                player = Block('hankhill', 50, 50)
                all_sprites_list.add(player)
                block_list.add(block)
                all_sprites_list.add(block)
                all_sprites_list.draw(screen)
                pygame.display.flip()
                            
            print 'CHEAT ON, Rimshaa!'
            cheat = True

    
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)  
    
    # Check the list of collisions.
    if len(blocks_hit_list) > 0:
        score += len(blocks_hit_list)
        count += len(blocks_hit_list)
        randomColor = random.randrange(6)
        if (randomColor == 0): randomColor += 1
        if (randomColor == 1): randomColorCombo = 'bill'
        if (randomColor == 2): randomColorCombo = 'boomhauer'
        if (randomColor == 3): randomColorCombo = 'peggyhill'
        if (randomColor == 4): randomColorCombo = 'bobbyhill'
        if (randomColor == 5): randomColorCombo = 'luanneplatter'
        if (randomColor == 6): randomColorCombo = 'dalegribble'
        if ( count > 5):
            count = count - 5
        block = Block(randomColorCombo, 40+count, 40+count)
        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(40, screen_height)
        
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
        
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Check em!
    if (timeLeft == 0):
        timeIsUp(score)
        done = True

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
