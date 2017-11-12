class Solution(object):
    def bsearch(self, nums, t, start):
        L = start
        R = len(nums) - 1
	m = 0
        while (L < R):
            m = int((L + R) / 2)
            print L,R,m,t
            if t > nums[m]:
                L = m + 1
            else:
                R = m
        return L if nums[L] == t else None
    
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,d in enumerate(numbers):
            e = target - d
            j = self.bsearch(numbers, e, i+1)
            print j
            if j is not None:
                return [i+1, j+1]


