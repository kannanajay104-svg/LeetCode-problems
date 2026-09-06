class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def solve(i):
            if expression[i] == 't':
                return True, i + 1

            if expression[i] == 'f':
                return False, i + 1

            op = expression[i]
            i += 2

            values = []

            while expression[i] != ')':
                if expression[i] == ',':
                    i += 1
                    continue

                value, i = solve(i)
                values.append(value)

            i += 1

            if op == '!':
                return not values[0], i

            if op == '&':
                return all(values), i

            return any(values), i

        return solve(0)[0]