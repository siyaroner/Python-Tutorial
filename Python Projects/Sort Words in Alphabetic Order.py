# def creating_nest_lst():
#     for i in range(words):
#         words_lst.append([])


# def word_count(words):
#     #global words
#     for i in range(len(sentence_lst)):
#         if ord(sentence_lst[i])==32: # 32 repesents null in ascii
#             words+=1
#     return words

# Method 1
# Program to sort alphabetically the words form a string provided by the user

sentence = "Hello my name is Ahmet"
words = [word.lower() for word in sentence.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)

# Method 2
def filling_words_lst():
    j=0
    k=1
    for i in range(len(sentence_lst)):
        if ord(sentence_lst[i])==32: # 32 repesents space in ascii
           words_lst.append(sentence_lst[j:i])
           j=i+1
           last_null=i
        elif i==len(sentence_lst)-1:
            words_lst.append(sentence_lst[last_null+1:i+1])
            
def sorting_words():
    for j in range (len(words_lst)):
        j=0
        k=0
        Min=words_lst[0][0].lower()
        for i in range(len(words_lst)-1):
            if ord(words_lst[i+1][0].lower())<ord(Min):
                Min=words_lst[i+1][0]
                k=i+1
                j+=1
        sorted_lst.append(words_lst[k])
        words_lst.remove(words_lst[k])
def sorting_strings(sorted_strings):
    for j in range(len(sorted_lst)):
        for i in range(len(sorted_lst[j])):
            sorted_strings+=sorted_lst[j][i]
        print(f"{j+1}: {sorted_strings}\n")
        sorted_strings=""       
sentence="Hello my name is Ahmet"
sentence_lst=list(sentence)
words_lst=[]
filling_words_lst()
sorted_lst=[]
sorting_words()
words_lst=[]
sorted_strings=""
sorting_strings(sorted_strings)
