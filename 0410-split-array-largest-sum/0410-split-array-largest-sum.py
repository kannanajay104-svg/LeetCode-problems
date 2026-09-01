class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            groups = 1
            current_sum = 0

            for x in nums:
                if current_sum + x <= mid:
                    current_sum += x
                else:
                    groups += 1
                    current_sum = x

            if groups <= k:
                right = mid
            else:
                left = mid + 1

        return left