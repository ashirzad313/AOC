# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    range.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ashirzad <ashirzad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/28 20:21:47 by ashirzad          #+#    #+#              #
#    Updated: 2024/11/28 20:56:26 by ashirzad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import sys
import csv

def main():
	writeFile()
	data = readFile()
	count = 0
	for pairs in data:
		if checkPairs(pairs):
			count += 1
	print(count)

def writeFile():
	url = "https://adventofcode.com/2022/day/4/input"
	cookies = {"session" :"53616c7465645f5fe30ea34caca24c7c16f55531030cd76f00296f17e67930b0b166594717ed9e73d2b265ff2dcece0877e2f479c7a57c14ec60c8b8c0e99f9a"}

	re = requests.get(url, cookies=cookies)

	if re.status_code != 200:
		sys.exit("Could not read the input")

	with open("input.csv", "w") as file:
		file.write(re.text)


def readFile():
	data = []
	with open("input.csv") as file:
		reader = csv.reader(file)
		for line in reader:
			range1, range2 = line[0].split("-")
			range3, range4 = line[1].split("-")
			data.append([int(range1), int(range2), int(range3), int(range4)])
	return data

def checkPairs(pairs):
	num1 = pairs[0]
	num2 = pairs[1]
	num3 = pairs[2]
	num4 = pairs[3]

	if num1 <= num3:
		if num2 >= num4:
			return True
	if num2 <= num1:
		if num4 >= num2:
			return True
	return False



main()
