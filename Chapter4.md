# Quicksort
Quicksort is a sorting algorithm. It's much faster than selection sort and is frequently used in real life. C standard library has a function called qsort which is its implementation of quicksort.

Empty arrays and arrays with just one element will be the base case. You can just return those arrays as is there's nothing to do.


Quicksort works by picking an element from an array. This element is the pivot.

For the pivot you are finding elements taht are smaller than the pivot and larger than the pivot.

This is called partitioning.
Now you have a sub-array of all the numbers less than the pivot.
The pivot
A sub-array of all the numbers greater than the pivot.

The two sub arrays aren't sorted. They're just partitioned. 

If the sub arrays were sorted then you can combine the whole thing as such: 
left array (elements smaller than the pivot) + pivot (middle point) right array (elements larger than the pivot).

QUicksort base case knows how to sort arrays of two elements (the left sub-array) and empty arrays (the right sub-array). So if you call quicksort on the two subarrays and then combine the results you get a sorted array
quicksort([15,10]) + [33] + quicksort([]) => [10,15,33]

Steps as followed:
1. Pick a pivot
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Call quicksort recursively on the two sub-arrays

## Inductive Proofs

Inductive Proofs are one way to prove that your algorithm works. Each inductive proof has two steps: the base case and the inductive case.


## Divide and Conquer
D&C for short
D&C Algorithm are recursive algorithms.
1. Figure out the base case. This should be the simplest possible case.
2. Divide or decrease your problem until it becomes the base case.44

Euclidean Algorithm, 
Divide a plot of land by the largest box possible.

When you're writing a recursive function involving an array, the base case is often an empty array or an array with one element.

Haskell doesn't have loops so the use of recursion happens often

## Big O
Quicksort is unique because its speed depends on the pivot you choose. 

Examples of Big O:

O (log n) Binary Search
O (n) Simple search
O (n Log n) Quicksort
O (n^2) Selection Sort
O (n!) The Traveling Salesman

## Merge Sort vs Quicksort

When you write Big O notation like O(n), it really means this: 
c * n
Some Fixed Amount of Time 
c is some fixed amount of time that your algorithm takes. It's called the constant.

Sometimes constant can make a difference.
The performance of quicksort heavily depends on the pivot you choose.

In worse case scenario you choose the first element of the array and have to loop through all the elements. O(n). In the best case, the stack size is O(log n). If you always choose a random element in the array as the pivot, quicksort will complete in O(n log n) time on average.

D&C works by breaking a problem down into smaller and smaller pieces.