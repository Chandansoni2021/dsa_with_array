arr = [1, 2, 3, 4, 5, 6, 7]
d=2
k=arr.index(d)
print(k)
newlst=[]
newlst=arr[k+1:]+arr[0:k+1]
print(newlst)
