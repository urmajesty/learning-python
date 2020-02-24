#import is how I add modules to my script
#argv is the argument variable.  It just holds the args.
from sys import argv

#line 6 unpacks the argments and passes them to "filename" 
script, filename = argv

#line 9 opens the file 
txt = open(filename)

#line 7 prints a message
#line 8 reads the file 
print(f"Here's you file {filename}:")
print(txt.read())
# print(txt.close())

# #line 17 is part of the input function on line 18
print("Type the filename again:")
file_again = input("> ")

# #line 21 opens the file again
txt_again = open(file_again)

# #line 24 prints the text again
print(txt_again.read())