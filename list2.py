def matching(words):
    count =0
    list=[]
    for i in words:
        if len(i)>1 and i[0] == i[-1]:
            count +- 1
            list.append(i)
   
   
    print("List of words the first and the last character are same", list)   
    return count
word1 = matching(['abc','art','1221','aba'])    
print(word1) 