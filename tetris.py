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

DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1000

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

# Main game loop		
def gameLoop():		
	
	blockSize = 40
	boardColNum = 10
	boardRowNum = 20
	boardLineWidth = 10
	blockLineWidth = 1
	scoreBoardWidth = blockSize * (boardColNum // 2)
	boardPosX = DISPLAY_WIDTH * 0.35
	boardPosY = DISPLAY_HEIGHT * 0.1

	mainBoard = MainBoard(pygame, gameClock, gameDisplay, key, blockSize, boardPosX, boardPosY, boardColNum, boardRowNum, boardLineWidth, blockLineWidth, scoreBoardWidth)	
	
	gameExit = False

	while not gameExit: #Stay in this loop unless the game is quit
		
		for event in pygame.event.get():	
			if event.type == pygame.QUIT: #Looks for quitting event in every iteration (Meaning closing the game window)
				gameExit = True
				
			key.handle_input(event, pygame)
		
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