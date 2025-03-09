class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        window = 1
        ans = 0
        n = len(colors)

        for i in range(1, n+k-1):
            if colors[i % n] != colors[(i - 1 + n) % n]:
                window += 1
            else:
                window = 1

            if window >= k:
                ans += 1        

        return ans        
    
    
# ! Explanation:
# * This function calculates the number of alternating groups of colors in a given list of colors.
# * 1. Initialize variables `window` to store the size of the current alternating group and `ans` to store the total number of alternating groups.
# * 2. Get the length of the input list `colors`.
# * 3. Iterate through the list of colors with an extended range to handle the wrap-around case.
# * 4. If the current color is different from the previous color, increment the window size.
# * 5. If the current color is the same as the previous color, reset the window size to 1.
# * 6. If the window size is greater than or equal to k, increment the answer.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input list `colors`.
# * This is because we iterate through the list once to calculate the number of alternating groups.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space to store variables `window` and `ans`.
# * The space complexity of this approach is O(1).
        