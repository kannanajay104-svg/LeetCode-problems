class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum = arrays[0][0]
        maximum = arrays[0][-1]

        ans = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            ans = max(
                ans,
                current_max - minimum,
                maximum - current_min
            )

            minimum = min(minimum, current_min)
            maximum = max(maximum, current_max)

        return ans