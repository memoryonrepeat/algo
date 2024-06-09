from most_active_cookie import Cookies, Parser
from datetime import datetime, timezone
import unittest

class Test(unittest.TestCase):
	maxDiff = None

	def test_invalid_date_value(self):
		with self.assertRaises(Exception) as ctx:
			Parser("cookie_log.csv", "2018-12-32")

	def test_invalid_date_format(self):
		with self.assertRaises(Exception) as ctx:
			Parser("cookie_log.csv", "2018/12/08")

	def test_invalid_content(self):
		with self.assertRaises(Exception) as ctx:
			Parser("invalid_cookie_log.csv", "2018-12-08")

	def test_valid_content(self):
		parser = Parser("cookie_log.csv", "2018-12-08")
		self.assertEqual(
			parser.content,
			[
				['AtY0laUfhglK3lC7', datetime(2018, 12, 9, 14, 19, tzinfo=timezone.utc)],
			  	['SAZuXPGUrfbcn5UA', datetime(2018, 12, 9, 10, 13, tzinfo=timezone.utc)],
			  	['5UAVanZf6UtGyKVS', datetime(2018, 12, 9, 7, 25, tzinfo=timezone.utc)],
				['AtY0laUfhglK3lC7', datetime(2018, 12, 9, 6, 19, tzinfo=timezone.utc)],
			  	['SAZuXPGUrfbcn5UA', datetime(2018, 12, 8, 22, 3, tzinfo=timezone.utc)],
			  	['4sMM2LxV07bPJzwf', datetime(2018, 12, 8, 21, 30, tzinfo=timezone.utc)],
			  	['fbcn5UAVanZf6UtG', datetime(2018, 12, 8, 9, 30, tzinfo=timezone.utc)],
			  	['4sMM2LxV07bPJzwf', datetime(2018, 12, 7, 23, 30, tzinfo=timezone.utc)]
			]
		)

	def test_empty_result(self):
		parser = Parser("cookie_log.csv", "2008-12-08")
		cookies = Cookies(parser.content, parser.date)
		self.assertEqual(
			cookies.mostActive,
			[]
		)

	def test_nonempty_result(self):
		parser = Parser("cookie_log.csv", "2018-12-08")
		cookies = Cookies(parser.content, parser.date)
		self.assertEqual(
			cookies.mostActive,
			['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
		)

if __name__ == "__main__":
	unittest.main(argv=['dummy-workaround'], exit=False)