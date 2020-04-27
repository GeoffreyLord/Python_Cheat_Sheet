#NOTE:python 3.7
#This program is to be used as a massive example of how pyhton works


#________________________________________________________________________________________
#					PRINT
#________________________________________________________________________________________
print(" ")
print("__________PRINT__________")
print("Below are examples for printing in Python")
print(" ")
#EX. 1
print("Hello World!")

#EX. 2
message = "Hello Word"
print(message)

#EX. 3
message_2 = 'Hello World'
print(message_2)

#EX. 4
	#If there is a need for a '
message_3 = "Hello' World"
print(message_3)

#EX. 5
	#If there is a need for a "
message_4 = 'Hello" World'
print(message_4)

#EX. 6
	#If there is a need for ' and "
message_5 = """Hello'" World"""
print(message_5)

#________________________________________________________________________________________
#					Numbers
#_______________________________________________________________________________________
print(" ")
print("__________NUMBERS__________")
print("Below are examples for using numbers in Python")
print(" ")
#EX. 1
#In this example we will assign different number to their type and print that number
#There are four types of numbers in pyhton 
	#Int: Integers
	#Long: Longs are extreamly large or small ints
	#Floats: are integers with decimals ie. 2.0
	#Complex: are complex numbers denoted by j

a = 1 #This is an int
b = 100000000000000000000 #This is a long
c = 1.0 #This is a float
d = 1j #This is a complex

print("Below are computations using these numbers")

#addition
print("Addition")
add_int_int = a + a
add_int_long = a + b
add_int_float = a + c
add_int_complex = a + d
print(add_int_int, add_int_long, add_int_float, add_int_complex)

#subtraction
print("Subtraction")
sub_int_int = a - a
print(sub_int_int)

#Multiplication
print("Multiplication")
mult_int_float = a * c
print(mult_int_float)

#Division
print("Division")
div_int_float = a / c 
print(div_int_float)

#Remainder
print("Remainder")
rem_int_long = a % b
print(rem_int_long)
	#Reminder when using division you must account for rounding
	#Recomended: Use floats to insure an accurate answer is given
	#If you use two ints and there should be a remainder divison will only give quotent

#Exponents
print("Exponents")
exp_int_long = a ** b
print(exp_int_long)


#________________________________________________________________________________________
#                                       INPUT
#________________________________________________________________________________________
print(" ")
print("__________INPUTS__________")

fst_input = input("Please Enter Your Name: ")
print("Hello", fst_input)
print(" ")

print("Lets take in two numbers and output the sum")
comp1_input = float(input("Please enter your 1st Number: "))
comp2_input = float(input("Please enter your 2nd Number: "))

mult_comp1_comp2 = comp1_input + comp2_input
print(mult_comp1_comp2)

#________________________________________________________________________________________
#                                       BOOL
#________________________________________________________________________________________
print(" ")
print("__________BOOL__________")

#Bools are important in all programing languages
#note: you can compare all statements with ==, !=, <=, or >=
#When using bools they must be capped ie. True, False

#EX. 1
#Lets make a bool statement 
bool_1 = 1
bool_2 = 2

bool_result = bool_1 == bool_2
print(bool_result)
bool_result = bool_1 == bool_1
print(bool_result)


#________________________________________________________________________________________
#                                       IF/THEN/ELSE
#________________________________________________________________________________________
print(" ")
print("__________IF/THEN/ELSE__________")

#Ex. 1
#This will be example of an if statement
#It will tell you what type of triangle you have.

print("Lets find the type of a given triangle")
a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if a != b and b != c and a != c:
	print("This is a scalene triangle")
elif a == b and b == c:
	print("This is an equilateral traingle")
else:
	print("This is a isosceles triangle")

#________________________________________________________________________________________
#                                       Functions
#________________________________________________________________________________________
print(" ")
print("__________FUNCTIONS__________")

#Functions are a very benefitial tool and are great if you need to the same thing many times
#Lets make a function that finds the area of a triangle

print("Here is a function that finds the area of a triangle")
print("We will use the two numerical inputs from the input section")

def triangle_area(b,h):
	"""This finds the area of a triangle from two inputs"""
	area = (.5) * b * h
	return area

area = triangle_area(comp1_input, comp2_input)

print("The Area of your triangle is", area, "units")



#________________________________________________________________________________________
#                                       HELP
#________________________________________________________________________________________
print(" ") 
print("__________HELP__________")

print("All of the information on the help section can be found in the sourcecode")


#Knowing how to find help in Python is important
#dir() is short for directory
#using dir() can help the user find the way to the correct modules and tools in python

#say we want to learn about the pow() function 
#dir() #will give us the list of directories
#dir(__builtins__) #will allow us to look in the builtin directory 
#in there we can find the pow function 
#help(pow) #will allow us to see the syntax for the pow function 




#________________________________________________________________________________________
#                                       IMPORT
#________________________________________________________________________________________
print(" ")
print("__________IMPORT__________")
#sometimes we will need to import directories that we dont have
import math #this is the same as include<cmath> in c++
#now we can use pi
imp_test = 2 * math.pi
print(imp_test)
#If you need to find other librarys to import look online


#________________________________________________________________________________________
#                                       DATETIME
#________________________________________________________________________________________
print(" ")
print("__________DATETIME__________")

#The datetime module is great when we need to know the time
#It can also be used if we need to randomize something

#EX. 1
#Lets assign a time to a variable and then print it. 
import datetime
bdate = datetime.datetime(1998,9,30,23,59,59)
print(bdate)
#Now lets reformat this date
bdate_message  = "I was born on {:%A, %B %d, %Y}."
print(bdate_message.format(bdate))

#Now lets learn how to find the current time 
now = datetime.datetime.today()
print(now)

#Lets just print the microsecond
#This will be a great way to randomize
now = datetime.datetime.today()
print(now.microsecond)

#________________________________________________________________________________________
#                                       SETS
#________________________________________________________________________________________
print(" ")
print("__________SETS__________")

#Sets are used to organize data. 
#Sets are good when the order or frequency of the data is irrelevent

#EX. 1
example_set = set()
example_set.add(44)
example_set.add(False)
example_set.add(math.pi)
example_set.add("Hello World")

print(example_set)
#if not scripting in python you can just type the set name and it will print the set
#if you were to add 44 to the set again the set will still only disp one 44

#to see the number of elements in the set use the length function 
set_length = len(example_set)
print("Your set has", set_length ,"elements")

#to remove from the set use the remove function
example_set.remove(44)
print(example_set)

#if you use discard to remove somthing from a set it will not give an error
example_set.discard(44)

#EX. 2 
#Another way to make a set
example_set.clear()
example_set = set([44, False, math.pi, "Hello World"])
print(example_set)

#EX. 3
#Compairing sets is important 
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
print(odds.intersection(primes))
print(primes.intersection(evens))
print(2 in primes)
print(2 in odds)

#________________________________________________________________________________________
#                                       LISTS
#________________________________________________________________________________________
print(" ")
print("__________LISTS__________")

#Lists are a better way to organize data. 
#List are constructed with []

example_list = [1, 2, 3, 4, 5]
print(example_list)

example_list.append(6)
print(example_list)

#to index 
print(example_list[4])
print(example_list[-1])

#Slicing a list
#This includes the starting index but will not include the ending index
print(example_list[2:4])

#in python a list can contain many types of data
#A list can also contain another list
example_list2 = [1, "Hello World", True, 1.234, [1, 2, 3]]
print(example_list2)
print(example_list2[-1])

#merging a list is done by the following
example_list3 = example_list + example_list2
print(example_list3)

#use help(reverse) to learn how to reverse a list
#If optmizaiton is needed you can use a tuple 
#Tuples contain less data and can not be changes after creation

#________________________________________________________________________________________
#                                       DICTIONARIES
#________________________________________________________________________________________
print(" ")
print("__________DICTIONARIES__________")

#In python dictionaries are like classes in c++
#However these are not ortered 
example_dict = {"first_name":"John", "last_name":"doe", "date_of_birth":(1, 1, 1990)}
print(example_dict)
print(" ")
print("Printing with For loop")
for key in example_dict.keys():
	value = example_dict[key]
	print(key, "=", value)



#we can check the type by using type(example_dict)
#lets make another dictionary usind the dict constructor
example_dict2 = dict(first_name2="John2", last_name2="Doe2", date_of_birth2=(1, 1, 2000))
print(" ")
print(example_dict2)

#to add additional data use brackets
example_dict2["age"]= 19
example_dict2["height"]= 6
print(" ")
print(example_dict2)

#to index 
print(" ")
print(example_dict2['age'])
try:
	print(example_dict2['weight'])
except KeyError:
	print("This does not contain weight")


loc = example_dict2.get('weight', None)
print(loc)
print(" ")
print("Lets print another way")

for key, value in example_dict2.items():
	print(key, "=", value)

#To remove data from a dict use pop
#To remove all use clear


#________________________________________________________________________________________
#                                       FOR/WHILE LOOPS
#________________________________________________________________________________________
print(" ") 
print("__________FOR/WHILE_LOOPS__________")
#As you know for and while loops are very important 

#EX. 1: FOR LOOP
loop_test = 3
for loop_test in range(0,loop_test):
	print('For Loop')

#EX. 2: WHILE LOOP
while_test = True
while while_test is True:
	print('While Loop')
	while_test = False

#________________________________________________________________________________________
#                                       TIMEIT
#________________________________________________________________________________________
print(" ")
print("__________TIMEIT__________")

#Here we will learn about timeit 
#This is important when you need to optimize your code 

import timeit

list_time = timeit.timeit(stmt = "[1, 2, 3, 4]", number = 100000)
tuple_time = timeit.timeit(stmt = "(1, 2, 3, 4)", number = 100000)

print("List Time: ", list_time)
print("Tuple Time: ", tuple_time)



#________________________________________________________________________________________
#                                       TUPLES
#________________________________________________________________________________________
print(" ")
print("__________TUPLES__________")

#EX. 1
tuple1 = (1, 2, 3, 4)
tuple2 = (1,)
tuple3 = 1, 2, 3, 4
tuple4 = 1,

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

#EX. 2
#Lets make a list and a tuple that will print the same thing
#List: dog_age, dog_breed
print(" ")
print("Dog Survey")
list_survey = (5, "Boxer")

dog_age = list_survey[0]
dog_breed = list_survey[1]

print("Dog Age: ", dog_age)
print("Dog Breed: ", dog_breed) 

#now lets do the same thing with a tuple
tuple_survey = (5, "Boxer")
dog_age, dog_breed = tuple_survey

print("Dog Age: ", dog_age)
print("Dog Breed: ", dog_breed)

#As you can see doing this with tuples can be much easier 

#________________________________________________________________________________________
#                                       LOGGING
#________________________________________________________________________________________
print(" ")
print("__________LOGGING__________")

 
print("Logging file can be found in same folder as this script")

#Logging is similar to having a backup plan that can alert you if there is a problem
#Logging has 5 levels Debug, Info, Warning, Error, and Critical

import logging 

#create and config the logger 
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\desktop\\msc\\testlogger.Log",
				level = logging.DEBUG,
				format = LOG_FORMAT)
logger = logging.getLogger()

#Lets now test the logger.
logger.info("Test Message")

#More complex logger example can be found in the python examples folder

#________________________________________________________________________________________
#                                       MEMOIZATION
#________________________________________________________________________________________
print(" ")
print("__________MEMOIZATION__________")

#This is an important tool to use because it allows us to make programs run much faster.

fibonacci_cache = {}

def fibonacci(n):
	#We must first cache the value and then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	#compute the nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)

	#cache the calue and return it 
	fibonacci_cache[n] = value 
	return value 

for n in range(1, 11):
	print(n, ":", fibonacci(n))

#Lets do the same thing again using the lru_cache tool

from functools import lru_cache
@lru_cache(maxsize = 1000)

def fibonacci_test(y):
        if y == 1:
                return 1
        elif y == 2:
                return 1
        elif y > 2:
                return fibonacci_test(y-1) + fibonacci_test(y-2)


for y in range (1, 101):
	print(y, ":", fibonacci_test(y))


#________________________________________________________________________________________
#                                       RANDOM NUMBERS
#________________________________________________________________________________________
print(" ")
print("__________RANDOM_FUNCTION__________")

#Randomizing things is important for many uses we can learn how to do so here. 

#First lets print 4 random numbers 
import random

for i in range(0,4):
	print(random.random())


#Now lets print four random numbers that are brtween [3, 7)

def random_3_7():
	return 4*random.random()+3

for i in range (0,4):
	print(random_3_7())

#Now lets do the same thing using the uniform random generator 

for j in range(0,4):
	print(random.uniform(3,7))
#If you need more ways to make random numbers look in the dir(random)


#________________________________________________________________________________________
#                                       CSV FILES
#________________________________________________________________________________________
print(" ")
print("__________CSV_FILES__________")

#This is another way to store data 


