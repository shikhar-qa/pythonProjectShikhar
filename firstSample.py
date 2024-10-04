from itertools import count
from sys import executable

from selenium.webdriver.ie.service import Service

print("Hello, world")

li = [200, 150, 30, 45]
#find and count
c = 0
for x in li:
    if x == 30:
        c = c + 1
print(c)

#find a lowest number
def findMin(listArg):
    minNum = listArg[0]
    for m in listArg:
        if m < minNum:
            minNum = m
    print("Min number: " + str(minNum))
    return minNum

minNum = findMin(li)

#Do sorting
li1 = [200, 150, 30, 45]
print(li1[-1])
sortedli = []
for y in range(len(li1)):
    minNum1 = findMin(li1)
    li1.remove(minNum1)
    sortedli.append(minNum1)
print(sortedli)

# find even or odd
evenodd = [2, 45]
for i in evenodd:
    if (i % 2) == 0:
        print("Even")

#Input operator
#inp = input("enter a number: ")
#print(inp)

#Palindrome
s = "malayalam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#This is an example to tell that if a variable has anything in it or not
p = ""
if p:
    print("True")


#try and exception (catch and print)
try:
    a = 5 / 0
except Exception as e:
    print(e)


### String and string manipulation
j = "This is a long string"
print(j.title())

v = "1980"
print(v.isdigit())

fname = "shikhar "
lname = "daftari"
print(fname + " " + lname)

for d in range(5):
    print(fname*d)

print(v * 2)

# compare string
# escape characters /n and /t
t = "wonderful day daftari"
print (t.count("day"))
print("daftari" in t)
print(t[::-1])

#check if enter value is digit
###
#entername = input("what is your age: ")
#if entername.isdigit():
#    print(entername)
#else:
#    print("not a digit")

greeting = "Good {}, {}."
time = "morning"
secondname = "shikhar"
print(greeting.format(time,secondname))


# Practice list
fruit = ["grapes", "papaya", "orange", "aaple"]
veg = ["carrot", "peas", "tomato", "potato"]
both = fruit + veg
print(both.count("peas"))
print("carrot" in veg)
