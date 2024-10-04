#This is a python practice file, it has sample problem and solution
from importlib.readers import remove_duplicates
from math import factorial

# Sample 1: Reverse a String
def do_reverse_string(str1):
        print("\n************ Sample 1: Reverse a String *************")
        reversestr1 = str1[::-1]
        print(reversestr1)


#Sample 2: Check for Palindrome
def check_palindrome(str2):
    print("\n************ Sample 2: Check for Palindrome *************")
    reversestr2 = str2[::-1]
    if str2 == reversestr2:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")


#Sample 3: Fibonacci Series
print("\n************ Sample 3: Fibonacci Series *************")
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
n = 4
result = fibonacci(n)
print("Answer using recursive method: ", result)

# Without recursion
n1, n2 = 0, 1
sum = 0
for i1 in range(0, n):
    print((sum))
    n1 = n2
    n2 = sum
    sum = n1 + n2
print("Answer: " + str(sum))

# Sample 4: Factorial of a Number
def do_factorial(fac_num):
    print("\n************ Sample 4: Factorial of a Number *************")
    print("Factorial by Using math lib " + str(factorial(fac_num)))
    #Another way
    facto=1
    if fac_num <= 0:
        print("Incorrect number " + str(facto))
    elif fac_num == 1:
        print("Factorial number " + str(facto))
    else:
        for i2 in range(1,fac_num+1):
            facto = i2 * facto
        print("Factorial number " + str(facto))


# Sample 5: Even number check
def checkevenodd(num):
    print("\n************ Sample 5: Even number check *************")
    if num % 2 == 0:
        print("This number is even")
    else:
        print("This number is not even")

# Sample 6: prime number check
def checkprimenumber(sample):
    print("\n************ Sample 6: prime number check *************")
    for i in range(2,sample):
        if sample % i:
            print(str(sample) + " is a prime number")
            break
        else:
            print(str(sample) + " is not a prime number")
            break

# Sample 7: Count Vowels and Consonants
def count_vowels_conso(sample):
    print("\n************ Sample 7: Count Vowels and Consonants *************")
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelscount = 0
    for i in vowels:
        vowelscount = vowelscount + sample.count(i)
    print("Vowels count : " + str(vowelscount))
    consonants =  len(sample) - vowelscount
    print("consonants count : " + str(consonants))

# Sample 8: Sort an Array
def sortlist (samplelist):
    print("\n************ Sample 8: Sort an array *************")
    samplelist.sort()
    #print(samplelist)
    x = sorted(samplelist)
    print(x)

# Sample 9: Find largest element in an array
def findlargestnumber (samplelist):
    largestnum = samplelist[0]
    for x in samplelist:
        if x > largestnum:
            largestnum = x
    print("Largest number: ",  largestnum)
    print("Largest number using built-in function: ",  max(samplelist))

# Sample 10: Remove duplicate
def removeduplicate():
    samplelist = [20,28,21,20,21]
    uniquelist = []
    for x in samplelist:
        if x not in uniquelist:
            uniquelist.append(x)
    print(uniquelist)

