#The data stored in the variable is temporary
#But what if we want to have the parmanent data / Data for long time
#One of the way for doing this is Relational databases but that's the complex one
#the other way to do this is by creating a file and storing data in it

#How to open a txt file with data in code so as to use it in code?
#For that we have some inbuilt function

#open Function
f = open("myfile.txt",'r')
#it takes two parametres here the first one the file name itself and the second thing is mode
#Mode here refers to the do you want to read a file or write a file
#to read only we write r and for writeing we write w 

print(f)