def ratcounthouse(r,unit,n,arr:list):
    req=r*unit
    if n==0:
        return -1
    elif sum(arr) < req :
        return 0
    else:
        summ=0
        for i in range(n):
            summ+=arr[i]
            if summ>=req:
                return i+1

exp=ratcounthouse(7,2,2,[1,2])
print(exp)