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

# Write a function that takes a list as an argument and veriﬁes whether the list is sorted. Return True if sorted; False if not.

def list_sorted(l : list):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

# Remove odds or evens:
# (a) Write a function that takes a list of integers as an argument, removes even numbers from the list, and returns the modified list.
# (b) Write a function that takes a list of integers as an argument, removes odd numbers from the list, and returns the modified list.
# (c) Write a function that takes a list of integers and a Boolean as arguments. If the Boolean is True, the function removes odd numbers 
# from the list; otherwise, evens are removed. The function returns the modified list.

def no_evens(lst : list) -> list:
    for num in lst:
        if num % 2 == 0:
            lst.remove(num)
    return lst

def no_odds(lst : list) -> list:
    for num in lst:
        if num % 2 != 0:
            lst.remove(num)
    return lst

def even_odds(lst : list) -> list:
    if lst[0] == True:
        lst.remove(lst[0])
        for num in lst:
            if num % 2 != 0:
                lst.remove(num)
    else:
        lst.remove(lst[0])
        for num in lst:
            if num % 2 == 0:
                lst.remove(num)
    return lst

# A palindrome is a word that is the same backward as forward. The word rotor is an example of a palindrome.
# (a) Write a function that returns True if a string is a palindrome. (Hints: You can create a list from a
# string using the list() function. Lists are handy, because there is a reverse() method.)
# (b) Write a program that uses your function. The program should prompt for a string, call the 
# function, and then print results (something other than True or False).
# (c) Some palindrome rules ignore spaces and capitalization, so “Never odd or even” is an acceptable palindrome. Improve your function 
# to ignore spaces and capitalization. (Hints: Lists have a remove() method, and strings have a lower() method.)

def check_palindrome(words) -> bool:
    words = words.lower().replace(' ', '')
    return words == words[::-1]

word_input = input("Enter a word or phrase to check if it is palindrome: ")

if check_palindrome(word_input):
    print(word_input, "is a palindrome")
else:
    print(word_input, "is not a palindrome")

# There are websites such as https://www.carsireland.ie/ that provide information about secondhand vehicles.
# Design a base class for vehicles with fields such as model year, total mileage, Vehicle Identification Number (VIN), 
# engine, transmission, options, and etc. Design subclasses for car, truck, SUV, and minivan. Think about the 
# specific fields and methods required for the subclasses. Instantiate your classes with examples so you can test your code.

class Vehicle(object):
    def __init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options ):
        self.name = name
        self.model = model_year
        self.mileage = mileage
        self.vehicle_id = vehicle_id
        self.engine = engine
        self.transmission = transmission
        self.options = options

    def age(self, current_year):
        return f"{current_year - self.model} years old"

    def update_milage(self, new_mileage):
        self.mileage = new_mileage

    def __str__(self):
        return (f"{self.model} {self.name}\n"
                f"Mileage: {self.mileage}\n"
                f"Vehicle ID: {self.vehicle_id}\n"
                f"Engine: {self.engine}\n"
                f"Transmission: {self.transmission}\n"
                f"Options: {self.options}\n")

class Truck(Vehicle):
    def __init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options, max_load):
        Vehicle.__init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options)
        self.max_load = max_load

    def age(self, current_year):
        return f"This truck is {current_year - self.model} years old"

    def __str__(self):
        return Vehicle.__str__(self) + f"Max load: {self.max_load}\n"

class Car(Vehicle):
    def __init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options, fuel_type):
        Vehicle.__init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options)
        self.fuel_type = fuel_type

    def fuel_type(self):
        return self.fuel_type

    def __str__(self):
        return Vehicle.__str__(self) + f"Fuel Type: {self.fuel_type}\n"
    
class Minivan(Vehicle):
    def __init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options, seating_capacity):
        Vehicle.__init__(self, name, model_year, mileage, vehicle_id, engine, transmission, options)
        self.seating_capacity = seating_capacity
    
    def __str__(self):
        return Vehicle.__str__(self) + f"No. of seats: {self.seating_capacity}\n"

# Design a class to represent a bank account. Some information you might want in a bank account are the IBAN,
# account number, available funds, a list with the last 5 transactions. You might also add methods to withdraw
# and deposit money. Then create a subclass MinimumBalanceAccount that inherits bankAccount.
# MinimumBalanceAccount should have a minimum balance value and overwrite the method withdrawal
# so the new balance is not below the minimum balance after withdrawing.

class BankAccount(object):
    def __init__(self, iban, account_number, balance=0.0):
        self.iban = iban
        self.account_number = account_number
        self.balance = balance
        self.last_transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.last_transactions.append("+" + str(amount))
        if len(self.last_transactions) > 5:
            self.last_transactions.pop(0)

    def withdraw(self, amount):
        self.balance -= amount
        self.last_transactions.append("-" + str(amount))
        if len(self.last_transactions) > 5:
            self.last_transactions.pop(0)

    def show_balance(self):
        return self.balance

    def transaction_history(self):
        return self.last_transactions

class MinimumBalanceAccount(BankAccount):
    def __init__(self, iban, account_number, balance=0.0):
        BankAccount.__init__(self, iban, account_number, balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.last_transactions.append("-" + str(amount))
            if len(self.last_transactions) > 5:
                self.last_transactions.pop(0)
        else:
            print("Insufficient funds")


# Complete the code for the classes Student and Registration using composition. Make sure 
# the main code works after adding your implementation.

class Student:
   """
   INSERT YOUR DOCSTRING INFORMATION HERE
   """
   def __init__(self, study_type, f_name, l_name):
       # YOUR CODE GOES HERE
       pass
   # YOUR CODE GOES HERE


class RegistrationData:
   """
   INSERT YOUR DOCSTRING INFORMATION HERE
   """
   def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
       # YOUR CODE GOES HERE
       pass
   # YOUR CODE GOES HERE


# MAIN SCOPE - UNCOMMENT IT AND RUN AFTER IMPLEMENTING YOUR SOLUTION
# r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
#                      Student.POSTGRADUATE, "Lucas", "Rizzo")
# r.display_student_data()
# print()
# r.set_student_id_property("C12345")
# r.display_student_data()
# print()
# for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
#     r.get_student_object().set_courses(course)
#
# r.display_student_data()
# print()
# print(r.get_student_object())  # extra to match the __str__ additional function
# print()
# print(RegistrationData.__doc__)

# Answer below:

class Student:
    """
    Represents student name and study type.
    """
    UNDERGRADUATE = "Undergraduate"
    POSTGRADUATE = "Postgraduate"

    def __init__(self, study_type, f_name, l_name):
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name
        self.courses = []

    def set_courses(self, courses):
        self.courses.append(courses)

    def __str__(self):
        return (f"Student: {self.f_name} {self.l_name}\n"
                f"Study Type: {self.study_type}\n"
                f"Courses: {self.courses}")

class RegistrationData:
    """
    For storing student registration data
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.address = address
        self.registration_fee = registration_fee
        self.student = Student(study_type, f_name, l_name)
        self.s_id = s_id

    def display_student_data(self):
        print("Address:", self.address)
        print("Registration Fee:", self.registration_fee)
        print(self.student)
        print("Student ID:", self.s_id)

    def set_student_id_property(self, student_id):
        self.s_id = student_id

    def get_student_object(self):
        return self.student

r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                      Student.POSTGRADUATE, "Lucas", "Rizzo")
r.display_student_data()
print()
r.set_student_id_property("C12345")
r.display_student_data()
print()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.get_student_object().set_courses(course)

r.display_student_data()
print()
print(r.get_student_object())
print()
print(RegistrationData.__doc__)

# Write a class called WholeNumber class. The whole numbers are the non-negative integers: 0,1,2, . . . Your class
# must handle addition, subtraction, and multiplication of whole numbers—no division or mixed-type (whole number 
# and integer) operations need be handled. Your class must also handle printing—e.g., if x is an instance 
# of the WholeNumber class, you must be able to print x. 
# 
# Two cases must not be allowed: 
# (1) you must not be able to create a WholeNumber that has a negative value; 
# (2) an arithmetic operation cannot be allowed to have a negative result. 
# 
# In both cases, an error message must be printed. Remember that arithmetic must return a whole number. 
# That is, if x and y are whole numbers, the result of x + y must be a whole number. 


class WholeNumber(object):
    def __init__(self, whole_number):
        if whole_number < 0:
            raise ValueError("Whole number cannot be negative")
        elif type(whole_number) != int:
            raise TypeError(whole_number, "is not a whole number")
        else:
            self.whole_number = whole_number

    def __add__(self, other):
        if type(other) != WholeNumber:
            raise TypeError(other, "is not a whole number")
        else:
            return WholeNumber(self.whole_number + other.whole_number)

    def __sub__(self, other):
        if type(other) != WholeNumber:
            raise TypeError(other, "is not a whole number")
        else:
            answer = self.whole_number - other.whole_number

        if answer < 0:
            raise ValueError("Operation cannot result in a negative number")
        else:
            return WholeNumber(answer)

    def __mul__(self, other):
        if type(other) != WholeNumber:
            raise TypeError(other, "is not a whole number")
        else:
            return WholeNumber(self.whole_number * other.whole_number)

    def __str__(self):
        return str(self.whole_number)

x = WholeNumber(3)
y = WholeNumber(4)
print (y * x)
print (y + x)
print (y - x)

# Write a class for linear equations. A generic linear equation is of the form 
# y = mx + b where m and b are constants. Include the following methods: 
# (a) __init__, __str__, __repr__. 
# (b) value(x), which returns the value of the equation given x.
# (c) compose(LinearEquation) that composes two linear equations. That is, if y = ax + b and z = cx + d, then y(z)= (a*c)x +(a*d + b) and
# will be called as y.compose(z). Note that the compose operation is not commutative.
# (d) __add__ returns the sum of two linear equations. That is, if y = ax + b and 
# z = cx + d, then y + z = (a + c)x + (b + d).

class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def value(self, x):
        return self.m * x + self.b

    def compose(self, other):
        if not isinstance(other, LinearEquation):
            raise TypeError("Must be a LinearEquation")

        else:
            new_m = self.m * other.m
            new_b = self.m * other.b + self.b

            return LinearEquation(new_m, new_b)

    def __add__(self, other):
        if not isinstance(other, LinearEquation):
            raise TypeError("Must be a LinearEquation")

        else:
            new_m = self.m + other.m
            new_b = self.b + other.b

            return LinearEquation(new_m, new_b)

    def __str__(self):
        return f"y = {self.m}x + {self.b}"

    def __repr__(self):
        return f"LinearEquation(m={self.m}, b={self.b})"

# Write a Python class to represent a Vector. Implement the following behaviour in your Vector class:
# 
# a)	vector addition: If V1 is (x1, y1) and V2 is (x2, y2), the V1+V2 is the vector (x1+x2, y1+y2)
# b)	vector multiplication by an int: if V is (x, y), the V*n is the vector (x*n, y*n), where n is an integer number
# c)	vector subtraction: V1-V2 is the same as V1+(V2*-1), a vector (x1-x2,y1-y2)
# d)	vector multiplication with another vector: implement the dot product. If V1 is (x1,y1) and V2 is (x2,y2), then V1*V2 = x1*x2 + y1*y2, a scalar. Thus the dot product yields a scalar (number), not a vector.
# e)	vector magnitude: The magnitude based on the Pythagorean theorem for a vector V=(x,y) is the square root of (x + y).
# 
# Include any other appropriate methods, such a constructor and __str__, and pay attention to naming standards, private/public, etc.

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

        raise TypeError("Can only add Vector to Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

        raise TypeError("Can only subtract Vector from Vector")

    def __mul__(self, other):

        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)

        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        raise TypeError("Can only multiply Vector by int or Vector")

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))
