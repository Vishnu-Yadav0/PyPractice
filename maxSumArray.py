import sys
def maxSumArray(arr,n):
    maxi = -sys.maxsize
    summ=0
    start,end=0,0 # to keep track of the sub array indices
    for i in range(n):
        if summ == 0 : start = i
        summ+=arr[i]
        if summ > maxi:
            maxi = summ
            end = i
        if summ < 0:
            summ = 0
    if maxi < 0: maxi = 0 # if all the elements in the array are negative values then the output will be a negative value
                          #in that case in few questions they will mention that if the output is negative or the array is empty then return 0
                          #for that purpose we have written a condition as if maxi < 0 : that means negative then assign 0 to maxi
    print(maxi)
    print(arr[start:end+1])
arr = [-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
maxSumArray(arr,n)