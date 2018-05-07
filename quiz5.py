#Matt Westelman
#5/7/18
#quiz5.py

list = [10,11,12,13,14]

def penultimate(L):
    return(L[len(L)-2])

def plusEquals(L,x):
    for item in L:
        print(item+x)

def smallest(L):
    sorted(L)
    return(L[0])

print(penultimate(list))
plusEquals(list,10)
print(smallest(list))
