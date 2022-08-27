'''
used sorting a list,
taked first element as min
'''


a=[13,4,9,5,3]

for i in range(len(a)):
    min_index=i
    for j in range(i+1,len(a)):
        if a[j]<a[min_index]:
            min_index=j
            a[i],a[min_index]=a[min_index],a[i]
print (a)
