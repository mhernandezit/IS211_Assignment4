import pprint
import time
import random

def sequential_search(a_list, item):
	pos = 0
	found = False
	start = time.now()
	while pos < len(a_list) and not found:
		if a_list[pos] == item:
			found = True
		else:
			pos = pos+1
	return found, (time.now() - start)

def ordered_sequential_search(a_list, item):
	pos = 0
	found = False
	stop = False
	start = time.now()
	while pos < len(a_list) and not found and not stop:
		if a_list[pos] == item:
			found = True
		else:
			if a_list[pos] > item:
				stop = True
		else:
			pos = pos+1
	return found, (time.now() - start)

def binary_search(a_list, item):
	start = time.now()
	first = 0
	last = len(a_list) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if a_list[midpoint] == item:
			found = True
		else:
			if item < a_list[midpoint]:
				last = midpoint - 1
		else:
			first = midpoint + 1
	return found, (time.now() - start)

def recursive_binary_search(a_list, item):
	if len(a_list) == 0:
		return False
	else:
		midpoint = len(a_list) // 2
	if a_list[midpoint] == item:
		return True
	else:
		if item < a_list[midpoint]:
			return recursive_binary_search(a_list[:midpoint], item)
		else:
			return recursive_binary_search(a_list[midpoint + 1:], item)

def buildList(listSize):
	return [random.randint(0, 1000) for r in xrange(listSize)]

def runTests():
	testResults = {'Sequential_Search': {'Total_Time': 0, 'Average_Time': 1},
	'ordered_sequential_search': {'Total_Time': 0, 'Average_Time': 1},
	'binary_search': {'Total_Time': 0, 'Average_Time': 1},
	'recursive_binary_search': {'Total_Time': 0, 'Average_Time': 1}}
	for x in xrange(100):
		testList = buildList(500)
		found, testResults['Sequential_Search']['Total_Time'] =  sequential_search(testList, -1)
	