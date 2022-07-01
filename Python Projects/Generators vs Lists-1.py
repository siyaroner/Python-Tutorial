# For list 
def square_numbers_L(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result

def square_numbers_G(nums):
    for i in nums:
        yield (i*i)  # yield this is what make the generator.
        
my_nums_L=square_numbers_L([1,2,3,4,5])
my_nums_G=square_numbers_G([1,2,3,4,5])
print (my_nums_L)
for num in my_nums_G:
    print("Generator ",num)
print ("generator adress",my_nums_G)

# print ("printin generator items: ",next(my_nums_G))
# print ("printin generator items: ",next(my_nums_G))
# print ("printin generator items: ",next(my_nums_G))
# print ("printin generator items: ",next(my_nums_G))
# print ("printin generator items: ",next(my_nums_G))
#print ("printin generator items: ",next(my_nums_G)) # it will give StopIteration execption

# With list comprehension
my_nums_L =[x*x for x in [1,2,3,4,5] ]
print(my_nums_L)
my_nums_G =(x*x for x in [1,2,3,4,5] )
for num in my_nums_G:
    print("Generator comprehension",num)