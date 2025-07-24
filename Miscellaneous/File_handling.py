# The data stored in a variable is temporary.
# But what if we want to have the permanent data / data for a long time?
# ✅ One way: use Relational Databases (but that’s complex)
# ✅ Other way: create a file and store data in it (simple!)

# -------------------------------------------------
# 🔹 How to open a text file with data in code so as to use it in code?
# For that we have an inbuilt function: open()

# open() function takes 2 parameters:
# 1. File name
# 2. Mode (r = read, w = write, a = append)

#This works in the lastest version
with open(file, 'r'  , encoding="UTF-8") as f:
    content = f.read()
    print(content)

# Example: open file in READ mode
f = open(file, 'r'  , encoding="UTF-8")   # open a file named myfile.txt in read mode
print(f)                      # prints file object info (not content)

# To print the entire file content
print(f.read())               # prints the full data in the file

# -------------------------------------------------
# To print only the first line
f = open('myfile.txt', 'r')
print(f.readline())           # prints first line
# Every time we call readline(), it moves the internal pointer to next line
print(f.readline())           # prints second line

# If we pass n inside readline(), it will print only n characters of that line
f = open('myfile.txt', 'r')
print(f.readline(4))          # prints only 4 characters from the first line

# -------------------------------------------------
# 🔹 Writing data to a file
# Open a file in WRITE mode
k = open('abc.txt', 'w')      # if abc.txt does not exist, it will create it
k.write("Saumya")             # writes Saumya to the file
k.write(" Kumar")             # writes Kumar right after Saumya
k.close()

# ⚠️ Note: using 'w' mode will overwrite previous content every time

# -------------------------------------------------
# 🔹 Appending data to a file
k = open('abc.txt', 'a')      # open in append mode
k.write("\nNew Line Added")   # this will append instead of overwrite
k.close()

# -------------------------------------------------
# 🔹 Copying data from one file to another
source = open('myfile.txt', 'r')
destination = open('copy.txt', 'w')
for data in source:
    destination.write(data)
source.close()
destination.close()
# Now copy.txt will have the same content as myfile.txt

# -------------------------------------------------
# 🔹 Working with binary files (e.g., images)
# Open an image in READ BINARY mode
f_img = open('pig.jpg', 'rb')

# Create another file to copy image
f_img_copy = open('mypic.jpg', 'wb')

# Read and write binary data
for chunk in f_img:
    f_img_copy.write(chunk)

f_img.close()
f_img_copy.close()
# ✅ Now mypic.jpg is an exact copy of pig.jpg

# -------------------------------------------------
# Modes recap:
# r  -> read (file must exist)
# w  -> write (creates new file or overwrites existing)
# a  -> append (creates new file or appends to existing)
# rb -> read binary
# wb -> write binary
