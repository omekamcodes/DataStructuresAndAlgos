def longest_replacement_substring(s, k):
    # Initialize the maximum length of the substring to be 0.
    max_length = 0

    # Initialize the start and end indices of the window to be 0.
    start_index = 0
    end_index = 0

    # Initialize a dictionary to store the count of each character in the window.
    char_count = {}

    # Iterate over the string, starting at the first character.
    # For each character, update the count of the character in the window.
    # If the number of characters that are different from the most common character
    # in the window is greater than k, move the start index of the window forward
    # until the number of different characters is less than or equal to k.
    # Update the maximum length of the substring if the current length is greater than the maximum length.
    for i in range(len(s)):
        char = s[i]
        char_count[char] = char_count.get(char, 0) + 1
        while (
            len(char_count) > 0 and i - start_index + 1 - max(char_count.values()) > k
        ):
            char = s[start_index]
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
            start_index += 1
        max_length = max(max_length, i - start_index + 1)

    return max_length


s = "aabccbb"
k = 2
max_length = longest_replacement_substring(s, k)


"""
The longest_replacement_substring function will return the length of the 
longest substring that can be obtained by replacing no more than k letters in the input string. 
In this example, the longest substring that can be obtained by replacing no more than 2 letters is "bcbb", 
which has a length of 4.




"""
