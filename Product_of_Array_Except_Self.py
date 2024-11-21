"""
238. Product of Array Except Self - Medium
Medium

Link :- https://leetcode.com/problems/product-of-array-except-self/description/

Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Hint 1
Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
Hint 2
Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

"""


# def productExceptSelf(nums):
#     l_prod=1
#     r_prod=1
#     n=len(nums)
#     l_arr=[0]*n
#     r_arr=[0]*n
#     for i in range(n):
#         j=-i-1
#         l_arr[i]=l_prod
#         r_arr[j]=r_prod
#         l_prod*=nums[i]
#         r_prod*=nums[j]
#     return [l*r for l,r in zip(l_arr,r_arr)]

# print(productExceptSelf([1,2,3,4]))   #[24,12,8,6]
# print(productExceptSelf([-1,1,0,-3,3]))  #[0,0,9,0,0]

#Time complexity = O(n)
#Space complexity = O(n)

#Optimal solution using constant space solution O(1)

# def productExceptSelf(nums):
#     n=len(nums)
#     result=[0]*n
#     l=1
#     for i in range(n):
#         result[i]=l
#         l*=nums[i]
    
#     r=1
#     for j in range(n-1,-1,-1):
#         result[j]*=r
#         r*=nums[j]


#     return result



# print(productExceptSelf([1,2,3,4]))   #[24,12,8,6]
# print(productExceptSelf([-1,1,0,-3,3]))  #[0,0,9,0,0]

def productExceptSelf(nums):
    n=len(nums)
    result=[0]*n

    l=1
    for i in range(n):
        result[i]=l
        l*=nums[i]
    
    r=1
    for i in range(n-1,-1,-1):
        result[i]*=r
        r*=nums[i]

    return result

print(productExceptSelf([1,2,3,4]))   #[24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3]))  #[0,0,9,0,0]
