from string import Template
import unittest
import sys

LIST_SEPARATOR = ","
RANGE_SEPARATOR = "-"
STEP_SEPARATOR = "/"
ANY = "*"
TEMPLATE = "\
minute        $minute\n\
hour          $hour\n\
day of month  $dayOfMonth\n\
month         $month\n\
day of week   $dayOfWeek\n\
command       $command\n\
"

class Cron:
	def __init__(self, expression, toPrint = False):
		self.expression = expression
		self.toPrint = toPrint
		
		# Allow redundant whitespace for formatting
		self.items = list(filter(lambda item: len(item)>0 , self.expression.split(" ")))

		# Only allow 5 time + 1 command
		if len(self.items) != 6:
			raise Exception("Field length invalid")

		self.fields = {
			"minute": self.items[0],
			"hour": self.items[1],
			"dayOfMonth": self.items[2],
			"month": self.items[3],
			"dayOfWeek": self.items[4],
			"command": self.items[5]
		}

		self.result = {}
		self.report = Template(TEMPLATE)

		self.generateResult()
		self.generateReport()

	def getValueRange(self, type):
		if type == "minute":
			return [i for i in range(60)]
		elif type == "hour":
			return [i for i in range(24)]
		elif type == "dayOfMonth":
			return [i for i in range(1,32)]
		elif type == "month":
			return [i for i in range(1,13)]
		elif type == "dayOfWeek":
			return [i for i in range(7)]
		else:
			return []

	# Util function to parse each time field
	def parse(self, expression, valueRange):
		if not expression:
			return []

		lists = expression.split(LIST_SEPARATOR)

		if len(lists) > 1:
			return sorted(set([minute for l in lists for minute in self.parse(l, valueRange)]))

		interval, step = None, None

		if STEP_SEPARATOR in expression:
			interval, step = expression.split(STEP_SEPARATOR)
		else:
			interval = expression

		if RANGE_SEPARATOR in interval:
			start, end = map(int, interval.split(RANGE_SEPARATOR))

			if start < valueRange[0] or end > valueRange[-1]:
				raise Exception("Range {i} is out of boundary".format(i=interval))

			interval = [i for i in range(start, end+1)]
		elif interval == ANY:
			interval = valueRange
		elif interval.isnumeric():
			if int(interval) < valueRange[0] or int(interval) > valueRange[-1]:
				raise Exception("Range {i} is out of boundary".format(i=interval))
			interval = [int(interval)]
		else:
			raise Exception("Range {i} is not valid".format(i=interval))

		if step:
			interval = [i for i in range(interval[0], interval[-1]+1, int(step))]

		return interval

	def generateResult(self):
		for key, value in self.fields.items():
			if key == "command":
				self.result[key] = value
			else:
				self.result[key] = self.parse(value, self.getValueRange(key))

	def generateReport(self):
		if not self.result:
			return

		formattedResult = {}

		for key, value in self.result.items():
			if key == "command":
				formattedResult[key] = value
			else:
				value = map(str, value)
				formattedResult[key] = " ".join(value)

		self.report = self.report.safe_substitute(formattedResult)

		if self.toPrint:
			print(self.report)

class TestSum(unittest.TestCase):

	def test_handling_redundant_white_spaces(self):
		c = Cron(" 0    1 2   3   4   whoami  ")
		self.assertEqual(
			c.result,
			{
				"minute": [0],
				"hour": [1],
				"dayOfMonth": [2],
				"month": [3],
				"dayOfWeek": [4],
				"command": "whoami"
			},
			"Should filter out redundant whitespaces"
		)

	def test_handling_invalid_params_amount(self):
		with self.assertRaises(Exception) as ctx:
			Cron("0 1 2 3 4 5 6 whoami")

	def test_handling_invalid_range(self):
		with self.assertRaises(Exception) as ctx:
			Cron("0 1 32 3 4 5 whoami")

	def test_parse_wildcard(self):
		c = Cron("* * * * * whoami")
		self.assertEqual(
			c.result,
			{
				"minute": [i for i in range(60)],
				"hour": [i for i in range(24)],
				"dayOfMonth": [i for i in range(1,32)],
				"month": [i for i in range(1,13)],
				"dayOfWeek": [i for i in range(7)],
				"command": "whoami"
			},
			"Should parse wildcards correctly"
		)

	def test_parse_list(self):
		c = Cron("* * 1,3,4 * * whoami")
		self.assertEqual(
			c.result,
			{
				"minute": [i for i in range(60)],
				"hour": [i for i in range(24)],
				"dayOfMonth": [1,3,4],
				"month": [i for i in range(1,13)],
				"dayOfWeek": [i for i in range(7)],
				"command": "whoami"
			},
			"Should parse list correctly"
		)

	def test_parse_range(self):
		c = Cron("* * 5-9 * * whoami")
		self.assertEqual(
			c.result,
			{
				"minute": [i for i in range(60)],
				"hour": [i for i in range(24)],
				"dayOfMonth": [5,6,7,8,9],
				"month": [i for i in range(1,13)],
				"dayOfWeek": [i for i in range(7)],
				"command": "whoami"
			},
			"Should parse range correctly"
		)

	def test_parse_mixed_operators(self):
		c = Cron("* * */11,2-20/7,31 * * whoami")
		self.assertEqual(
			c.result,
			{
				"minute": [i for i in range(60)],
				"hour": [i for i in range(24)],
				"dayOfMonth": [1,2,9,12,16,23,31],
				"month": [i for i in range(1,13)],
				"dayOfWeek": [i for i in range(7)],
				"command": "whoami"
			},
			"Should parse mix of range / step / list correctly"
		)

def main():
	Cron(sys.argv[1], True)

if __name__ == "__main__":
	main()
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
