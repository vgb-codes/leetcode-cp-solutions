class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        MAP = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in MAP:
                return [MAP[comp], i]
            MAP[nums[i]] = i
        return []
