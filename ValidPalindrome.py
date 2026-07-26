# ValidPalindrome.py

"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

def is_palindrome(s):
    # Store only letters and numbers in lowercase
    x = ""                          # empty string

    for ch in s:                    # looping through string one character at a time
        if ch.isalnum():            # keeping letters(characterrs) and numbers only (filtering space, comma, colon, etc)
            x = x + ch.lower()      # adding valid characters to string with lower case

    return x == x[::-1]             # comparing clean string with its reverse


# User input
text = input("Enter a string: ")

# Check palindrome
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")