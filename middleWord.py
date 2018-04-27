#Matt Westelman
#4/26/18
#middleWord.py - Treat strings as lists

words = input('Enter some words ' ).split(' ')

if len(words)%2==1:
    print(words[len(words)/2])
if len(words)%2==0:
    print(words[len(words)/2-1],(words[len(words)/2]))
