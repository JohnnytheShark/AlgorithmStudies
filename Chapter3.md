# Recursion
Recursion, people either love it or hate it.

Recursion is used when it makes the solution clearer.

There is no performance benefit to using recursion, in fact loops are sometimes better for performance.

## Pseudocode
High-Level description of the problem you're trying to solve, in code. It's written like code, but it's meant to be closer to human speech

## Warning 
Because a recursive function calls itself, it's easy to write a function incorrectly that ends up in an infinite loop.

When you write a recursive function, you have to tell it when to stop recursing.

## In Practice
Recursion needs a base or a grounding element that break the recursion. This is typically called base case.

Example: 
def countdown(i):
print i
if i <= 1: #base case
    return 
else:
    countdown(i-1) #Recursive case

## The Stack
Call Stack is adding a list of to dos for your computer to do. The stack is a simple data structure.

Your computer uses a stack interally called the call stack.

When you call a function from another function, the calling function is paused in a partially completed state. All the values of the variables for that function are still stored in memory.

Using the stack is convenient, but there's a cost: saving all that info can take up a lot of memory. Each of those function calls takes up some memory.

## Tail Recursion
An advanced recursion topic that is only supported by some languages, not all.


