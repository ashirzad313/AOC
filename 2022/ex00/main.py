import requests
import sys

def main():
	data = read_input()

	array_total = [sum(line) for line in data]
	max_number = max(array_total)

	print(f"elf {array_total.index(max_number)} has the most Calories : {max_number}")

def read_input():

	url = "https://adventofcode.com/2022/day/1/input"
	cookie = { "session":"53616c7465645f5fe30ea34caca24c7c16f55531030cd76f00296f17e67930b0b166594717ed9e73d2b265ff2dcece0877e2f479c7a57c14ec60c8b8c0e99f9a"}
	r = requests.get(url, cookies=cookie)

	if (r.status_code != 200):
		sys.exit("page could not be opend")
	data = []
	array = []
	for line in r.text.splitlines():
		if line:
			array.append(int(line))
		else :
			data.append(array)
			array = []
	return (data)

if __name__ == "__main__":
	main()
