Problem Statement:
The string “PAYPALISHIRING” is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P A H N A P L S I I G Y I R And then read line by line: “PAHNAPLSIIGYIR”
Write the code that will take a string and make this conversion given a number of rows: string convert(string s, int numRows);

Constraints: 
1 <= s.length <= 1000 
s consists of English letters (lower-case and upper-case), ’,’ and ’.‘. 
1 <= numRows <= 1000 

Examples: 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3 Output: "PAHNAPLSIIGYIR" Example 2:
Input: s = "PAYPALISHIRING", numRows = 4 Output: "PINALSIGYAHRPI" Explanation: P I N A L S I G Y A H R P I Example 3:
Input: s = "A", numRows = 1 Output: "A" Analysis Here, we are given a string s and number of rows numRows. 

The task is to take one character of the string at a time and write it in a new row until we reach to the given numRows. 
Once we reach to the end, we continue writing the next character in the next column and row - 1 until we reach the first row. 
Repeat this process until we have anymore characters left.
Once we are done creating the rows, we will return the string made by appending each row one after the another.

Approach: 
Let’s say we have string s = PAYPALISHIRING and numRows = 4, then the zigzag pattern would look like below (I’ve added indices of each character against it for better understanding) -
[00]P [06]I [12]N
[01]A [05]L [07]s [11]I [13]G
[02]Y [04]A [08]H [10]R
[03]P [09]I
If you look closely to the above pattern, you will find that the difference between each character in the first and last row is 2 * numRows - 2. We will call it step i.e., step = 2 * numRows - 2.
In our case - step = 2 * numRows - 2 = 2 * 4 - 2 = 6 and you can confirm that this condition holds true for first (0 —> 6 —> 12) and last rows (3 —> 9).
And for the middle rows, we will run another loop which starts from the current row and jumps step size after each iteration. Thus, we will get following values
For i = 0 => j = 0, 6, 12
For i = 1 => j = 1, 7, 13
For i = 2 => j = 2, 8
For i = 3 => j = 3, 9



Time Complexity:
Since we are iterating each character in the String only once, the time complexity will be O(n).

Space Complexity:
We are not using any extra space here, therefore, the space complexity would be O(1).

#vitbhopallions #programming #leetcode2023
