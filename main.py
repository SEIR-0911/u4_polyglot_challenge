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
print("======== Challenge 1: add_List ===========")

def add_list(*listNum):
    if not listNum:
        print('No number to add')
        return 0

    result_sum = 0
    
    for num in listNum:

            if not isinstance(num, (int, float)):
                return "NaN"
            result_sum += num
    return result_sum
result0 = add_list()
result1 = add_list(1)
result2 = add_list( 1,50,1.23)
result3 = add_list( 7,-12)
result4 = add_list( "peanut_butter", "marshmellow_fluff")

print(result0)
print(result1)
print(result2)
print(result3)
print(result4)

#-----------------------------------------------

# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
print("======== Challenge 2: remove_ends ===========")

def remove_ends(str):
    result = ""
    if len(str) < 3 : return ""
     #Start from 1 cut 0 out until -1
    result = (str[1:-1])
    return result

strResult0 =  remove_ends('')
strResult1 =  remove_ends('Hello World')  

print(strResult0)
print(strResult1)

#-----------------------------------------------

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
print("======== Challenge 3: is_palindrome ===========")

def is_palindrome(str):
    if(len(str)<=1): True
    str= str.lower().replace(" ", "")
    reverse_str_lower_no_space = str[::-1]
    return  reverse_str_lower_no_space == str
     
test_str0 = is_palindrome('')
test_str1 = is_palindrome('b')
test_str2 = is_palindrome('book')
test_str3 = is_palindrome('W ow')

print(test_str0)
print(test_str1)
print(test_str2)
print(test_str3)
#-----------------------------------------------

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
print("======== Challenge 4: is_prime ========")

def is_prime(num):
    if(num<2): return False
    for i in range(2,num):
        if(num%i==0 ):
            return False
    return True

my_num0 = is_prime(0) 
my_num00 = is_prime(2) 
my_num1 = is_prime(211) 
my_num2 = is_prime(212) 

print("is prime?",my_num0)
print("is prime?",my_num00)
print("is prime?",my_num1)
print("is prime?",my_num2)
#-----------------------------------------------

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
print("======== Challenge 5: total_checkout_cost ========")

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]
def total_cost(cart,homestate):
    shipping_10 = ['HI', 'AK', 'TX', 'FL']
    shipping_5 = ['AL', 'MS', 'NV', 'IL']
    total=0
    for item in cart:
        total += item["price"]
        total += total*0.085 #add Tax
    #Add Shipping
    if homestate in shipping_10:
        print('$10 Shipping')
        total +=10
    elif homestate in shipping_5:
        print('$5 Shipping')
        total +=5
    else:
        print('Shipping is free!')
    return total

total_price = total_cost(shopping_cart,'TX')

print(total_price)
#-----------------------------------------------

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
print("======== Challenge 6: fizz_buzz ========")

def fizz_buzz(number):
    if not isinstance(number, int):
        return f"{number} is not a number"
    array_num = []
    for i in range(1, number+1):
        if(i%15==0):
             array_num.append('FizzBuzz')
        elif(i%3==0):
             array_num.append('Fizz')
        elif(i%5==0):
            array_num.append('Buzz')
        else:
             array_num.append(i)
    return array_num

fizz_buzz_print = fizz_buzz(50)
print(fizz_buzz_print)

#-----------------------------------------------

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
print("======== Challenge 7: Chessboard Creator ========")

def chess_board(rows, columns):
    board = []

    for i in range(rows):
        row = []
        for j in range(columns):
            if (i + j) % 2 == 0:
                row.append("O")
            else:
                row.append("X")
        board.append(row)

    return board
   
my_board = chess_board(6,4)
my_board2 = chess_board(3,7)
print(my_board)
print(my_board2)

#-----------------------------------------------
