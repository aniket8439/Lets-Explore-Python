class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        usedBits = 0
        maxLength = 0

        for right in range(len(nums)):
            while (usedBits & nums[right]) != 0:
                usedBits ^= nums[left]
                left += 1

            usedBits |= nums[right]
            maxLength = max(maxLength, right - left + 1)

        return maxLength        
    

# ! Explanation:
# * This function finds the length of the longest "nice" subarray in the input list.
# * 1. Initialize the left pointer to 0, the usedBits variable to 0, and the maxLength variable to 0.
# * 2. Iterate through the input list using the right pointer.
# * 3. While the current element is already present in the subarray, remove the leftmost element from the subarray.
# * 4. Update the usedBits variable by XORing it with the current element.
# * 5. Update the maxLength by taking the maximum of the current length and the previous maximum length.
# * 6. Return the maxLength after iterating through the entire list.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the number of elements in the input list.
# * This is because we iterate through the input list once using the right pointer.

# ? Space Complexity:
# * The space complexity of this approach is O(1) because we use a constant amount of extra space.
# * The space complexity of this approach is O(1).    