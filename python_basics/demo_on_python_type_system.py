'''
Author : Aditya Hegde
Description : Demo on how python handles the variables / objects datatype during runtime
Date : March 27th, 2017
'''

def add(a,b):
    print(a + b)

add(10,20)
add(5.25,-1.25)
add('Shama', 'Aditya')
add([1, 2], [3, 4])

'''
1. No need to define data types explicitely
2. Easy way to implement polymorphism
'''

add("Hello",23.5) #This will throw an error

'''
There is no implicit object type conversion
'''