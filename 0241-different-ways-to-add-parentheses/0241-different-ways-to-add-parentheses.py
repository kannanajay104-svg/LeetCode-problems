class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def solve(s):
            result = []

            for i in range(len(s)):
                if s[i] in "+-*":
                    left = solve(s[:i])
                    right = solve(s[i + 1:])

                    for a in left:
                        for b in right:
                            if s[i] == '+':
                                result.append(a + b)
                            elif s[i] == '-':
                                result.append(a - b)
                            else:
                                result.append(a * b)

            if not result:
                result.append(int(s))

            return result

        return solve(expression)