class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        end = Counter()

        for x in nums:
            if count[x] == 0:
                continue

            if end[x - 1] > 0:
                count[x] -= 1
                end[x - 1] -= 1
                end[x] += 1

            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x] -= 1
                count[x + 1] -= 1
                count[x + 2] -= 1
                end[x + 2] += 1

            else:
                return False

        return True