class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        positions = {}

        for i, ch in enumerate(ring):
            positions.setdefault(ch, []).append(i)

        memo = {}

        def dfs(k, pos):
            if k == len(key):
                return 0

            if (k, pos) in memo:
                return memo[(k, pos)]

            ans = float('inf')

            for next_pos in positions[key[k]]:
                diff = abs(pos - next_pos)
                rotate = min(diff, n - diff)

                ans = min(
                    ans,
                    rotate + 1 + dfs(k + 1, next_pos)
                )

            memo[(k, pos)] = ans
            return ans

        return dfs(0, 0)