import math

INPUT_FILE = "input2.txt"
MOVES = {
	"NORTH": (0,1),
	"EAST": (1,0),
	"WEST": (-1,0),
	"SOUTH": (0,-1)
}
ANGLE_DIRECTION_MAP = {
	0: "EAST",
	90: "NORTH",
	180: "WEST",
	270: "SOUTH"
}
DIRECTION_ANGLE_MAP = {value: key for key, value in ANGLE_DIRECTION_MAP.items()}
ROTATION = {
	"LEFT": 90,
	"RIGHT": -90
}

class Simulation():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.robot = {}
		self.logs = []

	def isValid(self, x, y):
		return 0<=x<self.width and 0<=y<self.height

	def report(self):
		if not self.robot:
			self.logs.append("Skipped REPORT instruction - robot not on table")
			return

		print(",".join(map(str,[self.robot["x"], self.robot["y"], ANGLE_DIRECTION_MAP[self.robot["angle"]]])))

	def move(self):
		if not self.robot:
			self.logs.append("Skipped MOVE instruction - robot not on table")
			return
		delta = MOVES[ANGLE_DIRECTION_MAP[self.robot["angle"]]]

		nextX = self.robot["x"] + delta[0]
		nextY = self.robot["y"] + delta[1]

		if not self.isValid(nextX, nextY):
			self.logs.append("Skipped MOVE instruction - robot would be out of bound "+self.robot)
			return

		self.robot["x"] = nextX
		self.robot["y"] = nextY

	def place(self, *args):
		x, y, direction = args
		x = int(x)
		y = int(y)

		if not self.isValid(x,y):
			self.logs.append("Skipped place instruction - robot would be out of bound "+args)
			return

		self.robot["x"] = x
		self.robot["y"] = y
		self.robot["angle"] = DIRECTION_ANGLE_MAP[direction]


	def rotate(self, direction):
		if not self.robot:
			self.logs.append("Skipped ROTATE instruction - robot not on table")
			return

		nextAngle = self.robot["angle"] + ROTATION[direction]

		# 0 <= r + k*360 < 360
		# -r/360 <= k < -r/360 + 1
		coeff = math.ceil(-nextAngle/360)

		self.robot["angle"] = nextAngle + coeff*360

	def simulate(self, instructions):
		for instruction in instructions:
			if " " not in instruction:
				command = instruction
			else:
				command, args = instruction.split(" ")
				args = args.split(",")

			if command == "PLACE":
				self.place(*args)
			elif command == "MOVE":
				self.move()
			elif command == "LEFT" or command == "RIGHT":
				self.rotate(command)
			elif command == "REPORT":
				self.report()
			else:
				raise Exception("Invalid command")

		if self.logs:
			print("----LOGS----")
			print("\n".join(self.logs))

def main():
	with open(INPUT_FILE) as reader:
		instructions = list(map(lambda line: line.strip(), reader.readlines()))

	simulation = Simulation(5,5)
	simulation.simulate(instructions)

if __name__ == "__main__":
	main()