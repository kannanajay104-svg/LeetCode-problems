class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        n = len(nums)

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        used = [False] * n

        def backtrack(start, current_sum, groups):
            if groups == k:
                return True

            if current_sum == target:
                return backtrack(0, 0, groups + 1)

            for i in range(start, n):
                if used[i]:
                    continue

                if current_sum + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, current_sum + nums[i], groups):
                    return True

                used[i] = False

                # Avoid trying the same value again
                while i + 1 < n and nums[i] == nums[i + 1]:
                    i += 1

                # If this is the first element of a group
                if current_sum == 0:
                    break

            return False

        return backtrack(0, 0, 0)