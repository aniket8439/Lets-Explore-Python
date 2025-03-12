class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive = 0
        negative = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                positive += 1
            if nums[i] < 0:
                negative += 1

        return max(positive, negative)
    
# ! Explanation:
# * This function calculates the maximum count of positive integers and negative integers in the input list.
# * 1. Initialize the `positive` and `negative` variables to store the count of positive and negative integers, respectively.
# * 2. Iterate through the elements of the input list using the `i` pointer.
# * 3. If the current element is greater than 0, increment the `positive` count.
# * 4. If the current element is less than 0, increment the `negative` count.
# * 5. Return the maximum count of positive and negative integers.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input list.
# * This is because we iterate through the list once to count the positive and negative integers.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space to store variables.
# * The space complexity of this approach is O(1).    