# Module import
from string import ascii_uppercase as uppercase
from string import ascii_lowercase as lowercase
from string import digits
from string import punctuation
from random import choice

# Start 

def Gen(mode, lenght):
    count = 0
    password = ''
    if mode == 1:
        chars = uppercase + lowercase + digits + punctuation
        while count != lenght:
            password += password.join(choice(chars))
            count += 1
        return password
    elif mode == 2:
        chars = uppercase + lowercase + digits
        while count != lenght:
            password += password.join(choice(chars))
            count += 1
        return password
    else:
        print('That mode dont exist')

if __name__ == "__main__":
    print(f'Mode 1 (With Punctuation): \n{Gen(1, 15)} \n\nMode 2: (Without Punctiation)\n{Gen(2,15)}')
