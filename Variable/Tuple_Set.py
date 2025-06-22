# ---- Tuple ----

#The tuple is almost similar to list it also have the collection of data but the differences
# Tuple is immutable means we cannot change the value of data

# To create tuple we use round bracket as the square brackets are used for creating lists

tup = (21,36,14,25)
tup[1]       #Returns 36
tup[1]=33    #Error as Tuple are immutable

# In built Funtion of tuples
tup.count(21)       #Counts the number of occurance of a number
tup.index           #Finds the index of a particular element

# when to use tuple
#When we don't want to change the values
# iteration in tuple is faster than in list as we are not changing the values

# ---- Set ----
# Set is a collection of unique elements
# To define set we use curly Braces

set ={22,25,1,4,28}
# The sequence of numbers inside can be random values as set uses the method of hash stores in the order of the frequency 
# If we add the same element in a set multiple times then it will be printed single time
# Insert the index in is not supported as the values are random
set[0] #Error

#In built functions of set
set.add
set.pop
set.update
