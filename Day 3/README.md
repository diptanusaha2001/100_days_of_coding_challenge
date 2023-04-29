Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

LeetCode 17 Keypad
Constraints:
0 ≤ digits.length ≤ 4
digits[i] is a digit in the range ['2', '9'].
Examples
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Approach
How do we solve it? If you are thinking about recursion, then you are on the right track. At each stage of recursion there will be a digit that will represent some characters, and then we will recursively send the next digit to look for those set of characters that could be appended in our result string.

We can follow below steps —

Construct an array where each index represents the corresponding letters on the keypad corresponding to that number. Since there are no letters with respect to 0 and 1, for the sake of ease of accessibility, we will put dummy values on those indices. Such an array will look something like this —
lettersAndNumbersMappings = [
        "Anirudh",
        "is awesome",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    ]
Write a helper function which will contain the crux of our logic. This function will be called recursively.
In the recursive function, we should have a terminating condition. In our case, think when our recursion will stop 🤔? It will stop when we have scanned all the characters in the given string. At that point, we will return.
If the terminating condition is not met then we will first find the letters corresponding to the current characters in the given string by referring to our mappings array.
We will then loop for all the characters in the string obtained in the previous step and call make recursive calls with the strings after appending the current character and the string in the previous step.


Time Complexity
The numbers in input string can represent strings of length of 3 or 4. Let m be the number of digits that map to 3 letters and n be the number of digits that map to 4 letters. Thus, the overall time complexity will be O(3m × 4n).

Space Complexity
The recursive call will use the stack memory equal to O(3m × 4n) and this will be the space complexity.
