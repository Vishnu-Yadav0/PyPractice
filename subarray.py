def subarr(arr):
    #to print all the contigous subarrays
    count=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(i,j+1):
                print(arr[k],end = ' ')
            count+=1
            print('\n')
        print('\n')
    print("SubArrays :",count)
arr=[1,2,33,4,5]
subarr(arr)