from numpy import *

#Creating a multi DImensional aaray 
#Multiple arrays inside a big array
arr1 = array([
                [1,2,3,8,5,2],
                [4,5,6,4,7,9]
            ])

#Some attributes

#dtype - to know which type of data we are working with
print(arr1.dtype)

#ndim - gives us the dimension of the array
print(arr1.ndim)

#shape - Gives a tuple of the no of reows and columns 
print(arr1.shape)
#to get rows
print(arr1.shape[0])

#size -return the size of entire block rows*columns
print(arr1.size)

#to create a new array arr2 same as arr1 but in 1D
#Mans to convert a 2d array to a 1d array
#Flatten - flats the comple array
arr2= arr1.flatten()

#to convert an array from 1d to multi dimensional
#rehape -pass the number of rows and colums of final array
arr3 = arr2.reshape(4,3)
arr4 =arr2.reshape(2,2,3)

# To convert a 2D array into a matrix
#there is a function called as a matrix
m=matrix(arr1)
m= matrix('1,2,3 ; 4,5,6;7,8,9')
#the output will look similar but the difference is with the matrices we can perform more operations

#to get the diagonal elements of a matrix thers is a function
print(diagonal(m))   #returns a list

#To find minimum elemnt of a matrix
m.min()

#The addition of the two matrices is same
m3 = m1+m2

#To multiply the matrices 
m3 = m1 * m2
#this can only be done with matrices not with the arrays
