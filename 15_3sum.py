class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cache = {}
        cnt = len(nums)
        if cnt < 3:
            return []
        
        for i in range(cnt):
            for j in range(i +1, cnt):
                sum = nums[i] + nums[j]
                if sum in cache:
                    cache[sum].append([i, j])
                else:
                    cache[sum] = [[i,j]]
        idx = []
        for i in range(cnt):
            remain = -nums[i]
            if remain in cache:
                for r in cache[remain]:
                    if i > r[1]:
                        one = r[:]
                        one.append(i)
                        idx.append(one)
        rt = []
        return rt
    



tc = Solution()
print(tc.threeSum([-1, 0, 1, 2, -1, -4]))