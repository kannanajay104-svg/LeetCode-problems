class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_freq = 0
        prev_char = ''

        while heap:
            freq, ch = heapq.heappop(heap)

            result.append(ch)
            freq += 1

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_freq = freq
            prev_char = ch

        if len(result) != len(s):
            return ""

        return ''.join(result)