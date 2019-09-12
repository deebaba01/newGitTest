#••••••• Project 3

# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
# Sal wants to make sure that every single one of his customers has the best, and
# most affordable experience shipping their packages.
# In this project, you’ll build a program that will take the weight of a package and
# determine the cheapest way to ship that package using Sal’s Shippers.
# Sal’s Shippers has several different options for a customer to ship their package.
# They have ground shipping, which is a small flat charge plus a rate based on the weight
# of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t
# charged for weight.
# They recently also implemented drone shipping, which has no flat charge, but the rate based
# on weight is triple the rate of ground shipping.

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

# Finding the Cheapest Shipping Method
flat_charge_g = 20.00
cost_of_prem_g_flat_charge = 125.00

def cost_of_g_shipping(weight):
  if (weight <= 2):
    cost_of_shipping = weight*1.5 + flat_charge_g
    return cost_of_shipping
  elif (weight >2) and (weight <= 6):
    cost_of_shipping = weight*3.0 + flat_charge_g
    return cost_of_shipping
  elif (weight >6) and (weight <= 10):
    cost_of_shipping = weight*4.0 + flat_charge_g
    return cost_of_shipping
  else:
    return return ("The cheapest way to ship a "+str(weight)+" pound package is using premium ground shipping and it will cost "+str(cost_of_prem_g_flat_charge)+".")

  print(cost_of_g_shipping(8.4))
  
 
  
  flat_charge_d = 0.00

def cost_of_d_shipping(weight):
  if (weight <= 2):
    cost_of_shipping = weight*4.5 + flat_charge_d
    return cost_of_shipping
  elif (weight >2) and (weight <= 6):
    cost_of_shipping = weight*9.0 + flat_charge_d
    return cost_of_shipping
  elif (weight >6) and (weight <= 10):
    cost_of_shipping = weight*12.0 + flat_charge_d
    return cost_of_shipping
  else:
    cost_of_shipping = weight*14.25 + flat_charge_d
    return cost_of_shipping

  print(cost_of_d_shipping(1.5))

# Write a program that asks the user for the weight of their package and then
# tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

#### Finding the Cheapest Shipping Method
# 1.
# First off, we need to know how much it costs to ship a package of given weight by normal ground shipping.
# Write a function for the cost of ground shipping. This function should take one parameter, weight, and return
# the cost of shipping a package of that weight.

# 2.
# A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:
# 8.4 lb×$4.00+$20.00=$53.60
# Test that your ground shipping function gets the same value.

# 3.
# We’ll also need to make sure we include the price of premium ground shipping in our code.
# Create a variable for the cost of premium ground shipping.
# Note: this does not need to be a function because the price of premium ground shipping does not
# change with the weight of the package.

# 4.
# Write a function for the cost of drone shipping. This function should take one parameter, weight,
# and return the cost of shipping a package of that weight.

# 5.
# A package that weighs 1.5 pounds should cost $6.75 to ship by drone:
# 1.5 lb×$4.50+$0.00=$6.75
# Test that your drone shipping function gets the same value.

# 6.
# Using those two functions for ground shipping cost and drone shipping cost, as well as the cost of premium ground shipping,
# write a function that takes one parameter, weight and prints a statement that tells the user

# The shipping method that is cheapest.
# How much it would cost to ship a package of said weight using this method.

## Hint
# Think about the control flow of this function. You want to:

# Check if a method is cheaper than the other two methods.
# If it isn’t, check if one of the other two methods is cheaper than the other.
# If that isn’t, then the final untested method must be the cheapest.
# If any of these conditions are met, you should calculate the cost of that method and print out a statement instructing the user to use that method and what it will cost.

# Here’s an example of what your function should do. With an input of:

cheapest_shipping(17)```
It should return something like:

# You should ship using ground shipping, it will cost $100.75```

# 7.
# Great job! Now, test your function!
# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
# What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

#Hint
# The cheapest way to ship 4.8 pound package is using ground shipping and it will cost $34.40.
# The cheapest way to ship a 41.5 pound package is using premium ground shipping and it will cost $125.00.



    
prem_g_shipping = 125
flat_charge_g = 20
flat_charge_d = 0
def c_of_g_shipping(weight):
    if weight <= 2:
        g_c = weight * 1.50 + flat_charge_g
        return g_c
    elif weight <= 6:
        g_c = weight * 3.00 + flat_charge_g
        return g_c
    elif weight <= 10:
        g_c = weight * 4.00 + flat_charge_g
        return g_c
    else:
        g_c = weight * 4.75 +  flat_charge_g
        return g_c


def c_of_d_shipping(weight):
    if weight <= 2:
        d_c = weight * 4.50 + flat_charge_d
        return d_c
    elif weight <= 6:
        d_c = weight * 9.00 + flat_charge_d
        return d_c
    elif weight <= 10:
        d_c = weight * 12.00 + flat_charge_d
        return d_c
    else:
        d_c = weight * 14.25 + flat_charge_d
        return d_c

def c_of_cheapest_shipping(weight):
    if c_of_g_shipping(weight) < (c_of_d_shipping(weight) and prem_g_shipping):
        print("You should ship using ground shipping, it will cost $"+str(c_g))
        print("The cheapest way to ship a "+str(weight)+" pound package is using ground shipping and it will cost $"+ str(c_g)+".")
        return c_g

    elif c_of_d_shipping(weight) < (c_of_g_shipping(weight) and prem_g_shipping):
        print("You should ship using ground shipping, it will cost $"+str(c_d)+".")
        print("The cheapest way to ship a "+str(weight)+" pound package is using ground shipping and it will cost $"+ str(c_d)+".")
        return c_d
    else:
        print("You should ship using premium ground shipping, it will cost $"+str(prem_g_shipping)+".")
        print("The cheapest way to ship a "+str(weight)+" pound package is using premium ground shipping and it will cost $"+ str(prem_g_shipping)+".")
        return prem_g_shipping
                    
                    
                    
c_of_cheapest_shipping(56)                    


###### Code Challenge: Control Flow

# This lesson will help you review Python functions by providing some challenge exercises involving control flow.
# As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output
# or example, a function that takes a number and checks to see if it is greater than ten would look like this

def greaterThanTen(number):
  if number > 10:
    return True
  else:
    return False

# And this would produce output like:

>>> greaterThanTen(20)
True
>>> greaterThanTen(-10)
False
>>> greaterThanTen(10)
False

####### When you’re ready to do this series of short function challenges, continue on to the rest of the lesson!

## In Range

in_range(num, lower, upper)

# 1.
# Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper.
# Otherwise, return False.

# Write your in_range function here:
def in_range(num, lower, upper):
  if (num >= lower) and (num <= upper):
    return True
  else:
    return False
#Uncomment these function calls to test your in_range function
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

## Movie Review

movie_review(rating)

# 2.
#Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!".
# If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:

def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

## Twice as large
twice_as_large(num1, num2)

# 3.
# Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

# Write your twice_as_large function here:

def twice_as_large(num1, num2):
  if num1 > 2*num2:
    return True
  else:
    return False


# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

## Power
large_power(base, exponent)

# 4.
# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

# Write your large_power function here:

def large_power(base, exponent):
  if base**exponent > 5000:
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

## Divisible By Ten
divisible_by_ten(num)

# 5.

# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise.
# Consider how to use modulo (%) to check for divisibility.

# Write your divisible_by_ten function here:

def divisible_by_ten(num):
  if num%10==0:
    return True
  else:
    return False
    
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

## Max Number
max_num(num1, num2, num3)

# Create a function called max_num() that has three parameters named num1, num2, and num3.

# The function should return the largest of these three numbers.
# If any of two numbers tie as the largest, you should return "It's a tie!".


#6.
#Write your max_num function here:

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie"

#•••• Alternatively

# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > (num2 and num3):
    return num1
  elif num2 > (num2 and num3):
    return num2
  elif num3 > (num1 and num2):
    return num3
  else:
    return "It's a tie!"


# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie"

### ## Over Budget
over_budget(budget, food_bill, electricity_bill, internet_bill, rent)

# 7.

# Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.
# The function should return True if budget is less than the sum of the other four parameters.
# You’ve gone over budget! Return False otherwise.

# Write your over_budget function here:

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

### Always False
always_false(num)

# 8.
# Create a function named always_false() that has one parameter named num.

# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter
# what number is stored in num.
# An if statement that is always false is called a contradiction.
# You will rarely want to do this while programming, but it is important to realize it is possible to do this.


# Write your always_false function here:

def always_false(num):
  if (num > 5) and (num < 5):
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))

### Not Equal
not_sum_to_ten(num1, num2)

# 9.
# Create a function named not_sum_to_ten() that has two parameters named num1 and num2.
# Return True if num1 and num2 do not sum to 10. Return False otherwise.

# Write your not_sum_to_ten function here:

def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
    return True
  else:
    return False
  
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

### Same Name
same_name(your_name, my_name)

# 10.
# Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

# Write your same_name function here:

def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False
