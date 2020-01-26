'''
Author : Aditya Hegde
Description : Demo on conditional statements
Date : March 23rd, 2017
'''
if True:
    print("This is True!")
if False:
    print("This is False!")

if bool("True"): #This will work similar to the first one
    print("This is True!")

if "Aditya": #Implicit Form
    print("There is Shama")

x=20
if x > 20:
    print("Greater!!")
elif x < 20:
    print("Smaller!!")
else:
    print("Equal!")
print("Done!")
print("Done!")
print("Done!")