#!/bin/python3
import copy

def next_thing(source, element):
	for i in range(len(source)):
		if source[i] == element:
			try:
				return source[i + 1]
			except IndexError:
				return IndexError

def combine(available, lenght):
	x = []

	for prepare in range(lenght):
		x += [available[0]]

	print(x)
	while True:
		mostright = -1
		while next_thing(available, x[mostright]) == IndexError:
			x[mostright] = available[0]
			mostright -= 1
		x[mostright] = next_thing(available, x[mostright])
		yield copy.copy(x)


def embasy(tm, base = 10):
	result = 0
	for i in tm:
		result += i
		result *= base
	return result // base
		

def unique(collection):
	for item in collection:
		count = 0
		for iitem in collection:
			if iitem == item:
				count += 1
		if count > 1:
			return False
	return True

if __name__ == "__main__":
	thing = [0, 2, 4, 5, 6, 7]	
	try:
		for combination in combine(thing, len(thing)):
			if unique(combination):
				if embasy(combination[:2]) * embasy(combination[2:3]) == embasy(combination[3:]):
					print(combination)
	except IndexError:
		pass
