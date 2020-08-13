import string
from random import *
print ("")
print ("")
print ("Your Password Here")
print ("")
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(20, 20)))
print(password)

print ("")
print("")
print ("Instagram @ao_ozdil")
print ("GitHub @Aliosmanq")
print ("Facebook Ali Osman Oz")