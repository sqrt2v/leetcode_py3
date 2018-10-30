class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        rlt = []
        def gen_pre(l, s, e):
            if s == e:
                rlt.append(l)
                return
            i = s
            while i <= e:
                swap(l, s, i)
                gen_pre(l, s +1, e)
                swap(l, s, i)
                i = i +1
                
        
        gen_pre(nums, 0, len(nums) -1)
        return rlt
    

tc  = Solution()
print(tc.permute([1, 2, 3]))