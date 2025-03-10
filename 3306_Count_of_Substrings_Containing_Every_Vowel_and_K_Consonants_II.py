class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        left = 0
        vowels = set('aeiou')
        vowels_count = defaultdict(int)
        consonants = 0
        count = 0
        substr = 0

        def minus_char(char):
            if char in vowels:
                vowels_count[char] -= 1
                if vowels_count[char] == 0:
                    del vowels_count[char]

            else:
                nonlocal consonants
                consonants -= 1

        for char in word:
            if char in vowels:
                vowels_count[char] += 1
            else:
                consonants += 1
                count = 0

            while consonants > k:
                minus_char(word[left])
                left += 1

            while consonants == k and len(vowels_count) == 5:
                count += 1
                minus_char(word[left])
                left += 1  

            substr += count

        return substr                                      
    
# ! Explanation:
# * This function calculates the number of substrings that contain every vowel and exactly k consonants.
# * 1. Get the length of the input word `n`.
# * 2. Initialize variables `left` to keep track of the left pointer, `vowels` to store the set of vowels, `vowels_count` to store the count of each vowel, `consonants` to store the count of consonants, `count` to store the number of substrings, and `substr` to store the total number of substrings.
# * 3. Define a helper function `minus_char` to decrement the count of a character in the `vowels_count` dictionary or decrement the `consonants` count.
# * 4. Iterate through the characters of the word.
# * 5. If the character is a vowel, increment the count of that vowel in the `vowels_count` dictionary.
# * 6. If the character is a consonant, increment the `consonants` count and reset the `count` to 0.
# * 7. While the number of consonants is greater than k, decrement the count of the character at the left pointer.
# * 8. While the number of consonants is equal to k and all vowels are present, increment the `count`, decrement the count of the character at the left pointer, and move the left pointer.
# * 9. Increment the total number of substrings by the `count`.
# * 10. Return the total number of substrings.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input word.
# * This is because we iterate through the word once to calculate the number of substrings.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space to store variables and dictionaries.
# * The space complexity of this approach is O(1).    