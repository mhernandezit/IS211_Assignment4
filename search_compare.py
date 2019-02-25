""" Comparing speed of search algorithms in Python """
from __future__ import division
import time
import random

def sequential_search(a_list, item):
    """ Sequential Search """
    pos = 0
    found = False
    start = time.time()
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return found, (end - start)

def ordered_sequential_search(a_list, item):
    """ Ordered Sequential Search """
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
    """ Binary Search """
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
    """ Recursive Binary Search """
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
    """ A random list builder """
    randomList = random.sample(xrange(1, listSize+100), listSize)
    return randomList

def runTests(testSize, listSize):
    """ Builds out our test suites """
    testResults = {'Sequential Search': {'time': 0},
                   'Ordered Sequential Search': {'time': 0},
                   'Binary Search': {'time': 0},
                   'Recursive Binary Search': {'time': 0}}
    for x in xrange(testSize):
        testlist = buildList(listSize)
        for k, v in testResults.items():
            if k == 'Sequential Search':
                testResults[k]['time'] += sequential_search(testlist, -1)[1]
            if k == 'Ordered Sequential Search':
                list.sort(testlist)
                testResults[k]['time'] += ordered_sequential_search(testlist, -1)[1]
            if k == 'Binary Search':
                list.sort(testlist)
                testResults[k]['time'] += binary_search(testlist, -1)[1]
            if k == 'Recursive Binary Search':
                list.sort(testlist)
                rb = time.time()
                recursive_binary_search(testlist, -1)
                testResults[k]['time'] += time.time() - rb
    for k, v in testResults.items():
        average = v['time']/listSize
        print '{} took {} seconds to run, on average.'.format(k, "%10.7f" % average)

def main():
    """ Main excecution method """
    print 'Test 1, 500 item lists'
    runTests(100, 500)
    print 'Test 2, 1000 item lists'
    runTests(100, 1000)
    print 'Test 3, 10000 item lists'
    runTests(100, 10000)

if __name__ == '__main__':
    main()
