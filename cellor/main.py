import math

FILENAME = "input.txt"
ROWS, COLUMNS = 5,5
MOVES = {
	"NORTH": (0,1),
	"EAST": (1,0),
	"WEST": (-1,0),
	"SOUTH": (0,-1)
}
DIRECTION_ANGLE_MAP = {
	"EAST": 0,
	"NORTH": 90,
	"WEST": 180,
	"SOUTH": 270
}
ANGLE_DIRECTION_MAP = {value: key for key,value in DIRECTION_ANGLE_MAP.items()}
ROTATION = {
	"LEFT": 90,
	"RIGHT": -90
}

def getNextDirection(currentDirection, rotation):
	nextAngle = DIRECTION_ANGLE_MAP[currentDirection] + ROTATION[rotation]
	# 0 <= r + k*360 < 360
	# -r/360 <= k < -r/360 + 1
	coeff = math.ceil(-nextAngle/360)
	nextAngle += coeff*360
	
	return ANGLE_DIRECTION_MAP[nextAngle]


def main():
	getNextDirection("EAST", "LEFT")
	getNextDirection("EAST", "RIGHT")
	getNextDirection("NORTH", "LEFT")
	getNextDirection("NORTH", "RIGHT")
	getNextDirection("WEST", "LEFT")
	getNextDirection("WEST", "RIGHT")
	getNextDirection("SOUTH", "LEFT")
	getNextDirection("SOUTH", "RIGHT")

if __name__ == "__main__":
	main()