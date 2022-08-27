l=[7,8,5,6,9,4,1]
l.sort()
print(l)
target=5
n=len(l)
low=0
up=len(l)
mid=(low+up)//2

if target==l[mid]:
    print("Target found at: ",mid)
elif target<l[mid]:
    up=mid
elif target>l[mid]:
    low=mid

for i in range(low,up):
    if l[i]==target:
        print("Target found at: ",i)
