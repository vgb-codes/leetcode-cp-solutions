class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num < 2):
            return num
        left = 1
        right = num

        while left <= right:
            middle = left + int((right - left)/2)
            if (middle * middle == num):
                return True
            elif (middle * middle > num):
                right = middle - 1
            else:
                left = middle + 1
        return False
