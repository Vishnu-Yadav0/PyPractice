'''
 Q.1 Write a function SmallLargeSum(array) which accepts the array as an argument or parameter, 
 that performs the addition of the second largest element from the even location with the second largest element from an odd location?

Rules:

All the array elements are unique.
If the length of the array is 3 or less than 3, then return 0.
If Array is empty then return zero.
 
 '''

def SmallLargeSum(arr):
    even=[]
    odd=[]
    if len(arr) > 3 :
        for i in range(len(arr)):
            if i%2==0:
                even.append(arr[i])
            else:
                odd.append(arr[i])
        even.sort(reverse=True)
        odd.sort(reverse=True)
        return even[1]+odd[1]
    else:
        return 0

array=[3,2,1,7,5,4]
res = SmallLargeSum(array)
print(res)

arr=[4,0,7,9,6,4,2]
res = SmallLargeSum(arr)
print(res)