'''
Author : Aditya Hegde
Description : Demo on while loop
Date :March 23rd, 2017
'''

print("\nBlock1:")
c = 5
while c !=0:
    print(c)
    c-=1

print("\nBlock2:")
c = 5
while c:
    print(c)
    c-=1

print("Testing with Break!!")
while True:
    resp = input()
    if int(resp) % 7 ==0:
        break
print("Infinite Loop Endnd")

#Break will terminates the inner most loop and transfers the execution to the first statement after the loop