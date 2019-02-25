import time
import random
import decimal

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
    a_list[position] = current_value
    end = time.time()
    return end - start

def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list)// 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return end - start

def gap_insertion_sort(a_list, start, gap):
    starttime = time.time()
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value
    end = time.time()
    return end - starttime

def python_sort(a_list):
    start = time.time()
    list.sort(a_list)
    end = time.time()
    return end - start

def buildList(listSize):
    return [random.randint(0, listSize) for r in range(listSize)]

def runTests(testSize, listSize):
    testResults = {'Insertion Sort': {'time': 0},
    'Shell Sort': {'time': 0},
    'Python Sort': {'time': 0}}
    for x in range(testSize):
        for k, v in testResults.items():
            if k == 'Insertion Sort':
                testlist = buildList(listSize)
                testResults[k]['time'] += insertion_sort(testlist)
            if k == 'Shell Sort':
                testlist = buildList(listSize)
                testResults[k]['time'] += shell_sort(testlist)
            if k == 'Python Sort':
                testlist = buildList(listSize)
                testResults[k]['time'] += python_sort(testlist)
    for k, v in testResults.items():
        average = v['time']/listSize
        print '{} took {} seconds to run, on average.'.format(k, "%.6f" % average)

def main():
    print 'Test 1, 500 item lists'
    runTests(100, 500)
    print 'Test 2, 1000 item lists'
    runTests(100, 1000)
    print 'Test 3, 10000 item lists'
    runTests(100, 10000)

if __name__ == '__main__':
    main()