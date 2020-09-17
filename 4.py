# FIND SUM OF ELEMENT FROM GIVEN ARRAY AND FIND AVERAGE OF ALL ELEMENT IN ARRAY

arr=[10,20,30,40,50]
def sum(arr):
    ans=0
    for i in arr:
        ans+=i
    return ans
print('sum:',sum(arr))

def Avg(arr):
    return sum(arr)/len(arr)
average=Avg(arr)
print("avg:",average)