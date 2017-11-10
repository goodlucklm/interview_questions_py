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

    def bfs(self, nums):
        # peal the array level by level
        level = [0]
        count = 0
        while len(nums)-1 not in level:
            count += 1
            next_level = set()
            for i in level:
                jump_distance = nums[i]
                max_step = 0
                next_jump = 0
                for n in range(i+1, i +jump_distance+1):
                    if n == len(nums)-1:
                        return count
                    if n < len(nums):
                        if n+nums[n] > max_step:
                            max_step = n+nums[n]
                            next_jump = n
                next_level.add(next_jump)
            level = list(next_level)
        return count

    def direct_jump(self, nums):
        # pick the next step that covers the most range
        next_step = 0
        count = 0
        while next_step < len(nums)-1:
            count += 1
            jump_distance = nums[next_step]
            max_step = 0
            next_jump = 0
            for n in range(next_step+1, next_step+jump_distance+1):
                if n == len(nums)-1:
                    return count
                if n + nums[n] > max_step:
                    max_step = n + nums[n]
                    next_jump = n
            next_step = next_jump
        return count



    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        return self.direct_jump(nums)


if __name__ == '__main__':
    jg = JumpGameII()
    print jg.jump([2,3,1,1,4])
