supplies = ['pens', 'staplers', 'Yu-Gi-Oh GOAT staples', 'Nukes', 'Deodorant sticks']
for i in range(len(supplies)):
    print ('Index ' + str(i) + ' in supplies is: '+ supplies[i])
#multi assign from a list:
writetools, papertools, cards, weapons, hygiene = supplies
print (writetools)
print (papertools)
print (cards)
print (weapons)
print (hygiene)
#swap variables' values
a = 'AAA'
b = 'BBB'
a, b = b,a 
print (a)
print (b)
#easy way to increment - if test=1, then you can use test+=1 to increment it with one more
#if you need to find where in a list something is, use this: 
print (supplies.index('Nukes'))
#if there's no such value, this crashes, if there are duplicate values, this returns the first one 
#use append() to add something to the end of the list 
supplies.append('a credit card for spending on Yu-Gi-Oh GOAT staples')
print (supplies)
#use insert() to add something to the list wherever you damn well please
supplies.insert(1, 'money for spending on random shit')
print (supplies)
#to remove stuff from a list, use remove(), only the first instance found is removed
supplies.remove('money for spending on random shit')
print(supplies)
supplies.sort()
print(supplies)
supplies.sort(reverse=True)
print(supplies)
#that sort does not work if you have a list like [1,2,3, 'Alice', 'Bob']
#sort works normally by sorting Capitals first, then lowercase 
supplies.sort(key=str.lower)
print(supplies)