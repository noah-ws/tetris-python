#Tetris Game,  written in Python 3.6.5
#Version: 1.0
#Date: 26.05.2018

import sys
# caution: path[0] is reserved for script path (or '' in REPL)

import pygame #version 1.9.3
import sys

# Custom imports
from lib.InputController import GameKeyInput
from lib.Board import MainBoard
from lib.GameClock import GameClock
from lib.Fonts import *

pygame.init()
pygame.font.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

# Main game loop		
def gameLoop():		
	
	blockSize = 20 
	boardColNum = 10 
	boardRowNum = 20
	boardLineWidth = 10
	blockLineWidth = 1
	scoreBoardWidth = blockSize * (boardColNum//2)
	boardPosX = DISPLAY_WIDTH * 0.3
	boardPosY = DISPLAY_HEIGHT * 0.15

	mainBoard = MainBoard(pygame, gameClock, gameDisplay, key, blockSize, boardPosX, boardPosY, boardColNum, boardRowNum, boardLineWidth, blockLineWidth, scoreBoardWidth)	
	
	xChange = 0
	
	gameExit = False

	while not gameExit: #Stay in this loop unless the game is quit
		
		for event in pygame.event.get():	
			if event.type == pygame.QUIT: #Looks for quitting event in every iteration (Meaning closing the game window)
				gameExit = True
				
			if event.type == pygame.KEYDOWN: #Keyboard keys press events
				if event.key == pygame.K_a:
					xChange += -1
				if event.key == pygame.K_d:
					xChange += 1
				if event.key == pygame.K_s:
					key.down.status = 'pressed'
				if event.key == pygame.K_RIGHT: # Rotate CW
					if key.rotate.status == 'idle':
						key.rotate.trig = True
						key.rotate.status = 'pressed'
				if event.key == pygame.K_LEFT: # Rotate CCW
					if key.cRotate.status == 'idle':
						key.cRotate.trig = True
						key.cRotate.status = 'pressed'
				if event.key == pygame.K_p:
					if key.pause.status == 'idle':
						key.pause.trig = True
						key.pause.status = 'pressed'
				if event.key == pygame.K_r:
					if key.restart.status == 'idle':
						key.restart.trig = True
						key.restart.status = 'pressed'
				if event.key == pygame.K_RETURN:
					key.enter.status = 'pressed'
						
			if event.type == pygame.KEYUP: #Keyboard keys release events
				if event.key == pygame.K_a:
					xChange += 1
				if event.key == pygame.K_d:
					xChange += -1
				if event.key == pygame.K_s:
					key.down.status = 'released'
				if event.key == pygame.K_RIGHT:
					key.rotate.status = 'idle'
				if event.key == pygame.K_LEFT:
					key.cRotate.status = 'idle'
				if event.key == pygame.K_p:
					key.pause.status = 'idle'
				if event.key == pygame.K_r:
					key.restart.status = 'idle'
				if event.key == pygame.K_RETURN:
					key.enter.status = 'idle'
			
			if xChange > 0:
				key.xNav.status = 'right'
			elif xChange < 0: 
				key.xNav.status = 'left'	
			else:
				key.xNav.status = 'idle'
		
		gameDisplay.fill(BLACK) #Whole screen is painted Fonts.BLACK in every iteration before any other drawings occur 
			
		mainBoard.gameAction() #Apply all the game actions here	
		mainBoard.draw() #Draw the new board after game the new game actions
		gameClock.update() #Increment the frame tick
		
		pygame.display.update() #Pygame display update		
		clock.tick(60) #Pygame clock tick function(60 fps)

# Main program
key = GameKeyInput()		
gameClock = GameClock()	
gameLoop()	
pygame.quit()
sys.exit()