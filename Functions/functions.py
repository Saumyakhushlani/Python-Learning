#Defining the Funtion :
def function_name():
    print("Hello")
    print("Good Morining")

#Calling the function
function_name()

def add(x,y):
    print(x+y)


add(5,4)

#As we know that the function can return a value as well
def multiply(x,y):
    return x*y

k= multiply(5,4)

#In pyhon we can return two values from a function
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d


add ,sub = add_sub(5,4)
