# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.bonus.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ashirzad <ashirzad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 18:38:04 by ashirzad          #+#    #+#              #
#    Updated: 2024/12/05 18:40:36 by ashirzad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import requests
from main import get_input

UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1

def main():
	data = get_input()

	count = search_word(data)
	print(count)

def search_word(data):
	count = 0
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == "A":
				count += ft_check(data, x, y)
	return count

def ft_check(data, x, y, y_dir, x_dir):
	try :
		if data[y][x] == "A":
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
