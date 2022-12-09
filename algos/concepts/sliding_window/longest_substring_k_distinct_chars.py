"""
To find the longest substring with k distinct characters in a given string,
 you can use a sliding window approach. 
 This involves keeping track of the number of distinct characters 
 in the current window 
 and updating the window as it moves through the string.
"""


def longest_substring_with_k_distinct_characters(num_distinct_chars, s):
    # Initialize the maximum length to be 0.
    max_length = 0

    # Initialize the start and end indices of the window to be 0.
    start_index = 0
    end_index = 0

    # Initialize a dictionary to store the count of each character in the window.
    char_count = {}

    # Iterate over the string, starting at the first character.
    # For each character, update the count of the character in the window.
    # If the current number of distinct characters in the window is greater than num_distinct_chars,
    # move the start index of the window forward until the number of distinct characters
    # is less than or equal to num_distinct_chars.
    # Update the maximum length if the current length is greater than the maximum length.
    for i in range(len(s)):
        char = s[i]
        char_count[char] = char_count.get(char, 0) + 1
        while len(char_count) > num_distinct_chars:
            char = s[start_index]
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
            start_index += 1
        max_length = max(max_length, i - start_index + 1)

    return max_length


k = 2
s = "araaci"
max_length = longest_substring_with_k_distinct_characters(k, s)

"""
The longest_substring_with_k_distinct_characters function will return the length of the 
longest substring with k distinct characters in the given string. 
In this example, the longest substring with 2 distinct characters is 
"araa" with a length of 4.
"""
