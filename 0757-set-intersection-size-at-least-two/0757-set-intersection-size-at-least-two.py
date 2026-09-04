class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -1
        b = -1
        ans = 0

        for start, end in intervals:
            if start > b:
                a = end - 1
                b = end
                ans += 2

            elif start > a:
                a = b
                b = end
                ans += 1

        return ans