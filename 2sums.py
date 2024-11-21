# def read(n: int, book: [int], target: int) -> str:
#     # Write your code here.
#     for i in range(len(book)):
#         for j in range(len(book)):
#             if i==j:
#                 continue
#             elif book[i]+book[j] == target:
#                 return 'Yes',i,j
#                 break
#     return 'NO'
# def read(n: int, book: [int], target: int) -> str:
#     global mp
#     mp={}
#     for i in range(n):
#         num=book[i]
#         more=target-num
#         if more in mp:
#             return 'YES'
#         mp[num]=i
#     return 'NO'
# a=read(5,[4,1,2,3,1],7)
# print(a,mp)
def twoSum(n, arr, target):
    ans = [-1, -1]
    mpp = {}
    for i in range(n):
        num = arr[i]
        moreNeeded = target - num
        if moreNeeded in mpp:
            ans[0] = mpp[moreNeeded]
            ans[1] = i
            return ans
        mpp[arr[i]] = i
    return ans

n = 5
arr = [2, 6, 5, 8, 11]
target = 14
ans = twoSum(n, arr, target)
print("This is the answer for variant 2: [" + str(ans[0]) + ", " + str(ans[1]) + "]")