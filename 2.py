#   REMOVE DOUBLICATES IN ARRAY

arr=[1,2,4,5,3,5,7,6,2]
print("original array:" + str(arr))

res=[]
for i in arr:
    if i not in res:
        res.append(i)
print("aftere removing duplicate elements:" + str(res))