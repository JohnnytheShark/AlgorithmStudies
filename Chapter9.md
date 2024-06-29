# Dynamic Programming

Dynamic Programming starts by solving subproblems and builds up to solving the big problem. 

Think of the problem as a grid of possible options. Each row of the grid starts with a possibility and each column is the limitations we have in place. 

We want to create an algorithm going through the different rows checking for possiblities to get to the final conclusion.

## Formula for Knapsack problem: 

row i column j
cell[i][j] = {1. The previous Max (value at cell[i-1][j]) vs 2. Value of the current item + value of the remaining space cell[i-1][j-item's weight]}

## Fractions of an item? 
You can't do it with dynamic-programming solution, you either take the item or not.

You can however divide you columns into divisions just not objects or use a greedy algorithm to solve for fractions. 

## Optimizing your travel itinerary 

It is like knapsack except the columns are the allotted time for the activity and the value it the ranking you gave that item.

Something to know is that changing costs based on where you travel to are not accounted for with Dynamic Programming. 

Meaning if you are to travel from London to Paris it would take half a day to travel there and the weights from the existing activities can't be changed to remove the values. 

Dynamic Programming only works when each subproblem is discrete - when it doesn't depend on other subproblems. 

## Take aways 

- Dynamic Programming is useful when you're trying to optimize something given a constraint. In the knapsack problem, you had to maximize the value of the goods you stole, contrained by the size of the knapsack. 
- You can use dynamic programming when the problem can be broken into discrete subproblems, and they don't depend on each other. 

General tips to follow: 
- Every dynamic-programmming solution involves a grid
- The valuse in the cells are usually what you're trying to optimize.
- Each cell is a subproblem, so think about how you can divide your problem into subproblems. 

## Feynman Algorithm 
Named after the famous physicist Richard Feynman, and it works like: 
1. Write down the problem.
2. Think real hard.
3. Write down the solution.

Sometimes algorithms aren't an exact recipe. They're a framework that you build your idea on top of.

## Longest Common Subsequence - solution: 

pseudo code 
```
if word_a[i] == word_b[j]: # Letters match
    cell[i][j] = cell[i-1][j-1] + 1
else:# THe letters don't match
    cell[i][j] = max(cell[i-1][j], cell[i][j-1])
```
## Use cases 
- Biologist use the longest common subsequence to find similarities in DNA strands. They can use this to tell how similar two animals or two diseases are. 
- git diff. Diff tells you the differences between two files, and it uses dynamic programming to do so. 
- String similarity - Levenshtein distance measures how similar two strings are, and it uses dynamic programming. Levenshtein distance is used for everything from spell-check to figuring out whether a user is uploading copyrighted data.
- Microsoft word wrap utilizes it

## Recap 

- Dynamic Programming is useful when you're trying to optimize something given a constraint. 
- You can use dynamic programming when the problem can be broken into discrete subproblems. 
- Every dynamic-programming solution involves a grid. 
- The values in the cells are usually what you're trying to optimize 
- Each cell is a subproblem, so think about how you can divide your problem into subproblems.
- There's no single formula for calculating a dynamic programming solution.



