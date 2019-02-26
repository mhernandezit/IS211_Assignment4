""" Comparing speed of search algorithms in Python """
from __future__ import division
import time
import random

def sequential_search(a_list, item):
    """ Sequential Search
    Args:
        a_list (list) A list of integers
        item (int) The number we will be searching for

    Returns:
        found (boolean) True if the item is in the list
        algotime (float) Time the algorithm took to run

    """
    pos = 0
    found = False
    start = time.time()
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    algotime = end - start
    return found, algotime

def ordered_sequential_search(a_list, item):
    """ Ordered Sequential Search
    Args:
        a_list (list) A list of integers
        item (int) The number we will be searching for

    Returns:
        found (boolean) True if the item is in the list
        algotime (float) Time the algorithm took to run
    """
    pos = 0
    found = False
    stop = False
    start = time.time()
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return found, (end - start)

def binary_search(a_list, item):
    """ Binary Search
    Args:
        a_list (list) A list of integers
        item (int) The number we will be searching for

    Returns:
        found (boolean) True if the item is in the list
        algotime (float) Time the algorithm took to run

    """
    start = time.time()
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
    end = time.time()
    return found, (end - start)

def recursive_binary_search(a_list, item):
    """ Recursive Binary Search
    Args:
        a_list (list) A list of integers
        item (int) The number we will be searching for

    Returns:
        found (boolean) True if the item is in the list
    """
    if not a_list:
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
    """ A random list builder
    Args:
        listSize (int) The size of the list we want to build

    Returns:
        randomList (list) A randomly generated list

    """
    randomList = random.sample(xrange(1, listSize+100), listSize)
    return randomList

def runTests(testSize, listSize):
    """ Builds out our test suites, prints results of search algorithms
    Args:
        testSize (int) How many tests we want to run
        listSize (int) How big our random lists will be

    Returns:
        Null

    """
    testResults = {'Sequential Search': {'time': 0},
                   'Ordered Sequential Search': {'time': 0},
                   'Binary Search': {'time': 0},
                   'Recursive Binary Search': {'time': 0}}
    for _ in xrange(testSize):
        testlist = buildList(listSize) # We are only going to build the random list once
        for key, value in testResults.items():
            if key == 'Sequential Search': # Sequential search works on a unsorted list
                testResults[key]['time'] += sequential_search(testlist, -1)[1]
            if key == 'Ordered Sequential Search':
                list.sort(testlist)
                testResults[key]['time'] += ordered_sequential_search(testlist, -1)[1]
            if key == 'Binary Search':
                list.sort(testlist)
                testResults[key]['time'] += binary_search(testlist, -1)[1]
            if key == 'Recursive Binary Search':
                list.sort(testlist)
                rbTime = time.time()
                recursive_binary_search(testlist, -1)
                testResults[key]['time'] += time.time() - rbTime
    for key, value in testResults.items():
        average = value['time']/listSize
        print '{} took {} seconds to run, on average.'.format(key, "%10.7f" % average)

def main():
    """ Main excecution method """
    print 'Test 1, 500 item lists'
    runTests(100, 500)
    print 'Test 2, 1000 item lists'
    runTests(100, 1000)
    print 'Test 3, 10000 item lists'
    #runTests(100, 10000)

if __name__ == '__main__':
    main()
