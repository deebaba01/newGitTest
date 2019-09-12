############### Project 4

####### Python Gradebook

# You are a student and you are trying to organize your subjects and grades using Python.
# Let’s explore what we’ve learned about lists to organize your subjects and scores.

# 1.
# Create Some Lists:
# Create a list called subjects and fill it with the classes you are taking:

# "physics"
# "calculus"
# "poetry"
# "history"

# 2.
# Create a list called grades and fill it with your scores:

98
97
85
88

# 3.
# Use the zip() function to combine subjects and grades.
# Save this zip object as a list into a variable called gradebook.

# 4.
#Print gradebook.
#Does it look how you expected it would?

# 5.
# Your grade for Computer Science class just came in! You got a perfect score, 100!

# After your definitions of subjects and grades but before you create gradebook,
# use append to add "computer science" to subjects and 100 to grades.

# 6.
# Your grade for visual arts just came in! You got a 93!
# After the creation of gradebook (but before you print it out), use append to add ("visual arts", 93) to gradebook.

# One Big Gradebook!

# 7.
# You also have your grades from last semester, stored in last_semester_gradebook.
# Create a new variable full_gradebook with the items from both gradebook and last_semester_gradebook.

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("compter science")
grades.append(100)
subjects.append("visual arts")
grades.append(93)
gradebook = zip(subjects, grades)
full_gradebook = list(gradebook) + last_semester_gradebook

print(list(full_gradebook))


########## Len's Slice

# You work at Len’s Slice, a new pizza joint in the neighborhood.
# You are going to use your knowledge of Python lists to organize some of your sales data.


# Make Some Pizzas

# 1.

# To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

# pepperoni
# pineapple
# cheese
# sausage
# olives
# anchovies
# mushrooms

# 2.

# To keep track of how much each kind of pizza slice costs, create a list called prices that holds:

# 2
# 6
# 1
# 3
# 2
# 7
# 2

# 3.

# Find the length of the toppings list and store it in a variable called num_pizzas.

# 4.
# Print the string "We sell X different kinds of pizza!", with num_pizzas where the X is.

# 5.
# Use zip to combine the two lists into a list called pizzas that has the structure:

[(price_0, topping_0), (price_1, topping_1), (price_2, topping_2), ...]
# In order to make the result of zip a list, do the following:

list(zip(____, ____))

# 6.
# Print pizzas.

# Does it look the way you expect?

##### Sorting and Slicing Pizzas

# 7.
# Sort pizzas so that the pizzas with the lowest prices are at the start of the list.

# 8.
# Store the first element of pizzas in a variable called cheapest_pizza.

# 9.
# A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE pizza!”
# Get the last item of the pizzas list and store it in a variable called priciest_pizza.

# 10.
# Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
# Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.

# 11.
# Print the three_cheapest list.

# 12.
# Your boss wants you to do some research on $2 slices.
# Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices.
# Print it out.

{

    toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

price = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza = zip(price, toppings)

pizza = (list(zip(price, toppings)))

pizza.sort()

cheapest_pizza = pizza[0]

priciest_pizza = pizza[-1]

three_cheapest = pizza[0:3]

print(three_cheapest)

num_two_dollar_slices = price.count(2)

print(num_two_dollar_slices)

}

######### CODE CHALLENGE: LISTS

## Introduction

# This lesson will help you review Python functions by providing some challenge exercises involving lists.
# As a refresher, function syntax looks like this:Introduction
# This lesson will help you review Python functions by providing some challenge exercises involving lists.
# As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output

# For example, a function that returns the sum of the first and last elements of a given list might look like this:

def first_plus_last(lst):
  return lst[0] + lst[-1]

# And this would produce output like:

>>> first_plus_last([1, 2, 3, 4])
5
>>> first_plus_last([8, 2, 5, -8])
0
>>> first_plus_last([-10, 2, 3, -4])
-14

####### Double Index

# double_index(lst, index)

# 1.
# Create a function named double_index that has two parameters named lst and index.
# The function should return a new list where all elements are the same as in lst except
# for the element at index, which should be double the value of the element at index of lst.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)

# After writing your function, un-comment the call to the function that we’ve provided for you to test your results.


{

    #Write your function here
def double_index(lst, index):
    if index >= len(lst):
    return lst
    else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

}

# Remove Middle

# remove_middle(lst, start, end)
# 2.
# Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

{

    def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

}

# More Than N

# more_than_n(lst, item, n)
# 3.
# Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

{
    #Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
}

# More Frequent Item

# more_frequent_item(lst, item1, item2)
# 4.
# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.

{
    #Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  elif lst.count(item2) >= lst.count(item1):
    return item2
  else:
    item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

}

# Middle Item

# middle_element(lst)
# 5.
# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element.
# If there are an even number of elements, the function should return the average of the middle two elements.

#•••••• The index of the middle element can be found by using len(lst)/2.
#•••••• However, division results in a float, and indices must be integers.
#•••••• You can cast that number to be an integer using int(len(lst)/2).
# For lists with an even number of indices, you will want the element at the index found above and also the element at index int(len(lst)/2) - 1

{
    #Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

}

# Append Sum

# append_sum(lst)
# 6.
# Write a function named append_sum that has one parameter named lst.
# The function should add the last two elements of lst together and append the result to lst.
# It should do this process three times and then return lst.
# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

{

    def append_sum(lst):
  lst_new = lst[-1]+lst[-2]
  lst.append(lst_new)
  lst_new1 = lst[-1]+lst[-2]
  lst.append(lst_new1)
  lst_new2= lst[-1]+lst[-2]
  lst.append(lst_new2)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

}

# Larger List

# larger_list(lst1, lst2)
# 7.
# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements.
# If both lists are the same size, then return the last element of lst1.

{
    #Write your function here
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  elif len(lst2) >= len(lst1):
    return lst2[-1]
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
}

# Combine Sort

# combine_sort(lst1, lst2)
#8.
# Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

{
    #Write your function here

def combine_sort(lst1, lst2):
  return sorted(lst1 + lst2)
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

}

# Append Size

#9.
# Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst.
# The function should then return this new list.
# For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.
# append_size(lst)

{
    #Write your function here
def append_size(lst):
  size = len(lst)
  lst.append(size)
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
}

# Every Three Nums

# every_three_nums(start)
#10.
# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive).
# For example, every_three_nums(91) should return the list [91, 94, 97, 100].
# If start is greater than 100, the function should return an empty list.

{
    def every_three_nums(start):
  lst =  []
  lst0 = [start]
  lst1 = start
  lst.append(lst1)
  lst2 = lst1 + 3
  lst.append(lst2)
  lst3 = lst2 + 3
  lst.append(lst3)
  lst.append(100)
  if start < 100:
      return lst
  elif start==100:
      return lst0
  else:
      return []

#Uncomment the line below when your function is done
print(every_three_nums(101))
}

# Alternatively:
{
#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

}
