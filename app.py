class Solution(object):
    def twoSum(self, nums, target):

        ## first, we'd want to create a directory with dict()
        ## Then, let's loop i throughout the entire array. 

        complementMap = dict()

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if num in complementMap:
                return [complementMap[num], i]
            else:
                    complementMap[complement] = i



#           def brutForce(self, nums, target):
#            for i in range(len(nums)):
#                for j in range(i+1, len(nums)):
#                    sum - nums[i] + nums[j]
#            if sum == target: 
#                return [i, j]

