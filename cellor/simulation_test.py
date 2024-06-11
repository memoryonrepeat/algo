from simulation import Simulation
import unittest

class Test(unittest.TestCase):
	maxDiff = None

	def test_simple_move(self):
		instructions = ["PLACE 0,0,NORTH", "MOVE", "REPORT"]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"0,1,NORTH"
		)

	def test_simple_rotation(self):
		instructions = ["PLACE 0,0,NORTH", "LEFT", "REPORT"]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"0,0,WEST"
		)

	def test_mixed_move_and_rotation(self):
		instructions = [
			"PLACE 1,2,EAST", 
			"MOVE",
			"MOVE",
			"LEFT",
			"MOVE",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"3,3,NORTH"
		)

	def test_multiple_places(self):
		instructions = [
			"PLACE 1,2,SOUTH",
			"MOVE",
			"MOVE",
			"RIGHT",
			"PLACE 3,4,WEST",
			"MOVE",
			"RIGHT",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"2,4,NORTH"
		)

	# Do nothing since the only instruction is invalid
	def test_invalid_place(self):
		instructions = [
			"PLACE 0,6,EAST",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			None
		)

	def test_invalid_then_valid_place(self):
		instructions = [
			"PLACE 0,6,EAST",
			"PLACE 0,2,EAST",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"0,2,EAST"
		)

	# Should skip the invalid place
	def test_valid_then_invalid_place(self):
		instructions = [
			"PLACE 0,2,EAST",
			"PLACE 0,6,EAST",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"0,2,EAST"
		)

	# Should skip the last two moves due to out of bound
	def test_should_skip_out_of_bound_moves(self):
		instructions = [
			"PLACE 0,3,NORTH",
			"MOVE",
			"MOVE",
			"MOVE",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"0,4,NORTH"
		)

	# Should work with multiple rotations
	def test_multiple_rotations(self):
		instructions = [
			"PLACE 0,3,NORTH",
			"RIGHT",
			"RIGHT",
			"RIGHT",
			"RIGHT",
			"RIGHT",
			"RIGHT",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"0,3,SOUTH"
		)

	# Should selectively skip invalid moves / places then continue valid ones
	def test_skip_then_move(self):
		instructions = [
			"PLACE 0,1,SOUTH",
			"MOVE",
			"MOVE",
			"MOVE",
			"LEFT",
			"MOVE",
			"REPORT"
		]
		simulation = Simulation(5,5,False,False)
		simulation.simulate(instructions)

		self.assertEqual(
			simulation.status,
			"1,0,EAST"
		)

	# Should throw exception on invalid commands
	def test_invalid_command(self):
		with self.assertRaises(Exception) as ctx:
			instructions = ["PLACE 0,1,SOUTH", "RUN"]
			simulation = Simulation(5,5,False,False)
			simulation.simulate(instructions)

if __name__ == "__main__":
	unittest.main(argv=['dummy-workaround'], exit=False)