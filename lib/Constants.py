ROW = (0)
COL = (1)

#The speed of the moving piece at each level. Level speeds are defined as Constants.LEVEL_SPEEDS[level]
#Each 10 cleared lines means a level up.
#After level 29,  speed is always 1. Max level is 99
LEVEL_SPEEDS = (48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)

DIRECTIONS = {
    'down' : (1, 0), 
    'right' : (0, 1), 
    'left' : (0, -1), 
    'downRight' : (1, 1), 
    'downLeft' : (1, -1), 
    'noMove' : (0, 0) 
}

#Initial(spawn) block definitons of each piece
SPAWN_DEFS = {
'I' : ((1, 0), (1, 1), (1, 2), (1, 3)), 
'O' : ((0, 1), (0, 2), (1, 1), (1, 2)), 
'T' : ((0, 1), (1, 0), (1, 1), (1, 2)), 
'S' : ((0, 1), (0, 2), (1, 0), (1, 1)), 
'Z' : ((0, 0), (0, 1), (1, 1), (1, 2)), 
'J' : ((0, 0), (1, 0), (1, 1), (1, 2)), 
'L' : ((0, 2), (1, 0), (1, 1), (1, 2)) }

BLOCK_COLORS = {
    'I' : (19, 232, 232),  #CYAN
    'O' : (236, 236, 14),  #YELLOW
    'T' : (126, 5, 126),  #PURPLE
    'S' : (0, 128, 0),  #GREEN
    'Z' : (236, 14, 14),  #RED
    'J' : (30, 30, 201),  #BLUE
    'L' : (240, 110, 2) 
} #ORANGE

PIECE_NAMES = ('I',  'O',  'T',  'S',  'Z',  'J',  'L')

POINTS_BASE = (0, 40, 100, 300, 1200)
#Total score is calculated as: Score = level*baseLinePoints[clearedLineNumberAtATime] + totalDropCount
#Drop means the action the player forces the piece down instead of free fall(By key combinations: down,  down-left,  down-rigth arrows)