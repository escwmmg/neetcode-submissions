class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = nums.copy()
        for checker in nums:
            del(dupe[0])
            if (checker in dupe):
                return True
        return False