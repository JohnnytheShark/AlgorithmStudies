# Chapter 2 Selection Sort

## How Memory Works
In memory your computer looks like a giant set of drawers, and each drawer has an address.
Each time you want to store an item in memory, you ask for the computer for some space, and it gives you an address where you can store your item.

Storing multiple items you either use arrays or lists.

## Arrays and Linked Lists
### Arrays
In an array all items are stored in memory right next to each other
When new items are needed to be added to the list the list itself needs to be moved to a new spot in memory that can hold all items consecutively. 
An easy fix to this is to "hold seats" even if you have only 3 items in your task list. Problems with this approach: You may not need the extra slots that you asked for, and then that memory will be wasted, or you may need more than selected amount of spaces, and have to move to a new location anyway.

### Linked Lists
Your items can be anywhere in memory. Each item store the address of the next item in the list. A bunch of random memory addresses are linked together.

Treasure hunt style you go to the first address and it says the next item can be found at address 123. That one then says that the following item is at 846, and so on. Adding an item to a linked list is easy: you stick it anywhere in memory and store the address with the previous item.

Linked LIsts are great if you're going to read all the items one at a time. You can read one item, follow the address to the next item and so on. But if you're going to keep jumping around, linked lists are terrible.

### Arrays
Arrays are different. YOu know the address for every item in your array. Arrays are great if you want to read random elements, because you can look up any elment in your array instantly.

Array indexes start at 0.

Run Times: 

||Arrays|Lists|
|---|---|---|
|Reading| O(1) | O(n)|
|Insertion|O(n)|O(1)|
|Deletion|O(n)|O(1)|

O(n) = Linear Time
O(1) = Constant Time

Lists are better if you want to insert an element into the middle because you are changing what the pointer points to versus an array you may need to shift everything to a new location in memory to accomodate the space.

When you delete an item from an array everything needs to be shifted versus when you delete an item in a list you just change what the previous element points to.

Common practice is to keep track of first and last item in a linked list, so it would take only O(1) time to delete those.

Arrays allow for random access.

## Two Types of Access are Random and Sequential Access
Sequential Access means reading the elements one by one, starting at the first element.

Linked LIsts can only do sequential access. If you want to read the 10th element of a linked list, you have to read the first 9 elements and follow the links to the 10th element.

Random access means you can jump directly to the 10th element.

## Selection Sort
O(n^2^)





