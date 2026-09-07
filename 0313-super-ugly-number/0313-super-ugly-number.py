class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        k = len(primes)

        index = [0] * k
        values = primes[:]

        for i in range(1, n):
            ugly[i] = min(values)

            for j in range(k):
                if values[j] == ugly[i]:
                    index[j] += 1
                    values[j] = ugly[index[j]] * primes[j]

        return ugly[n - 1]