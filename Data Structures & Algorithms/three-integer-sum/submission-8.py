class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []
        i = 0
        while i < n-2:
            target = - nums[i]
            left = i+1
            right = n-1
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            while left < right:
                if nums[left] +nums[right] == target:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right-=1
                    while left < n-1 and nums[left] == nums[left-1]:
                        left +=1
                    while right >=0 and nums[right] == nums[right+1]:
                        right-=1
                elif nums[left] + nums[right] < target:
                    left +=1
                elif nums[left] + nums[right] > target:
                    right -=1
            i+=1
        return res



