#Class for the game input keys and their status
class GameKeyInput:
	
	def __init__(self):
		self.xNav = self.KeyName('idle', False) # 'left' 'right'
		self.down = self.KeyName('idle', False) # 'pressed' 'released'
		self.rotate = self.KeyName('idle', False) # 'pressed' //KEY UP
		self.cRotate = self.KeyName('idle', False) # 'pressed' //KEY Z
		self.enter = self.KeyName('idle', False) # 'pressed' //KEY Enter
		self.pause = self.KeyName('idle', False) # 'pressed' //KEY P
		self.restart = self.KeyName('idle', False) # 'pressed' //KEY R
		# Moving right or left
		self.xChange = 0

	def handle_input(self, event, pygame):
		if event.type == pygame.KEYDOWN: #Keyboard keys press events
			if event.key == pygame.K_a:
				self.xChange += -1
			if event.key == pygame.K_d:
				self.xChange += 1
			if event.key == pygame.K_s:
				self.down.status = 'pressed'
			if event.key == pygame.K_RIGHT: # Rotate CW
				if self.rotate.status == 'idle':
					self.rotate.trig = True
					self.rotate.status = 'pressed'
			if event.key == pygame.K_LEFT: # Rotate CCW
				if self.cRotate.status == 'idle':
					self.cRotate.trig = True
					self.cRotate.status = 'pressed'
			if event.key == pygame.K_p:
				if self.pause.status == 'idle':
					self.pause.trig = True
					self.pause.status = 'pressed'
			if event.key == pygame.K_r:
				if self.restart.status == 'idle':
					self.restart.trig = True
					self.restart.status = 'pressed'
			if event.key == pygame.K_RETURN:
				self.enter.status = 'pressed'
					
		if event.type == pygame.KEYUP: #Keyboard keys release events
			if event.key == pygame.K_a:
				self.xChange += 1
			if event.key == pygame.K_d:
				self.xChange += -1
			if event.key == pygame.K_s:
				self.down.status = 'released'
			if event.key == pygame.K_RIGHT:
				self.rotate.status = 'idle'
			if event.key == pygame.K_LEFT:
				self.cRotate.status = 'idle'
			if event.key == pygame.K_p:
				self.pause.status = 'idle'
			if event.key == pygame.K_r:
				self.restart.status = 'idle'
			if event.key == pygame.K_RETURN:
				self.enter.status = 'idle'
		
		if self.xChange > 0:
			self.xNav.status = 'right'
		elif self.xChange < 0: 
			self.xNav.status = 'left'	
		else:
			self.xNav.status = 'idle'
	
	class KeyName:
	
		def __init__(self,initStatus,initTrig):
			self.status = initStatus
			self.trig = initTrig
