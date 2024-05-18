# Algorithms
An algorithm is a set of instructions for accomplishing a task. 

## Binary Search

Binary Search is an Algorithm; it's input is a sorted list of elements. IF an element you're looking for is in the list, binary search returns the position where it's located. Otherwise, binary search returns null (-1 in Java).

With Binary Search, YOu guess the middle number and eliminate half the remaining numbers every time.

Illustrated: 

100 Items -> 50 Items -> 25 -> 13 -> 7 -> 4 ->2 -> 1

In general, for any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search will take n.

## Simple Search (Stupid Search)
You loop through your entire list one element at a time and it takes forever to get through just to find your item.