L = [4,6,7,8,9,2,4,5]
print("original list", L)
count=0

#sum of list items
for i in L:
    count=count+1

#average of list items
avg = count/len(L)

print("sum = ",count)
print("average = ",avg)

L.sort() #by default ascending order
print(L)
print("smallest element ", L[0])
print("largest element is ", L[-1])


