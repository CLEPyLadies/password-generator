import string
import random


#get a list of all the different type of characters you can use in your password
DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER  = string.ascii_uppercase
SYMBOLS = string.punctuation

# combines all the character arrays above to form one array 
COMBINED_LIST = DIGITS + UPPER + LOWER + SYMBOLS 

#get the word you want to use as your password
WORDS = input("What word would you like to use? ")
#split it into a list of string characters

splitword = [char for char in WORDS]

#substitute a random character in your word with a random character from the combined list
for index, x in enumerate(splitword):
    if random.randint(0, 1):
        splitword[index] = random.choice(COMBINED_LIST)
  
#put the characters back together in your password
password = "".join(splitword)
            
# print out password 
print(password)
