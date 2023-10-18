print ('Please enter a total to calculate')

#ask user for input
Inputtotal=input()
#transform input to desired value type - int in this case 
integer=int(Inputtotal)

total=0

for num in range(integer):

    total=total+num

print ('Here is your total: ' + str(total))