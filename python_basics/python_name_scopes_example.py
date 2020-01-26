
count = 0 #Global Variable

def show_count():
    print("Count:",count) #Local

def set_count(c):
    c = count
def set_count_global(c): #Enclosed Scope
    global count #This will help to assign new value to
    count = c #Local


