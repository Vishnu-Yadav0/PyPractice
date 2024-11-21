arr=[1,2,-3,0,-4,3]
n=len(arr)
for i in range(n+1):
    for j in range(i):
        print(arr[j],end='\t')
    print('\n')


