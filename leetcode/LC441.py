class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            middle = left + (right-left)//2
            total = middle*(middle + 1)//2
            if total == n:
                return middle
            if n < total:
                right = middle - 1
            else:
                left = middle + 1
        return right
