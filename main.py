import math
import decimal
from decimal import Decimal

# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"


# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------

def add_list(*nums):
    # nums comes in as a tuple with a spread operator. Thanks Josh H!
    sum = 0

    #https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
    #https://stackoverflow.com/questions/33311258/python-check-if-variable-isinstance-of-any-type-in-list
    #https://www.w3schools.com/python/python_datatypes.asp

    for num in nums:
        if isinstance(num, (int, float, complex)):
            sum += num
        else:
            return "NaN"
    return sum
# print(add_list(1,2,3,4,5,6))
# print(add_list(1,2,3,"a",5,6))

# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------

# https://stackoverflow.com/questions/38066836/python-best-way-to-remove-char-from-string-by-index
# https://www.digitalocean.com/community/tutorials/python-slice-string

def remove_ends(str):
    # print(str[::-1])
    return(str[1:-1:1])
    # return(str[1:(len(str)-1):1])
# print(remove_ends("abcdefg"))

# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------
#https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
#https://www.datacamp.com/tutorial/case-conversion-python
# for i in range(2,10):
#     print(i)

# test_str = "0123456789"
# print(test_str[0])
# print(test_str[-0])
# print(test_str[1])
# print(test_str[-1])

def is_palindrome(str):
    str_updated = str.replace(" ","").lower()
    # print(str_updated)
    # print (math.ceil(len(str_updated)/2))
    for i in range(math.ceil(len(str_updated)/2)):
        # print(f"i = {i}")
        # print(str_updated[i])
        # print(str_updated[-i-1])
        if str_updated[i] != str_updated[-i-1]:
            return "false"
    return "true"

    return(str_updated)
# print(is_palindrome('SEI Rocks'))
# print(is_palindrome('rotor'))
# print(is_palindrome('A nut for a jar of tuna'))
# print(is_palindrome(''))


# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

#-----------------------------------------------
# Solution goes here ->
#-----------------------------------------------

def is_prime(integer):
    if integer > 1:
        for i in range(2,integer): #start at 2, go to one less than integer
            # print(i, integer%i)
            if integer%i == 0:
                return "false"
        return "true"
    else:
        return "invalid entry, number must be greater than 1"

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(29))
print(is_prime(200))




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

# shopping_cart = [ 
#   {"item": "headphones", "price": 25},
#   {"item": "speakers", "price": 40 },
#   {"item": "microphone", "price": 70},
#   {"item": "lamp", "price": 15 },
#   {"item": "tower fan", "price": 35 },
# ]


#-----------------------------------------------
# Solution Goes Here ->
#-----------------------------------------------
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# https://chat.openai.com/c/a6543af9-ba5c-44d1-98fd-ecf732bd2cad
shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]

def total_checkout_cost(cart, state):
    total_cost=0
    for item in shopping_cart:
        total_cost += round(item["price"]*1.085, 2)
    if state == "HI" or state == "AK" or state=="TX" or state=="FL":
        total_cost += 10
    if state == "AL" or state == "MS" or state=="NV" or state=="IL":
        total_cost += 5
    return total_cost
print(total_checkout_cost(shopping_cart, "IL"))
print(total_checkout_cost(shopping_cart, "TX"))
print(total_checkout_cost(shopping_cart, "VA"))




# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not a number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------
# Solution Goes Here ->
#-----------------------------------------------
def fizz_buzz(i):
    if not isinstance(i, (int, float, complex)): print(f"{i} is not a Number")
    elif i%3==0 and i%5==0 : print("FizzBuzz")
    elif i%3==0 : print("Fizz")
    elif i%5==0 : print("Buzz")
    else: print(i)
fizz_buzz(10)
fizz_buzz(30)
fizz_buzz(18) 
fizz_buzz(22) 
fizz_buzz("ham_sandwich") 


# Challenge 7 - Chessboard Creator

# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chess_board(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
# And chess_board(3,7) should return this:


[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]

#The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'


#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------

def chess_board(row,col):
    
    start_O = []
    for space in range (col):
        if space%2==0 : start_O.append("O")
        else : start_O.append("X")
        space += 1

    start_X = []
    for space in range (col):
        if space%2==0 : start_X.append("X")
        else : start_X.append("O")
        space += 1

    result = []
    for r in range(row):
        if r%2==0: result.append(start_O)
        else: result.append(start_X)
    print(result)
        
chess_board(3,7)
chess_board(6,4)