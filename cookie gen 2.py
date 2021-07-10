import requests
import re
import string
import os
import threading
import random
import time
from queue import Queue


outputfile = open("cookies.txt", "a")

x = 0
cookies = []
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
n = 0
print('[RECOMMENDED: Pick a high amount for better odds of generating a valid cookie]')
c = int(input("How many cookies do you want to generate? \n"))
print('Generating random cookies... please be patient! \n')
print('(these are not real cookies they are randomly generated cookies they will now be')
print('checked to find if any of them are valid which is a very low chance but still possible if done for long enough) \n')
letters = 'ABCDEF'

while x < c:


    cookies =  intro +  ''.join(random.choices(letters + string.digits, k=732))

    x = x + 1
    
    f = open('Cookies.txt', "a+")
    f.write(f'{cookies}\n')
    f.close()
    

if __name__ == '__main__':

    number_of_threads = 900
    print_lock = threading.Lock()
    cookie_queue = Queue()
    url = 'https://accountinformation.roblox.com/v1/birthdate'

        
    cookie_queue.join()

outputfile.close()

t1 = time.time()
print('Done! IF any valid cookies were found, they have been added to the hits.txt file!')
input("Press enter to exit.")




 
