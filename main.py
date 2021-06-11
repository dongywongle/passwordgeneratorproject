'''
did some research and tried a different method than i was using, this is using secrets module and is, afaik,
more secure. still going to look to add complexity soon.
'''

import string
import secrets

reqlen = int(input("Please enter your desired password length (1-10 characters): "))

charpool = string.ascii_letters + string.punctuation
password = "".join(secrets.choice(charpool) for i in range(reqlen))

print(password)