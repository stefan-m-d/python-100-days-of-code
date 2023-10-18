#code doesn't work if the below line isn't in it - this imports a Python built in function
#alternatively, use the following command: from random import * and this way, you can form your commands as just randint(x,y) instead of having to use random.randint
import random
#user inputs how many songs they have in their playlist
print ('Please enter how many songs your playlist has')
playlist=input()
#convert to number
number=int(playlist)
for num in range(number+1):
    print (random.randint(1, number+1))