def div (a,b):
    print(a/b)
# if we don't wanna change the funtion already existing so use decorators
def smart_div(func): 
    
    def inner (a,b):
        a,b=b,a
        return func(a,b)
    return inner
div =smart_div(div)
div(2,4)
