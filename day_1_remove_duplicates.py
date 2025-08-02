from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup=set()
        for i in range (len(nums)):
            if nums[i] in dup:
                nums[i]="_"
            else:
                dup.add(nums[i])
        write = 0
        for read in range(len(nums)):
            if nums[read] != '_':
                nums[write] = nums[read]
                write += 1
        return len(dup)   
sol = Solution()     
print(sol.removeDuplicates([1,1,2]))  