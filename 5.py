# CHECK ARRAY ARE DISJOINT OR NOT

arr1=[1,2,3,4,5]
arr2=[1,2,3,4,5]
def disjoint_array(arr1,arr2):
    for i in range(0,len(arr1)):
        for j in range(0, len(arr2)):
            if(arr1[i]==arr2[j]):
                return-1
res=disjoint_array(arr1,arr2)
if(res==-1):
    print("the array are not disjoint")
else:
    print("the array are disjoint")
