import math
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = {}
        left_index = 0
        max_length = -math.inf

        for right_index in range(len(s)):
            right_character = s[right_index]

            if right_character in seen:
                left_index = max(left_index, seen[right_character] + 1)

            seen[right_character] = right_index

            max_length = max(max_length, right_index - left_index + 1)

        return max_length
