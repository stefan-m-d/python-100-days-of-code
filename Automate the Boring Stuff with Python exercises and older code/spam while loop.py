print ('Please enter a total to calculate')
Inputtotal=input()
integer=int(Inputtotal)
total=0
for num in range(integer):
    total=total+num
print ('Here is your total: ' + str(total))