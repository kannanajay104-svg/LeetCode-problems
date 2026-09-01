class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        missing = 0

        if not any(c.islower() for c in password):
            missing += 1

        if not any(c.isupper() for c in password):
            missing += 1

        if not any(c.isdigit() for c in password):
            missing += 1

        replace = 0
        one = 0
        two = 0

        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                replace += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

            i = j

        if n < 6:
            return max(6 - n, missing)

        if n <= 20:
            return max(replace, missing)

        delete = n - 20

        take = min(delete, one)
        replace -= take
        delete -= take

        take = min(delete // 2, two)
        replace -= take
        delete -= take * 2

        replace -= delete // 3

        return (n - 20) + max(replace, missing)