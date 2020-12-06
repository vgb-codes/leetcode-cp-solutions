class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        if len(numbers) == 2:
            if numbers[0] + numbers[1] == target:
                return [1,2]
            else:
                return []
        
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            total = numbers[start] + numbers[end]
            
            if total > target:
                end -= 1
            elif total < target:
                start += 1
            else:
                return [start + 1, end + 1]
        
        return []