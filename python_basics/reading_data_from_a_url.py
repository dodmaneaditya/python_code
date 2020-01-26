'''
Author : Aditya Hegde
Description : Program to fetch the contents of a HTML page using urlopen() function

'''
#from reading_data_from_a_url import * this will import all the function bodies available in a module
import sys
from urllib.request import urlopen
def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
#print(story_words)
#print(line_words)

#for w in story_words:
#    print(w)
##print(__name__) #this will print the module or file name, that too only once (first time)
#if __name__ =='__main__': # __name__ is a special attribute used in Python which evaluates to __main__ or the given name of the module
#    url_read()

"""
As a html protocol alwaya passes the values in byte code format, we should convert that 'utf-8' using decode()
"""



def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])