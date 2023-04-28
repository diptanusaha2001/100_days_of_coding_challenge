Day 2 of #100daysofcodingchallenge

PROBLEM:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:
Input: height = [1,1]
Output: 1

 

CONSTRAINTS:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104







APPROACH:

The first thing we should realize is that the amount of water contained is always going to be a rectangle whose area is defined as length * width. 
The width of any container will be the difference between the index of the two lines (i and j), and the height will be whichever of the two sides is 
the lowest (min(H[i], H[j])). The brute force approach would be to compare every single pair of indexes in H, but that would be far too slow. Instead, 
we can observe that if we start with the lines on the opposite ends and move inward, the only possible time the area could be larger is when the height 
increases, since the width will continuously get smaller. The first step would be to find our starting container described by the lines on either end. 
We can tell that the line on the right end will never make a better match, because any further match would have a smaller width and the container is 
already the maximum height that that line can support. This is a clear improvement over the last container. We only moved over one line, but we more than 
doubled the height. Now, it's the line on the left end that's the limiting factor, so the next step will be to slide i to the right. Just looking at the 
visual, however, it's obvious that we can skip the next few lines because they're already underwater, so we should go to the first line that's larger than 
the current water height. This time, it doesn't look like we made much of a gain, despite the fact that the water level rose a bit, because we lost more 
in width than we made up for in height. That means that we always have to check at each new possible stop to see if the new container area is better than 
the current best. Just like before we can slide j to the left again. This move also doesn't appear to have led to a better container. But here we can see 
that it's definitely possible to have to move the same side twice in a row, as the j line is still the lower of the two. This is obviously the last possible 
container to check, and like the last few before it, it doesn't appear to be the best match. Still, we can understand that it's entirely possible for the 
best container in a different example to be only one index apart, if both lines are extremely tall.Putting together everything, it's clear that we need to 
make a 2-pointer sliding window solution. We'll start from either end and at each step we'll check the container area, then we'll shift the lower-valued 
pointer inward. Once the two pointers meet, we know that we must have exhausted all possible containers and we should return our answer.



#vitbhopallions #vitbhopal  #programming #leetcode2023 #100daysofcode #100daysofcodechallenge 
