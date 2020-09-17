#  REVERSE THE ARRAY
arr=["school","collage","building","roads","student","teachers","school","roads"]
print("original array:")
for i in range(0,len(arr)):
    print(arr[i])
print("array in reverse order:")
for i in range(len(arr)-1,-1,-1):
    print(arr[i])