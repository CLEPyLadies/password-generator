import string
import random
import array

# maximum length of password needed 
# this can be changed to suit your password length 
PASS_LEN = int(input("How long of a password would you like? "))

DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER  = string.ascii_uppercase
SYMBOLS = string.punctuation

# combines all the character arrays above to form one array 
COMBINED_LIST = DIGITS + UPPER + LOWER + SYMBOLS 

# randomly select at least one character from each character set above 
rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPPER) 
rand_lower = random.choice(LOWER) 
rand_symbol = random.choice(SYMBOLS) 

# combine the character randomly selected above 
# at this stage, the password contains only 4 characters but  
# we want a 12-character password 
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

    
# now that we are sure we have at least one character from each 
# set of characters, we fill the rest of 
# the password length by selecting randomly from the combined  
# list of character above. 
for x in range(PASS_LEN - 4): 
    temp_pass = temp_pass + random.choice(COMBINED_LIST) 
    # convert temporary password into array and shuffle to  
    # prevent it from having a consistent pattern 
    # where the beginning of the password is predictable 
    temp_pass_list = array.array("u", temp_pass) 
    random.shuffle(temp_pass_list) 

# now go through the array to print out password
password = "" 
for x in temp_pass_list: 
    password = password + x 
            
# print out password 
print(password) 
