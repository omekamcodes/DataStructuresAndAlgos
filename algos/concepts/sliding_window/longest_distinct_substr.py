def longest_distinct_substring(s):
    # Initialize the maximum length of the substring to be 0.
    max_length = 0

    # Initialize the start and end indices of the window to be 0.
    start_index = 0
    end_index = 0

    # Initialize a set to store the distinct characters in the window.
    distinct_chars = set()

    # Iterate over the string, starting at the first character.
    # For each character, update the set of distinct characters in the window.
    # If the current number of distinct characters in the window is greater than 1,
    # move the start index of the window forward until the number of distinct characters
    # is less than or equal to 1.
    # Update the maximum length of the substring if the current length is greater than the maximum length.
    for i in range(len(s)):
        char = s[i]
        distinct_chars.add(char)
        while len(distinct_chars) > 1:
            char = s[start_index]
            distinct_chars.remove(char)
            start_index += 1
        max_length = max(max_length, i - start_index + 1)

    return max_length


s = "abccdefgh"
max_length = longest_distinct_substring(s)


"""
The longest_distinct_substring function will return the length of the longest 
substring with all distinct characters. 
In this example, the longest substring with all distinct characters is "cdefgh",
which has a length of 6.
"""
