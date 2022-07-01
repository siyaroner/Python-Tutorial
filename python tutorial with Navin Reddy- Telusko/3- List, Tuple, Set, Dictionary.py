# Lists are mutable so it means you can change the value in the list

##                PYTHON COLLECTIONS (ARRAYS)
##-List : is a collection which is ordered and changeable. Allows duplicate members                                                                                                             (  )   
##-Tuple : is a collection which is ordered and uncahngeable. Allows duplicate members                                                                                                      [   ]   
##-Set : is a collection which is unordered, unchangeable (* but you can remove items and add new items), and unindexed. No duplicate members.         {   }   
##-Dictionary : is a collection which is ordered (in py 3.7 is ordered.), and changeable. No duplicate members.                                                                     {    }  


                                                ##                      LISTS        
nums = [2, 323, 32,44,67,2]
nums[3]
nums[-1]
names = ['siyar','Furkan,' 'Biyo', 'Leyla']
values = [3.14, 'Siyar', 54]
mil = [nums, names]
mil
nums.append (85)         # append is using for add the value in parentheses into end of the list
nums.copy ()                 # it's using for copying value
nums.count (2)              # it is counting the object that stated in parentheses
nums.extend([3, 4, 64]) #extend is using for add multiple value
nums.index  (44)           # it's working like count. So count the value is spicified in parentheses
nums.sort                     # sort is using for sort the number in the list from the smaller to the bigger
nums.clear                   # clear is using for clear entire items in the list
del nums[3:]                 # del is delete all item that spicified in square parantheses
min (nums)                   # min is using to find the smallest value in that list
max (nums)                  # max is using to find the biggest value in that list
sum (nums)                  # sum is using for addition items in the list


                                                ##                    TUPLE       


# Tuple are unmutable.
tup= (23, 43,90,87)
tup
tup[2]
# tup[2]=78 #it will give an error beause it's unmutable


                                                ##                   SET         


#set is collection of elements
s = {34,56,245,33}
s  # this will not give certain sort. Because set don't have proper sequence.
#  s[1] # so this will not work

# s.add
# s.copy
# s.difference
# s.difference_update
# s.discard
# s.intersection
# s.intersection_update
# s.isdisjoint
# s.issubset
# s.issuperset 
# s.pop
# s.remove
# s.symmetric_difference
# s.symmetric_difference_update
# s.union
# s.update
# s.clear


                                            ##                   DICTIONARY         


# Dictionary is working like a contacts in phone. So if you want see a number you search forr name and you can reach the number

data= {1: 'Siyar', 2: 'Furkan!', 3:'Veysel', 4:'Biyo'}
data
# How to fetch a particular value

data[4]
# data [5]   it will give an error

# another way to fetch value in dictionary

data.get(1)
data.get(7) # it will give none/null
data.get(1, 'Not Found')
data.get(5, 'Not Found') # it will give not found as output

#how to combine two list into a dictionary

keys= ['Siyar', 'Furkan', 'Veysel', 'Biyo']
value= ['python', 'C', 'matlab', 'Assembly']
data= dict (zip(keys, value))      # zip combine two list   and dict make them a dictionary

#how to add new value in the dictionary

data ['Zafer'] = 'Autocad'
data

# how to create a dictionary which contain dictionary and list in it

prog = {'js': 'Atom', 'c#':'vs', 'python': ['pycharm', 'sublime'], 'java': {'jse':'netbeans', 'jee': 'ecplise'}}
prog ['js']
prog ['python'] 
prog ['python'] [1]
prog ['java']
prog ['java'] ['jee']




