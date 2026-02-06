class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    needed = target - (nums[i] + nums[j] + nums[k])

                    if needed in seen:
                        quad = [nums[i], nums[j], nums[k], needed]
                        quad.sort()
                        if quad not in result:
                            result.append(quad)

                    seen.add(nums[k])

        return result

        