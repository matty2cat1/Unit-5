#Matt Westelman
#5/3/18
#cocktailSort.py - implementing coctail sort

from random import *
from time import time

N = 3 #how many numbers will be sorted

def inOrder(A):
    if A == sorted(A):
        return True
    else:
        return False

def bestSort(A):
    while not inOrder(A):
        random.shuffle(A)
    return A


if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = bestSort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
