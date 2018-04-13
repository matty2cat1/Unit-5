#Matt Westelman
#4/14/18
#listDemo.py - Lists. How hard could this be?

words = input("Enter some words: ").split(" ")

print("The first word was: ",words[0])
print("The last word was: ",words[-1])

#printing list 1 item at a time
for item in words:
    print(item)

