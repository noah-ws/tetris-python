from lib.MovingBlock import MovingBlock
from lib.Constants import *

# Class for all the definitions of current moving piece
class MovingPiece:
	def __init__(self, gameClock, key, colNum, rowNum, status):

		self.colNum = colNum
		self.rowNum = rowNum
		self.gameClock = gameClock
		self.key = key

		self.blockMat = [['empty'] * colNum for i in range(rowNum)]
		
		self.blocks = []
		for i in range(0, 4):
			self.blocks.append(MovingBlock())
		
		self.currentDef = [[0] * 2 for i in range(4)]
		self.status = status # 'uncreated' 'moving' 'collided'
		self.type = 'I' # 'O',  'T',  'S',  'Z',  'J',  'L'
		
		self.gameOverCondition = False
		
		self.dropScore = 0
		self.lastMoveType = 'noMove'
	
	def applyNextMove(self):
		for i in range(0, 4):
			self.blocks[i].currentPos.col = self.blocks[i].nextPos.col
			self.blocks[i].currentPos.row = self.blocks[i].nextPos.row
	
	def applyFastMove(self):
		
		if self.gameClock.move.check(self.gameClock.frameTick) == True:
			if self.lastMoveType == 'downRight' or self.lastMoveType == 'downLeft' or self.lastMoveType == 'down':
				self.dropScore = self.dropScore + 1
			self.applyNextMove()
			
	def slowMoveAction(self):
	
		if self.gameClock.fall.check(self.gameClock.frameTick) == True:
			if self.movCollisionCheck('down') == True:
				self.createNextMove('noMove')
				self.status = 'collided'
			else:
				self.createNextMove('down')
				self.applyNextMove()		
			
	def createNextMove(self, moveType):
		
		self.lastMoveType = moveType
		
		for i in range(0, 4):
			self.blocks[i].nextPos.row = self.blocks[i].currentPos.row + DIRECTIONS[moveType][ROW]
			self.blocks[i].nextPos.col = self.blocks[i].currentPos.col + DIRECTIONS[moveType][COL]
			
	def movCollisionCheck_BLOCK(self, dirType, blockIndex):
		if dirType == 'down':
			if (self.blocks[blockIndex].currentPos.row+1 > self.rowNum-1) or self.blockMat[self.blocks[blockIndex].currentPos.row + DIRECTIONS[dirType][ROW]][self.blocks[blockIndex].currentPos.col+DIRECTIONS[dirType][COL]] != 'empty':
				return True
		else:
			if ( ((DIRECTIONS[dirType][COL])*(self.blocks[blockIndex].currentPos.col+DIRECTIONS[dirType][COL])) > ( ((self.colNum-1)+(DIRECTIONS[dirType][COL])*(self.colNum-1)) / 2 ) or 
				   self.blockMat[self.blocks[blockIndex].currentPos.row+DIRECTIONS[dirType][ROW]][self.blocks[blockIndex].currentPos.col+DIRECTIONS[dirType][COL]] != 'empty' ):
				return True
		return False	
			
	def movCollisionCheck(self, dirType): #Collision check for next move
		for i in range(0, 4):
			if self.movCollisionCheck_BLOCK(dirType, i) == True:
				return True
		return False
		
	def rotCollisionCheck_BLOCK(self, blockCoor):
		if ( blockCoor[ROW]>self.rowNum-1 or blockCoor[ROW]<0 or blockCoor[COL]>self.colNum-1 or blockCoor[COL]<0 or self.blockMat[blockCoor[ROW]][blockCoor[COL]] != 'empty'):
			return True
		return False
		
	def rotCollisionCheck(self, blockCoorList): #Collision check for rotation
		for i in range(0, 4):
			if self.rotCollisionCheck_BLOCK(blockCoorList[i]) == True:
				return True
		return False
		
	def spawnCollisionCheck(self, origin): #Collision check for spawn

		for i in range(0, 4):
			spawnRow = origin[ROW] + SPAWN_DEFS[self.type][i][ROW]			
			spawnCol = origin[COL] + SPAWN_DEFS[self.type][i][COL]
			if spawnRow >= 0 and spawnCol >= 0:
				if self.blockMat[spawnRow][spawnCol] != 'empty':
					return True
		return False
	
	def findOrigin(self):
		
		origin = [0, 0]
		origin[ROW] = self.blocks[0].currentPos.row - self.currentDef[0][ROW]
		origin[COL] = self.blocks[0].currentPos.col - self.currentDef[0][COL]
		return origin
	
	def rotate(self, rotationType):
		
		if self.type != 'O':
			tempBlocks = [[0] * 2 for i in range(4)]		
			origin = self.findOrigin()
			
			if self.type == 'I':
				pieceMatSize = 4
			else:
				pieceMatSize = 3
				
			for i in range(0, 4):				
				if rotationType == 'CW':
					tempBlocks[i][ROW] = origin[ROW] + self.currentDef[i][COL]
					tempBlocks[i][COL] = origin[COL] + (pieceMatSize - 1) - self.currentDef[i][ROW]
				else:
					tempBlocks[i][COL] = origin[COL] + self.currentDef[i][ROW]
					tempBlocks[i][ROW] = origin[ROW] + (pieceMatSize - 1) - self.currentDef[i][COL]
									
			if self.rotCollisionCheck(tempBlocks) == False:
				for i in range(0, 4):
					self.blocks[i].currentPos.row = tempBlocks[i][ROW]
					self.blocks[i].currentPos.col = tempBlocks[i][COL]
					self.currentDef[i][ROW] = self.blocks[i].currentPos.row - origin[ROW]
					self.currentDef[i][COL] = self.blocks[i].currentPos.col - origin[COL]

	def spawn(self):

		self.dropScore = 0
		
		origin = [0, 3]
		
		for i in range(0, 4):		
			self.currentDef[i] = list(SPAWN_DEFS[self.type][i])	
		
		spawnTry = 0
		while spawnTry < 2:
			if self.spawnCollisionCheck(origin) == False:
				break
			else: 
				spawnTry = spawnTry + 1
				origin[ROW] = origin[ROW] - 1
				self.gameOverCondition = True
				self.status = 'collided'
					
		for i in range(0, 4):
			spawnRow = origin[ROW] + SPAWN_DEFS[self.type][i][ROW]			
			spawnCol = origin[COL] + SPAWN_DEFS[self.type][i][COL]
			self.blocks[i].currentPos.row = spawnRow
			self.blocks[i].currentPos.col = spawnCol
				
	def move(self,  lastBlockMat):
	
		if self.status == 'uncreated':
			self.status = 'moving'
			self.blockMat = lastBlockMat			
			self.spawn()
			
		elif self.status == 'moving':			
			
			if self.key.down.status == 'pressed':			
				if self.key.xNav.status == 'right':
					if self.movCollisionCheck('down') == True:
						self.createNextMove('noMove')
						self.status = 'collided'
					elif self.movCollisionCheck('downRight') == True:
						self.createNextMove('down')
					else:
						self.createNextMove('downRight')

				elif self.key.xNav.status == 'left':					
					if self.movCollisionCheck('down') == True:
						self.createNextMove('noMove')
						self.status = 'collided'
					elif self.movCollisionCheck('downLeft') == True:
						self.createNextMove('down')
					else:
						self.createNextMove('downLeft')
						
				else: # 'idle'
					if self.movCollisionCheck('down') == True:
						self.createNextMove('noMove')
						self.status = 'collided'
					else:
						self.createNextMove('down')
					
				self.applyFastMove()
					
			elif self.key.down.status == 'idle':
				if self.key.xNav.status == 'right':
					if self.movCollisionCheck('right') == True:
						self.createNextMove('noMove')
					else:
						self.createNextMove('right')
				elif self.key.xNav.status == 'left':
					if self.movCollisionCheck('left') == True:
						self.createNextMove('noMove')
					else:
						self.createNextMove('left')
				else:
					self.createNextMove('noMove')
					
				self.applyFastMove()
				
				self.slowMoveAction()
					
			else: # 'released'
				self.key.down.status = 'idle'
				#self.gameClock.fall.preFrame = self.gameClock.frameTick #Commented out because each seperate down self.key press and release creates a delay which makes the game easier
			
		#else: # 'collided'			
