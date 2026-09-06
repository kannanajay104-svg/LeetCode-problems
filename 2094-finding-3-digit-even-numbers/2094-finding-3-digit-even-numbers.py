class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = [0] * 10

        for d in digits:
            count[d] += 1

        ans = []

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            if count[a] == 0:
                continue

            count[a] -= 1

            if count[b] == 0:
                count[a] += 1
                continue

            count[b] -= 1

            if count[c] > 0:
                ans.append(num)

            count[b] += 1
            count[a] += 1

        return ans