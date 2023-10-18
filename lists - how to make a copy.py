def test(list):
    list.append('zdr')
    
list1= [1,2,3]
test(list1)
print(list1)

#this always modifies the same list. Now, to do a brand new copy, you need import copy

import copy 

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1]=42 
print(cheese)
print(spam)