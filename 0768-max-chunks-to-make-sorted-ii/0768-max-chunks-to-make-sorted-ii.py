class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        
        count = {}
        ans = 0
        
        for i in range(len(arr)):
            count[arr[i]] = count.get(arr[i], 0) + 1
            count[sorted_arr[i]] = count.get(sorted_arr[i], 0) - 1
            
            if count[arr[i]] == 0:
                del count[arr[i]]
            if sorted_arr[i] in count and count[sorted_arr[i]] == 0:
                del count[sorted_arr[i]]
            
            if not count:
                ans += 1
        
        return ans