import requests
import sys

def main():
	data = read_input()

	rocksacks_total = findItem(data)
	print(rocksacks_total)

def read_input():
	url = "https://adventofcode.com/2022/day/3/input"
	cookies = {"session" :"53616c7465645f5fe30ea34caca24c7c16f55531030cd76f00296f17e67930b0b166594717ed9e73d2b265ff2dcece0877e2f479c7a57c14ec60c8b8c0e99f9a"}

	re = requests.get(url, cookies=cookies)

	if (re.status_code != 200):
		sys.exit(f"Invalid status_code {re.status_code}")


	data = []
	for line in re.text.splitlines():
		data.append(line)
	return (data)


def findItem(data):
	total = 0
	for rocksack in data:
		mid = int(len(rocksack) / 2)
		first_comp = set(rocksack[0:mid])
		second_comp = set(rocksack[mid:])

		common_item = (first_comp & second_comp).pop()
		total += get_value(common_item)
	return (total)


def get_value(letter):
	if letter.isupper():
		return ord(letter) - 38
	else :
		return ord(letter) - 96
	return (0)


if __name__ == "__main__":
	main()
