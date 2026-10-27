class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        abc = []
        for i in nums:
            if i in abc:
                return True
            abc.append(i)
        
        return False