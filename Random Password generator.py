
#Modules
import random
import string


#Welcome Message
print('Hi There! Welcome to Password Generator')


#The length of the password
len = int(input('Enter the length of the pasword: '))


#Define the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


#Combining the data
all = lower + upper + num + symbols


#Randomizing
temp = random.sample(all,len)


#The Password
password = ''.join(temp)

#The output
print(password)