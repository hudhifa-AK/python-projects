# Prompt the user for three numbers and print which is the largest of the three.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("The first number:", num1, "is the biggest number")
elif num2 > num1 and num2 > num3:
    print("The second number:", num2, "is the biggest number")
else:
    print("The third number:", num3, "is the biggest number")


# How many three-digit numbers are divisible by 17? Write a program to print them.

count = 0
for num in range(100,1000):
    if num % 17 == 0:
        count += 1
print("There are", count, "three digit numbers that are divisible by 17")

# Sum of consecutive integers
# (a) Write a program that prompts for an integer — let’s call it X — and then finds the sum of X consecutive integers starting at 1. That is, if X = 5, you will find the sum of 1 + 2 + 3 + 4 + 5 = 15.

x = int(input("Type a number: "))
total = 0
for i in range(1, x+1):
    total += i
print(total)

#(b) Modify your program by enclosing your loop in another loop so that you can find consecutive sums. For example, if 5 is entered, you will find five sums of consecutive numbers:
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

x = int(input("Type a number: "))
total = 0
for i in range(1, x+1):
    total += i
    print(total)

# (c) Modify your program again to only print sums if the sum is divisible by the number of operands. For example, with the sum 1 + 2 + 3 + 4 + 5 = 15, there are five operands and the sum, 15, is divisible by 5, so that sum will be printed. (Do you notice a pattern?)

x = int(input("Type a number: "))
total = 0
for i in range(1, x+1):
    total += i
if total % x == 0:
    print(total)

# Write a FOR loop that will iterate from 0 to 20. For each iteration, it will check if the current number is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").

for i in range(0,21):
    if i % 2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")
# Ask the user to enter a number and print it back on the screen. Keep asking for a new number until they enter a negative number.

number = 1
while number > 0:
    number = int(input("give a number:"))
    print(number)

# (a) Write a FOR loop that will iterate from 0 to 10. For each iteration of the loop, it will multiply the number by 9 and print the result (e.g. "2 * 9 = 18").

for i in range(0,11):
    print(i,"* 9 =", i*9)

# (b) Use a nested loop to show the tables for every multiplier from 1 to 10 (100 results total).

for i in range(1,11):
    for j in range(1,11):
        print(i, "*", j, "=", i * j)
# Write a program to calculate and print the factorial of a number using a FOR loop. The factorial of a number is the product of all integers up to and including that number, so the factorial of 4 is 4*3*2*1= 24

number = int(input("Enter a number: "))
factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(factorial)

# Write a program that uses loops to print the triangle below
# Hint 1: you will need to use nested loops.
# Hint 2: on line 1 we print 1 *, on line 2 we print 2 stars… on line x we print x stars…)
# *
# * *
# * * *
# * * * *
# * * * * *

number = int(input("Enter a number: "))
for i in range(1, number + 1):
    for j in range(i):
        print("*", end="")
    print()

# Write a program that allows you to play rock, paper, scissors against the computer. Import the random module to select the computer’s choice.

import random

computerRPS = ["rock", "paper", "scissors"]
computerRPS = random.choice(computerRPS)
humanRPS = input("rock paper scissors?")
print("You chose", humanRPS, "and computer chose", computerRPS)
if humanRPS == computerRPS:
    print("You tied")
elif humanRPS == "paper" and computerRPS == "rock":
    print("You Win!")
elif humanRPS == "paper" and computerRPS == "scissors":
    print("You lost :(")
elif humanRPS == "rock" and computerRPS == "scissors":
    print("You Win!")
elif humanRPS == "rock" and computerRPS == "paper":
    print("You lost :(")
elif humanRPS == "scissors" and computerRPS == "paper":
    print("You Win!")
elif humanRPS == "scissors" and computerRPS == "rock":
    print("You lost :(")
else:
    print("Invalid Input")

# Write a Python program to print each character of a string on a single line.

my_str = input("Input a string: ")
for char in my_str:
    print(char, end=" ")

# Write a Python program that will calculate the length of a string
# (We already have a function len that does that, but we want to implement our own)

my_str = input("Input a string: ")
index = 0
for char in my_str:
    index += 1
print(index)

# Given the string "Monty Python":
# (a)	Write an expression to print the first character.
print(my_str[0])
# (b)	Write an expression to print the last character.
print(my_str[-1])
# (c)	Write an expression including len to print the last character.
print(my_str[len(my_str) - 1])
# (d) Write an expression that prints "Monty".
print(my_str[:6])

# Write a Python program that reads a string and prints a string that is made up of the first two characters and the last two characters.
# If the string has a length less than 4 the program prints a message on the screen.

# For example: “hello there” will result in “here”

my_str = input("Enter a string: ")
new_str = " "
if len(my_str) < 4:
    print("Your string is too short")
else:
    new_str = my_str[:2] + my_str[-2] + my_str[-1]
    print(new_str)

# Given a variable S containing a string of odd length:
# (a) Write an expression to print the middle character.

my_str = input("Enter a string: ")

index = 0
letter = " "

if len(my_str) % 2 == 0:
    print(my_str, "isn't an odd number of letters")
else:
    index = int(len(my_str) / 2 - 0.5)
    print(my_str[index])

# (b) Write an expression to print the string up to but not including the middle character
# (i.e., the first half of the string).

my_str = input("Enter a string: ")

index = 0
letter = " "

if len(my_str) % 2 == 0:
    print(my_str, "isn't an odd number of letters")
else:
    index = int(len(my_str) / 2 - 0.5)
    print(my_str[:index])

# (c) Write an expression to print the string from the middle character to the end (not
# including the middle character).

my_str = input("Enter a string: ")

index = 0
letter = " "

if len(my_str) % 2 == 0:
    print(my_str, "isn't an odd number of letters")
else:
    index = int(len(my_str) / 2 - 0.5)
    print(my_str[index + 1:])

# Write a Python program that will reverse a string (using a loop, not using slicing)

my_str = "Hello World"
new_str = ""
for char in my_str:
    new_str = char + new_str
print(new_str)

# Write a Python program that will “encrypt” a string. The encryption algorithm we’ll use is add 1 to the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc. The string ‘abc’ becomes ‘bcd’. You’ll need to use the functions ord() and chr() discussed in class
# Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98) and find the
# character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’

my_string = "abc"
encrypted_string = ""
for char in my_string:
    encrypted_string += chr(ord(char) + 1)
print(encrypted_string)

#  (a) Suppose you want to print a line full of '#' characters. For simplicity, let’s say that a
# line can have only 80 characters. One way is to create a long string to be printed. How
# would you do it more elegantly in Python using the plus operation (+) of strings?

my_str = ""
for i in range(80):
    my_str += "#"
print(my_str)

# Suppose you want to print a column full of '#' characters. For simplicity, let’s
# say that a column could have only 30 characters. Similar to (a), how would you do
# it more elegantly in Python using the multiply operation (*) of strings? Hint: Use
# the newline character (‘\n’).

my_str = "#"
new_str = my_str * 30
for char in new_str:
    print(char)

# Suppose you have a string ab_string = 'abababababababab' . Write an
# expression to remove all the b’s and create a string string = 'aaaaaaaa' .

ab_string = 'abababababababab'
a_string = ''
for letter in ab_string:
    if letter == 'a':
        a_string += letter
print(a_string)

# Write a function that takes a number as a parameter and prints the
# numbers from 1 to that number on the screen.

def numbers_upto(n):
    if n == 0:
        print(0)
    else:
        for i in range(n):
            print(i + 1)
    return

# Write a function that takes a number as a parameter and iterates from 0
# to that number. For each iteration, it will check if the current number is even or odd,
# and report that to the screen (e.g. “1 is odd”, “2 is even”).

def numbers_even_odd(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
    return

# Write a function that takes a number as a parameter, iterates from 0 to
# that number, and for each iteration of the loop, multiplies the current number by 9
# and prints the result (e.g. “2 * 9 = 18”).

def numbers_by_9(n):
    for i in range(n+1):
        print(i, "* 9 =", i * 9)
    return

# Write a function that asks the user for a number and prints the sum of all
# numbers from 1 to the number they enter.

def numbers_sum(n):
    index = 0
    for i in range(n+1):
        index += i
    print(index)
    return

# Write a function to print a factorial of a number.

def factorial(n):
    index = 1
    for i in range(1,n+1):
        index *= i
    print(index)
    return

# Write a Python function to sum all numbers in a list.
# Sample list: [1, 2, 3, 4, 5, 6]. Expected Output: 21

numbers = [1,2,3,4,5,6]
addition = 0
for n in numbers:
    addition += n
print(addition)

# Write a Python function to get the largest number from a list. 
# Sample list: [1, 2, 3, 4, 5, 6]. Expected Output: 6

numbers = [1,2,3,4,5,6]
numbers.sort()
print(numbers[-1:])

# Write a Python function that takes a list of words and counts how many
# of them begin with ‘o’.
# Sample list: ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
# Expected Output: 2

words = ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
count = 0
for word in words:
    if word[0] == 'o':
        count += 1
print(count)

# (modify previous Ex) Write a Python function that takes a list of words and a
# character, and counts how many of the words in the list begin with that character.

def first_letter_check(words, letter: str):
    count = 0
    for word in words:
        if word[0] == letter:
            count += 1
    return count
l1 = ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
print(first_letter_check(l1, 'o'))

# Write a Python function that takes a list of numbers and returns a
# new list containing only the even numbers from the first list.
# Sample list: [1, 2, 3, 4, 5, 6]. Expected Output: [2, 4, 6]

def even_numbers(num: list) -> list:
    even_list = []
    for number in num:
        if number % 2 == 0:
            even_list.append(number)
    return even_list
listofnums = even_numbers([1,2,3,4,5,6])
print(listofnums)

# Create a list of 100 integers whose value and index are the same, e.g., L[5]=5.

my_list = []
for i in range(100):
   my_list.append(i)
print(my_list)

# Write a Python program to remove duplicates from a list.
# Sample list: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]. Expected Output: [1, 2, 3, 4, 5, 6]

my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
for num in my_list:
    for num2 in my_list:
        if num == num2:
            my_list.remove(num2)
print(my_list)

# Write a Python function that takes two lists and returns True if they have at least one common member.
# Sample list: [1, 2, 3, 4, 5, 6] and [10, 9, 8, 7, 6]. Expected Output: True

def same_number_check(num1, num2):
    for i in nums1:
        for j in nums2:
            if i == j:
                return True
    return False

nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [10, 9, 8, 7, 6]

print(same_number_check(nums1, nums2))

# Write a Python program to get the difference between the two lists.
# Sample list: [1, 2, 3, 4, 5, 6] minus [10, 9, 8, 7, 6]
# Expected Output: [1, 2, 3, 4, 5]
# Sample list: [10, 9, 8, 7, 6] minus [1, 2, 3, 4, 5, 6]
# Expected Output: [10, 9, 8, 7]

nums2 = [1, 2, 3, 4, 5, 6]
nums1 = [10, 9, 8, 7, 6]

for i in nums2:
    for j in nums1:
        if i == j:
            nums1.remove(i)
print(nums1)

# Write a Python program to convert a list of multiple integers into a single integer. 
# Sample list: [11, 33, 50]
# Expected Output: 113350

nums1 = [11, 33, 50]
processing_num = ""
result = 0
for num in nums1:
    processing_num += str(num)
result = int(processing_num)
print(result)
