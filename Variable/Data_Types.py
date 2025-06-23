#------------ Types of data type-------------
#None
#Numeric
#Lists
#Tuple
#Set
#String
#Range
#Dictionary

#------None-------
# When we have a variable in that variable is not assigned with any value then it is called none

#-----Numeric------
# Numeric itself has four types Int, Float, complex, bool
complex =5+9j
int =5
float=3.33
bool =True

# Can we do the interconversion between the types of numeric
#Yes
a=3.33
b=int(a)          #b=3
c=5
e=float(c)        #e=5.00
d=complex(b,c)    #d=3+5j
# This int function will convert any value to an integer

# In python we don't have a char type of data Because we can create a single character string
# So in place of char we have string as a type

#--------- Range ---------
# When we iterate between values we can use rage
range (10)
list( range(10) )    #[1,2,3,4,5,6,7,8,9]

range(2,10,2)        # Start to 2 goes till 8 and the differences is 2


#---------- Mapping or Dictionary ----------
# In dictionary for every value we will assign a key
# Used in bigger data so that we can identify each value with a key
# The key should be unique
d = {'saumya':'samsung','navin':'oneplus','raj':'apple'}

# To get keys only use
d.keys()
# To get values only use
d.values()

# To get a value through key
d["keyname"]
d['navin']
#or
d.get('keyname')