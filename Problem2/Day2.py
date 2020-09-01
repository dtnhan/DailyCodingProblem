'''
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of 
all the numbers in the original array except the one at i

'''
def product(list0):
    list1 = [1] * len(list0)
        
    for i in range(len(list0)):
        list1[i] = 1
        for j in range(len(list0)):
            if i != j:
                list1[i] = list1[i] * list0[j]
                
            
    print(list1)
    
    
# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
product(lst)
