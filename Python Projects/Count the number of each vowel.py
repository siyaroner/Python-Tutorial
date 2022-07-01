# ADDING KEY AND VALUE TO DICTIONARY METHODS
# CountryCodeDict["Spain"]= 34
# CountryCodeDict.update( {'Germany' : 49} )
# CountryCodeDict.update( [('Austria', 43),('Russia',7)] )
# .fromkeys(key:value)

sentence="Hello my name is Siyar"
sentence=sentence.lower()
vowels="aeiou"
vowels_dic={}.fromkeys(vowels, 0)
#method 1
for i in vowels:
    for j in sentence:
        if i==j:
            vowels_dic[i]+=1            
print("method 1: ",vowels_dic) 

#method 2
# for char in sentence:
#    if char in vowels_dic:
#        vowels_dic[char] += 1
# print("Method 2",vowels_dic) 

# Method 3: Dictionary comrehension

def func(i):
    vowels_dic[i]+=1
    return vowels_dic

vowels_dic={None:func(i) for i in sentence if i in vowels}

print("method 3",vowels_dic)

#method 4
print("method 4",[{sentence.count(i),i} for i in vowels if i in sentence])

#method 5
print("method 5",[{j:len(list(filter(lambda x:x in j, sentence)))} for j in vowels])

#method 6
print("method 6",[{len([j for j in sentence if j in i]),i} for i in vowels if i in sentence])