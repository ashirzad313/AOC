# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ashirzad <ashirzad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 14:30:24 by ashirzad          #+#    #+#              #
#    Updated: 2024/12/05 18:35:22 by ashirzad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import requests

UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1

def main():
	data = get_input()

	count = search_word(data)
	print(count)

def get_input():
	url = "https://adventofcode.com/2024/day/4/input"
	cookies = {"session" : "53616c7465645f5faf4ed976a9ef22c560513f22112043c55cd5e778e49997324f0a30013ed6746c6dbcdc307dad9d0e8ee325e7412e0b66a500feb77e187591"}

	re = requests.get(url, cookies=cookies)

	if re.status_code != 200:
		sys.exit("Invalid status_code", re.status_code)

	data = [line.strip("\n") for line in re.text.splitlines()]
	return data

def search_word(data):
	count = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == "X":
				count += ft_check(data, x, y, 0, RIGHT)
				count += ft_check(data, x, y, 0, LEFT)
				count += ft_check(data, x, y, DOWN, 0)
				count += ft_check(data, x, y, UP, 0)
				count += ft_check(data, x, y, DOWN, LEFT)
				count += ft_check(data, x, y, UP, LEFT)
				count += ft_check(data, x, y, UP, RIGHT)
				count += ft_check(data, x, y, DOWN, RIGHT)
	return count

def ft_check(data, x, y, y_dir, x_dir):
	try :
		if data[y][x] == "X":
			y += y_dir
			x += x_dir
			if x < 0 or y < 0:
					return 0
			if data[y][x] == "M":
				y += y_dir
				x += x_dir
				if x < 0 or y < 0:
					return 0
				if data[y][x] == "A":
					y += y_dir
					x += x_dir
					if x < 0 or y < 0:
						return 0
					if data[y][x] == "S":
						return 1
	except :
		pass
	return 0

if __name__ == "__main__":
	main()
