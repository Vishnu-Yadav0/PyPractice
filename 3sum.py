'''
13/10/2024

#3Sum - https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

'''


def threeSum(nums):
    nums.sort()  #sorting
    n=len(nums)
    answer=[]
    for i in range(n):
        if nums[i] > 0: #if the element is positive ,as we know the list is sorted so there will be no way of have triplet sum as 0
            break
        
        #if the previous number is same , then there is no use of looping into it again bcauz we tried all of them already , so its better to skip
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        low,high=i+1, n-1


        while low < high: #condition to check whether they both cross each other and do the things again
            summ = nums[i] + nums[low] + nums[high]
            if summ == 0:
                answer.append([nums[i], nums[low], nums[high]])
                low, high = low+1, high-1

                while low < high and nums[low] == nums[low-1]:
                    low+=1
                while low < high and nums[high] == nums[high+1]:
                    high-=1
            elif summ < 0:
                low+=1
            else:
                high-=1
            
    return answer

print(threeSum([0,0,0]))
print(threeSum([0,1,1]))
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-3,-3,-2,-1,0,1,2,2,3]))

            
            

