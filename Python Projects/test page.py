from array import array
vals=array ('i',[4,6,7,2,-13,9])
newArr=array(vals.typecode,(a*a for a in vals))
print(newArr)