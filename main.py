#!/bin/python3
import copy

def next_thing(source, element):
	for i in range(len(source)):
		if source[i] == element:
			try:
				return source[i + 1]
			except IndexError:
				return IndexError

def combine(available, lenght, needsUnique = False):
	x = []
	for prepare in range(lenght):
		x += [available[0]]
	while True:
		mostright = -1
		while next_thing(available, x[mostright]) == IndexError:
			x[mostright] = available[0]
			mostright -= 1
		x[mostright] = next_thing(available, x[mostright])
		if not needsUnique or unique(x):
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
	thing = []
	amountOfDigits = None
	while amountOfDigits == None or not 2 < amountOfDigits < 10:
		amountOfDigits = int(input("Enter amount of digits: "))
	
	sizes = [None, None]
	while sizes[0] == None or not 0 < sizes[0] < amountOfDigits - 1:
		sizes[0] = int(input("Enter sizes[0]: "))
	while sizes[1] == None or not 0 < sizes[1] < amountOfDigits - sizes[0]:
		sizes[1] = int(input("Enter sizes[1]: "))

	for i in range(amountOfDigits):
		thing.append(int(input(f"Enter digit[{i}]: ")))	
	try:
		for combination in combine(thing, len(thing), needsUnique = True):
			if embasy(combination[:sizes[0]]) * embasy(combination[sizes[0]:(sizes[0] + sizes[1])]) == embasy(combination[sizes[0] + sizes[1]:]):
				print(combination)
	except IndexError:
		print("Complete!")
