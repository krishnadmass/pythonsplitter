import time

def splitbyArray(array, delayTime):
    for x in array:
        print(x, type(x))
        for y in x:
            print(y)
        time.sleep(delayTime)