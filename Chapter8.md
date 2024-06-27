# Greedy Algorithms

## Classroom problem

Suppose you have a room and want to hold as many classes in that room as possible. 

You get a list of the classes and review times 
You can't hold all these classes in there, because some of them overlap. 

Here's the algorithm
1. Pick the class that ends the soonest. This is the first class you'll hold in this room 
2. Now you have to pick a class that starts after the first calss. Again, pick the class that ends the soonest. This is the second class you'll hold 

Keep doing this, and you'll end up with the answer!

Greedy Algorithms: ARE EASY! A greedy algorithm is simple: at each step, pick the optimal move. 

Greedy Algorithms don't always work, but they're simple to write.

## Knapsack Problem

Suppose you're a greedy thief. You're in a store with a knapsack, and there are all these items you can steal. But you can only take what you can fit in your knapsack. The knapsack can hold 35 pounds. 

You're trying to maximize the value of the items you put in your knapsack. 

Greedy Strategy: 
    1. Pick the most expensive thing that will fit in your knapsack
    2. Pick the next most expensive thing that will fit in your knapsack and so on. 

Purpose of this strategy is to get good enough and not perfect. Perfect is the enemy of good. Sometimes all you need is an algorithm that solves the problem pretty well. And that's where greedy algorithms shine, because they're simple to write adn usually get pretty close. 

## Set-covering problem 
Suppose you're starting a radio show. You want to reach listeners in all 50 states. The problem is deciding which radios stations to choose to have your show broadcasted.

Simplest way of doing it: 
1. List every possible subset of stations. This is called a power set. There are 2^n possible subsets. 
2. From these, pick  the set with the smallest number of stations that cover all 50 states

Problem is: It takes a long time to calculate every possible subset of stations. It takes O(2^n) time, because there ware 2^n subsets. It's possible to do if you have a small set of 5 to 10 stations. It takes much longer if you have more stations. 

You use Approximation Algorithms
1. Pick the station that covers the most states that haven't been convered yet. It's OK if the station covers some states that have been covered already. 
2. Repeat until all the states are covered. 

## Approximation Algorithms: 
Judged by: 
How fast they are 
How close they are to the optimal solution 

Greedy Algorithms are a good choice because not only are they simple to come up with, but that simplicity means they usually run fast, too. 

# Sets
Sets can be utilized to have groups of records with no duplicates. 

Things you can do with sets: 
A set union means 'combine both sets.' 
A set intersection means 'find the items that show in both sets'
A set differences means 'subtract the itesm in one set from the items in the other set. 

- Sets are like lists, except sets can't have duplicates. 
- You can do some interesting operations on sets, like union, intersection, difference. 

## Factorial Functions 
5! = 120 
The traveling-salesperson problem and the set-covering probelm both have something common: you calculate every possible solution adn pick the smallest/shortest one. Both of these problems are NP-complete.

nondeterministic polynomial
 if its solution can be guessed and verified in polynomial time

## NP Problems 
There is no right way of determining if a problem is NP complete. 
However there are giveaways: 
- Your algorithm runs quickly with a handful of items but really slows down with more items. 
- All combinations of X usually point to an NP complete probelms 
- Do you have to calculate every possible version of X because you can't break it down into smaller sub problems? 
- If you problem involves a sequence (such as a sequence of cities, like traveling salesperson), and it's hard to solve, it might be NP-complete.
- IF you problem involves a set(like a set of radio stations ) and it's hard to solve, it might be NP complete
- Can you restate your problem as the set-covering probelm or the traveling-salesperson problem? THen your problem is definitely NP-complete.

# Recap: 
Greedy algorithms optimize locally, hoping to end up with a global optimum
NP-complete problems have no known fast solution. 
IF you have an NP-complete problem, your best bet is to use an approximation algorithm. 
Greedy algorithms are easy to write and fast to run, so they make good approximation algorithms.





