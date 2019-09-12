#••••••• Project 2

# Review
# Great! So far you have learned:

# how to write a function
# how to give a function inputs
# how to return values from a function
# what scope means
# Let’s practice these concepts again so that you won’t forget them!

#### 1.
# Define a function called repeat_stuff that takes in two inputs, stuff, and num_repeats.
# We will want to make this function print a string with stuff repeated num_repeats amount of times.
# For now, only put an empty print statement inside the function.

# 2.Outside of the function, call repeat_stuff.  
# You can use the value "Row " for stuff and 3 for num_repeats.

# 3.Change the print statement inside repeat_stuff to a return statement instead.
# It should return stuff*num_repeats.
# Note: Multiplying a string just makes a new string with the old one repeated! For example:
# "na"*6
# results in the string "nananananana".

# 4.Give the parameter num_repeats a default value of 10.4.
# Give the parameter num_repeats a default value of 10.

#5.Add repeat_stuff("Row ", 3) and the string "Your Boat. " together and
# save the result to a variable called lyrics.

# 6.Create a variable called song and assign it the value of repeat_stuff called with the singular input lyrics.

# 7.Print song.7.

def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)

def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)


#••••••• CODE CHALLENGE: PYTHON FUNCTIONS

### Introduction

# This lesson will help you review Python functions by providing some challenge exercises.
# As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output

# For example, a function that takes in a number and returns that number multiplied by 4 would look like:

def mult_by_four(number):
  multiplied = number * 4
  return multiplied

# 1.
#Write a function named average() that has two parameters named num1 and num2.
#The function should return the average of these two numbers.

# Write your average function here:
def average(num1, num2):
  the_average = (num1 + num2)/2
  return the_average

# Uncomment these function calls to test your average function:

print(average(1, 100)) #he average of 1 and 100 is 50.5
print(average(1, -1))  # The average of 1 and -1 is 0

# 2.
# Write a function named tenth_power() that has one parameter named num.
#The function should return num raised to the 10th power.

# Write your tenth_power function here:

def tenth_power(num):
  return (num**10)
# Uncomment these function calls to test your tenth_power function:

print(tenth_power(1)) # 1 to the 10th power is 1
print(tenth_power(0)) # 0 to the 10th power is 0
print(tenth_power(2)) # 2 to the 10th power is 1024

# 3.
# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

# Write your introduction function here:
def introduction(first_name, last_name):
  return(last_name+", "+first_name+" "+last_name)

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))   # should print Bond, James Bond
print(introduction("Maya", "Angelou")) # should print Angelou, Maya Angelou

# 4.
# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.
#••**** Raising a number to 0.5 will result in the square root of that number

# Write your square_root function here:
def square_root(num):
  return(num**0.5)
# Uncomment these function calls to test your square_root function:
print(square_root(16)) # should print 4
print(square_root(100)) # should print 10

# 5.
# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

# Write your tip function here:
def tip(total, percentage):
    return((percentage/100)*total)
    
# Uncomment these function calls to test your tip function:
print(tip(10, 25)) # should print 2.5
print(tip(0, 100)) # should print 0.0

# 6.

# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

# Write your win_percentage function here:

def win_percentage(wins, losses):
  return ((wins/(wins+losses))*100)

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5)) # should print 50
print(win_percentage(10, 0)) # should print 100

# 7.
# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

# Write your first_three_multiples function here:
def first_three_multiples(num):
  print(num)
  print(2*num)
  print(3*num)
  return(3*num)
  
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10) # should print 10, 20, 30, and return 30
first_three_multiples(0)  # should print 0, 0, 0, and return 0

# 8.
# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life.
# Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"

# Test this function with your name and your age!

def dog_years(name, age):
  return(name+", you are "+str(age)+" years old in dog years")

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16)) # should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))  # should print "Baby, you are 0 years old in dog years"

# 8.
# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.

# Write your remainder function here:
def remainder(num1, num2):
   return((2*num1)%num2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))# should print 2
print(remainder(9, 6))# should print 0

# 9.
# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d.
# The function should print 3 lines and return 1 value.
# First, the sum of a and b.
# Second, d subtracted from c.
# Third, the first number printed, multiplied by the second number printed.
# Finally, it should return the third number printed mod a.

# Write your lots_of_math function here:
def lots_of_math(a,b,c,d):
   print(a+b)
   print(c-d)
   print((a+b)*(c-d))
   return(((a+b)*(c-d))%a)
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4)) # should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1)) # should print 2, 0, 0, 0
 
