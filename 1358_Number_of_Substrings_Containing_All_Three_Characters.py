class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        char_count = {'a':0,'b':0,'c':0}

        for right in range(len(s)):
            char_count[s[right]] += 1

            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                count += len(s) - right
                char_count[s[left]] -= 1
                left += 1

        return count        
    
    
# ! Explanation:
# * This function calculates the number of substrings that contain all three characters 'a', 'b', and 'c'.
# * 1. Initialize the `count` variable to store the number of substrings and the `left` pointer to keep track of the left boundary of the substring.
# * 2. Initialize the `char_count` dictionary to store the count of each character.
# * 3. Iterate through the characters of the string using the `right` pointer.
# * 4. Increment the count of the character at the `right` pointer in the `char_count` dictionary.
# * 5. While all characters 'a', 'b', and 'c' are present in the substring, increment the `count` by the number of substrings that can be formed with the current substring, decrement the count of the character at the `left` pointer, and move the `left` pointer.
# * 6. Return the total number of substrings.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input string.
# * This is because we iterate through the string once to calculate the number of substrings.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space to store variables and dictionaries.
# * The space complexity of this approach is O(1).    