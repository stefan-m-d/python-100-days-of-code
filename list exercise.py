#lists are started with [] and indexed with a number, like so 
#this is a list
test=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
print (test[3])
#this prints out the second to last indexed item of the list
print (test[-2])
#this prints a slice of the list - several items from the list based on the index, all of them are no including, so this prints out indexes 2,3 and 4
print (test[1:5])
#reassign items in lists in either single values or slices like so:
test[0]='EDNO'
test[1:3]=['DVE', 'TRI', 'CHETIRI']
print (test[0])
print (test[0:4])
#if you want ot print out all items in a list - from the beginning of it or until its end, do these:
print (test[:3])
print (test[2:])
#since we have 2 items in the list that correspond to four - chetiri and four, let's delete one of them:
del test[4]
print (test)
# what does list do again?
print (list(test))
print (list('ZDR KP'))
# in and not in functions search for a string in a list
if 'ZDR' in ['ZDR', 'BEPCE', 'KP', 'MALKO KOTE', 'SEKS IMA LI?']:
    print ('*clears throat* zdr')