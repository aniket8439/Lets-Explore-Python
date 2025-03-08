# Sliding Window

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_count = 0
        ans = float("inf")
        
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i-k] == 'B':
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1

            ans = min(ans, k - black_count)

        return ans

# ! Explanation:
# * This function calculates the minimum number of recolors required to obtain k consecutive black blocks in a given string of blocks.
# * 1. Initialize variables `black_count` to store the count of black blocks and `ans` to store the minimum number of recolors.
# * 2. Iterate through the string of blocks.
# * 3. If the window size is greater than k and the block at the left end of the window is black, decrement the black count.
# * 4. If the current block is black, increment the black count.
# * 5. Update the answer by taking the minimum of the current answer and the difference between k and the black count.
# * 6. Return the minimum number of recolors required to obtain k consecutive black blocks. 

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input string `blocks`.
# * This is because we iterate through the string once to calculate the minimum number of recolors. 

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space to store variables `black_count` and `ans`.
# * The space complexity of this approach is O(1).


