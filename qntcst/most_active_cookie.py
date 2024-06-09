from datetime import datetime, timedelta
from collections import Counter
import argparse

class Parser():
	def __init__(self, filename, date):
		self.filename = filename
		self.format = "%Y-%m-%d"
		self.defaultTime = "T00:00:00+00:00"

		try:
			datetime.strptime(date, self.format)
		except ValueError:
			raise ValueError("Incorrect date format, should be YYYY-MM-DD")

		self.date = date + self.defaultTime

		with open(self.filename) as reader:
			self.content = reader.readlines()

		self.parseContent()

	
	def parseContent(self):
		self.content = self.content[1:] # Skip column names
		self.content = [l.split(",") for l in self.content]

		try:
			self.content = [[cookie, datetime.fromisoformat(timestamp.strip())] for cookie, timestamp in self.content]
		except ValueError:
			raise ValueError("Incorrect cookie format, should be <cookie ID>,<ISO date>")

class Cookies():
	def __init__(self, cookies, date):
		self.cookies = cookies
		self.date = date
		self.mostActive = self.getMostActive()

	def getMostActive(self):
		start = datetime.fromisoformat(self.date)
		end = start + timedelta(hours = 24)
		cookiesWithinDate = list(filter(lambda c: start <= c[1] <= end , self.cookies))

		if len(cookiesWithinDate) == 0:
			return []

		counter = Counter(list(map(lambda c: c[0], cookiesWithinDate)))

		mostActiveCount = max(counter.values())

		return [cookie for cookie in counter.keys() if counter[cookie] == mostActiveCount]

def main():
	argParser = argparse.ArgumentParser(description = "Find the most active cookie")
	argParser.add_argument('-f', required = True, help = "Name of log file", dest = "filename")
	argParser.add_argument('-d', required = True, help = "Date to filter", dest = "date")
	args = vars(argParser.parse_args())
	
	parser = Parser(args["filename"], args["date"])
	cookies = Cookies(parser.content, parser.date)

	print("\n".join(cookies.mostActive))
	

if __name__ == "__main__":
	main()