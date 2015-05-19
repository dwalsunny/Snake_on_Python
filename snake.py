#!/usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *


class Snake:
        __snakePosition = [0,0]
        __snakeSegments = [[0,0],[0,0],[0,0]]
        __raspberryPosition = [0,0]
        __raspberrySpawned = 1
        __direction = 'right'
        __changeDirection = __direction

        def __init__(self, snakePosition, snakeSegments, raspberryPosition, raspberrySpawned, direction):
               self.__snakePosition = snakePosition
               self.__snakeSegments = snakeSegments
               self.__raspberryPosition = raspberryPosition
               self.__raspberrySpawned = raspberrySpawned
               self.__direction = direction
               self.__changeDirection = direction

        def getsnakePosition(self):
                return self.__snakePosition

        def getsnakeSegments(self):
                return self.__snakeSegments

        def getraspberryPosition(self):
                return self.__raspberryPosition

        def getraspberrySpawned(self):
                return self.__raspberrySpawned

        def getdirection(self):
                return self.__direction

        def getchangeDirection(self):
                return self.__changeDirection

        def setSnakePosition(self, snakePosition):
                self.__snakePosition = snakePosition

        def setsnakeSegments(self, snakeSegments):
                self.__snakeSegments = snakeSegments

        def setraspberryPosition(self, raspberryPosition):
                self.__raspberryPosition = raspberryPosition

        def setraspberrySpawned(self, raspberrySpawned):
                self.__raspberrySpawned = raspberrySpawned

        def setdirection(self, direction):
                self.__direction = direction

        def setchangeDirection(self, changeDirection):
                self.__changeDirection = changeDirection

        def default(self):
                self.__snakePosition = [100,100]
                self.__snakeSegments = [[100,100],[80,100],[60,100]]
                self.__raspberryPosition = [300,300]
                self.__raspberrySpawned = 1
                self.__direction = 'right'
                self.__changeDirection = self.__direction

        def insert(self):
                self.__snakeSegments.insert(0,list(self.__snakePosition))

        def pop(self):
                self.__snakeSegments.pop()


def gameOver():
        gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
        gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (320, 10)
        playSurface.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()
        time.sleep(2)
        Reset()

def Reset():
        Kobra.default()
        Draw()

def Draw():
        playSurface.fill(blackColour)
        for position in Kobra.getsnakeSegments():
                pygame.draw.rect(playSurface,whiteColour, Rect(position[0], position[1], 20 ,20))
        raspPosition = Kobra.getraspberryPosition()
   tr     pygame.draw.rect(playSurface,redColour, Rect(raspPosition[0],raspPosition[1], 20 , 20))
        pygame.display.flip()


pygame.init()
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Raspberry Snake')
redColour = pygame.Color(255,0,0)
blackColour = pygame.Color(0,0,0)
whiteColour = pygame.Color(255,255,255)
greyColour = pygame.Color(150,150,150)
Kobra = Snake([100,100], [[100,100], [80,100], [60,100]], [300,300], 1 , 'right')

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == KEYDOWN:
                        if event.key == K_RIGHT or event.key == ord('d'):
                                Kobra.setchangeDirection('right') 
                        if event.key == K_LEFT or event.key == ord('a'):
                                Kobra.setchangeDirection('left')
                        if event.key == K_DOWN or event.key == ord('s'):
                                Kobra.setchangeDirection('down') 
                        if event.key == K_UP or event.key == ord('w'):
                                Kobra.setchangeDirection('up') 
                        if event.key == K_ESCAPE:
                                pygame.event.post(pygame.event.Event(QUIT))
        if Kobra.getchangeDirection() == 'right' and not Kobra.getdirection() == 'left':
                Kobra.setdirection(Kobra.getchangeDirection) 
        if Kobra.getchangeDirection() == 'left' and not Kobra.getdirection() == 'right':
                Kobra.setdirection(Kobra.getchangeDirection) 
        if Kobra.getchangeDirection() == 'up' and not Kobra.getdirection() == 'down':
                Kobra.setdirection(Kobra.getchangeDirection) 
        if Kobra.getchangeDirection == 'down' and not Kobra.getdirection == 'up':
                Kobra.setdirection(Kobra.getchangeDirection) 
        positionCheck = Kobra.getsnakePosition()
        if Kobra.getdirection() == 'right':
                positionCheck[0] += 20
        if Kobra.getdirection() == 'left':
                positionCheck[0] -= 20
        if Kobra.getdirection() == 'up':
                positionCheck[1] -= 20
        if Kobra.getdirection() == 'down':
                positionCheck[1] += 20
        Kobra.setSnakePosition(positionCheck)        
        Kobra.insert()
        if Kobra.getsnakePosition() == Kobra.getraspberryPosition():
                Kobra.setraspberrySpawned(0)
        else:
                Kobra.pop()
        if Kobra.getraspberrySpawned() == 0:
                x = random.randrange(1,32)
                y = random.randrange(1,24)
                Kobra.setraspberryPosition([int(x*20), int(y*20)]) 
                Kobra.setraspberrySpawned(1) 
        Draw()
        positionCheck = Kobra.getsnakePosition()
        if positionCheck[0] > 620 or positionCheck[0] < 0:
                gameOver()
                continue
        if positionCheck[1] > 460 or positionCheck[1] < 0:
                gameOver()
                continue
        segmentCheck = Kobra.getsnakeSegments()
        for snakeBody in segmentCheck[1:]:
                if Kobra.getsnakePosition() == snakeBody:
                        gameOver()
                        continue
        fpsClock.tick(20)
