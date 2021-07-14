'''
Random password generater using python
Author: Fawaz_jee
'''
#import the necessary modules!
import random
import string

print('welcome to auto Password generator!')
print('Your password is here below')

#define data
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-=&$%@#" 

#combine the data
all = lower + upper + numbers + symbols
length = 16
password = "" .join(random.sample(all, length))
print (password)