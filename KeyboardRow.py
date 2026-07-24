#KeyboardRow.py

class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            original_word = word
            word = word.lower()

            # Check which row the first character belongs to
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            else:
                row = row3

            word_found = True

            # Check all characters belong to the same row
            for char in word:
                if char not in row:
                    word_found = False
                    break

            if word_found:
                result.append(original_word)

        return result


# --------------------User Input-------------------
if __name__ == "__main__":
    words = input("Enter words separated by space: ").split()

    solution = Solution()
    answer = solution.findWords(words)

    print("Words that can be typed using one keyboard row:")
    print(answer)

"""
LeetCode 500. Keyboard Row

Problem:
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 

So,
Time Complexity:
O(N * M)
N = number of words
M = average length of each word

------------------sample input from leetcode---------------------

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""