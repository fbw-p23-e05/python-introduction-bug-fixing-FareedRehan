### Task 1 - fix the FizzBuzz
#### Your :heavy_plus_sign: Task is to fix program non-working correctly.
#### The FizzBuzz problem:  
#### For all integers between 1 and 99 (include both):  
#- print 'fizz' for multiples of 3,
#- print 'buzz' for multiples of 5, 
#- print 'fizzbuzz' for multiples of 3 and 5.

three_mul = 'fizz' #Bug-1 ('fizz')
five_mul = 'buzz'
num1 = 3
num2 = 5 #Bug (num2 = 4)
max_num = 100
   
for i in range(1, max_num): #Bug-2 = (1,max_number)
    # % or modulo division gives you the remainder 
    if i % num1 == 0 and i % num2 == 0: #Bug-6 (elif i % num1 == 0 and num2 == 0)
        print(i, three_mul + five_mul)
    elif i % num1 == 0: #Bug-3 (if i%num1 = 0:)
        print(i, three_mul) #Bug-4 (i, three_mul)
    elif i % num2 == 0:
        print(i, five_mul) #Bug-5 (i, five_mul)
        
### :heavy_plus_sign: Task 2 - summing integers
#Your task is to fix program non-working correctly.
#The problem:  
  #- sum integers from 1 to 5 using while loop
  #- calculate what result should be and what you get after running the program 

n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number # Bug (add sum to number)
    number = number + 1
print("Sum =", sum)

## :heavy_plus_sign: Task 3 - summing integers with range()
#Your task is to fix program non-working correctly.
#The problem:  
  #- sum integers from 1 to 5 using `range()` function
  #- calculate what result should be and what you get after running the program   

n = 5
sum = 0
for num in range(1, n +1): # Bug (range(n))
    sum += num
print("Sum =", sum)

### :heavy_plus_sign: Task 4 - printing in loops
#Your task is to fix program non-working correctly.
#The problem:  
  #- there are 4 short programs with loops, that should print some numbers, but they don't work at all!  

#### Program no. 1 with the bug:  
for x in range(3): #Bug (for x in range(3))
    print(x)

#### Program no. 2 with the bug:
#### Option 1
for j in range(5): # Bug (range(5))
    print("This is loop number", j) #Bug (print("This is loop number j"))
    
#### Program no. 3 with the bug:
x = 10 # Bug (x was not defined)
while x > 0:
    print(x)
    x -= 1

#### Program no. 4 with the bug: 
countdown = 5 # Bug (countdown = 0)
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")

### :heavy_plus_sign: Task 5 - summing three integers

#Your task is to fix program non-working correctly.
#The problem:  
  #- sum the three prompted integers
  #- however, if two values are equal sum should be zero
  #- calculate what result should be and what you get after running the program 
   
#### Option 1
x = int(input("First number: ")) # Bug (int was not added)
y = int(input("Second number: "))
z = int(input("Third number: ")) # Bug (extra bracket)

if x == y or y == z: # Bug (x = y = z:)
    result = 0
    print("Calculated sum is: ", result)
else:
    sum = x + y + z
    print("Calculated sum is ", sum) # Bug (result)

#### Option
if x == y or y == z or x == z: # Bug (x = y = z:)
    result = 0
else:
    result = x + y + z
print("Calculated sum is: ", result) # Bug (result)

### :heavy_plus_sign: Task 6 - summing two integers
# Your task is to fix program non-working correctly.
# The problem:  
#- sum the two prompted integers
#- however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20  
#- calculate what result should be and what you get after running the program  

#### Program with bugs:  
#### Option 1
x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y
if result >= 15 and result <= 20:
    sum = 20
    print("calculated sum is: ", sum)
else:
    print("Calculated sum is: ", result)
    
#### Option 2
x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y
if result >= 15 and result <= 20:
    result = 20
print("Calculated sum is ", result)

### :heavy_plus_sign: Task 7 - swapping variables
# Your task is to fix program non-working correctly.
# The problem:  
#- prompt two values and assign them to variables `a` and `b`
#- write the Python program to swap these two variables
#- calculate what result should be and what you get after running the program   
#>Remark: **don't use** "fast" swapping available in Python:

# Program with bugs:  
### Option 1
a = input("First value: ") # Bug (int)
b = input("Second value: ")

print("Before swapping: a =", a, "b =", b)

temp = a
a = b
b = temp # Bug (b = temp)

print("After swapping: a =", a, "b =", b)

### Option 2
a = input("First value: ") # Bug (int)
b = input("Second value: ")

print("Before swapping: a =", a, "b =", b)

a, b = b, a

print("After swapping: a =", a, "b =", b)

    
### :heavy_plus_sign: Task 8 - max and min values
# Your task is to fix program non-working correctly.
# The problem:  
#- prompt three float numbers and determine the largest and the smallest one
#- calculate what result should be and what you get after running the program  

#### Program with bugs:  

x = float(input("First number: ")) # Bug (float), Bug (==)
y = float(input("First number: "))
z = float(input("First number: "))

print("The maximum value is: ", max(x, y ,z)) # Bug (max is missing)
print("The minimum value is: ", min(x, y ,z)) # Bug (abs replaced by min)

### :heavy_plus_sign: Task 9 - conversion
#Your task is to fix program non-working correctly.
#The problem:  
#- prompt value from the user and assign it to some variable  
#- if given value is 0 (zero) convert it to `False` and if given value is 1 convert it to `True`
#- display results  

#### Program with bugs:
x = (input("Type your value: "))

if x == "0": # Bug (if x = 0)
    x = False # Bug (false)
elif x == "1":  # Bug (if x = 1)
    x = True    # Bug (true)
else:
    pass
print("Your entered value is now:", x)

### :heavy_plus_sign: Task 10 - divisible number
#Your task is to fix program non-working correctly.
#The problem:  
#- accept (prompt) two integers values from the user  
#- check whether a first number is divisible by second number and vice versa  
#- display results  

#### Program with bugs:  
### Option 1
x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", (x / y))
elif y % x == 0:
    print("Second number is divisible by first number, result =", (y / x))
else:
    print("Numbers are non-divisible!")
    
### Option 2
x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", int(x / y))
elif y % x == 0:
    print("Second number is divisible by first number, result =", int(y / x))
else:
    print("Numbers are non-divisible!")