class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            if s < target:
                i += 1
            if s == target:
                return [i+1,j+1]
