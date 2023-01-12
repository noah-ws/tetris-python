# Class for the blocks of the moving piece. Each piece is made of 4 blocks in Tetris game		
class MovingBlock:

	def __init__(self):

		self.currentPos = self.CurrentPosClass(0, 0)
		self.nextPos = self.NextPosClass(0, 0)
	
	class CurrentPosClass:
	
		def __init__(self, row, col):
			self.row = row
			self.col = col
			
	class NextPosClass:
	
		def __init__(self, row, col):
			self.row = row
			self.col = col	
		