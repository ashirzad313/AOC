import requests

def main():
	data = read_input()

	referee = {
		("A", "Y") : 6, ("A", "X") : 3, ("A", "Z") : 0,
		("B", "Z") : 6, ("B", "Y") : 3, ("B", "X") : 0,
		("C", "X") : 6, ("C", "Z") : 3, ("C", "Y") : 0,
	}

	point_obj = {"X" : 1, "Y": 2, "Z" : 3}

	max_point = 0
	for line in data:
		opponent, me = line
		max_point += referee[(opponent, me)] + point_obj[me]
	print(max_point)


def read_input():
	url = "https://adventofcode.com/2022/day/2/input"
	cookies = {"session" :"53616c7465645f5fe30ea34caca24c7c16f55531030cd76f00296f17e67930b0b166594717ed9e73d2b265ff2dcece0877e2f479c7a57c14ec60c8b8c0e99f9a"}

	re = requests.get(url, cookies=cookies)

	if (re.status_code != 200):
		sys.exit(f"Invalid status_code {re.status_code}")


	data = [line.strip().split(" ") for line in re.text.splitlines()]
	return (data)


if __name__ == "__main__":
	main()
