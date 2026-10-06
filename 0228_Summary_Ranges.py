#Leetcode 228 : Summary Ranges
# Difficulty : Easy

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i, n = 0, len(nums)

        while i < n: 
            start = i # Start of the current range

            # Move i while numbers are consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            # If only one number in the range
            if start == i:
                res.append(f"{nums[start]}")
            else:
                # If there are multiple consecutive numbers
                res.append(f"{nums[start]}->{nums[i]}")

            i += 1 # Move to the next range

        return res