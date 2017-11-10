class JumpGameII(object):
    def dijkstra(self, nums):
        n = len(nums)
        result = {0: 0}
        furtherest = 0
        for i in range(n-1):
            if nums[i]+i <= furtherest:
                continue
            furtherest = nums[i]+i
            current_min_step = result[i]
            if nums[i] >= n-i-1:
                return current_min_step+1
            for j in range(1, nums[i]+1):
                if i+j not in result:
                    result[i+j] = current_min_step+1
                else:
                    result[i+j] = min(result[i+j], current_min_step+1)
        return result[n-1]

    def dfs(self, nums, position):
        # dfs is not a good algorithm for this problem
        # dfs is good for searching the only path not the best path
        pass

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        return self.dfs(nums, 0)


if __name__ == '__main__':
    jg = JumpGameII()
    print jg.jump([2,3,1,1,4])
