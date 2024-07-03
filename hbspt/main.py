import requests

PROBLEM_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=0ebac529ec2a11512d0b216a790c"
RESULT_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=0ebac529ec2a11512d0b216a790c"

def getConversations(original):
	users = original["users"]
	conversations = []

	for user in users:
		currentConv = list(filter(lambda c: c["fromUserId"] == user["id"] or c["toUserId"] == user["id"], original["messages"]))

		if not currentConv:
			continue

		currentConv.sort(key = lambda c: c["timestamp"] , reverse = True)

		mostRecent = {
			"avatar": user["avatar"],
			"firstName": user["firstName"],
			"lastName": user["lastName"],
			"mostRecentMessage": {
				"content": currentConv[0]["content"],
				"timestamp": currentConv[0]["timestamp"],
				"userId": currentConv[0]["fromUserId"]
			},
			"totalMessages": len(currentConv),
			"userId": user["id"]
		}
		
		conversations.append(mostRecent)

	conversations.sort(key = lambda c: c["mostRecentMessage"]["timestamp"], reverse = True)

	return {
		"conversations": conversations
	}

def main():
	try:
		original = requests.get(PROBLEM_URL)
	except Exception:
		print("Error fetching input from", PROBLEM_URL)

	try:
		original = original.json()
	except Exception:
		print("Error parsing input from", PROBLEM_URL)

	result = requests.post(RESULT_URL, json = getConversations(original))

	print(result, result.text)

if __name__ == "__main__":
	main()
