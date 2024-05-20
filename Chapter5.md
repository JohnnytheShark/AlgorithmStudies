# Hash Tables

A hash function is a function where you put in a string and you get back a number. 

In technical terminology, we'd say that a hash function maps strings to numbers. Requirements for a Hash Function: 
It needs to be consistent. Does not change. 
It should map different words to different numbers. In best case every different word should map to a different number.

Hash Function tells you exactly where the price is stored, so you don't have to search at all! 

## Hash Table
Put a hash function and an array together, and you get a data structure called a hash table. A hash table is the first data structure you'll learn that has some extra logic behind it. Arrays and lists map straight to memory but hash tables are smarter. They use a hash function to intelligently figure out where to store elements.

Hash Tables are probably the most useful complex data structure you'll learn. They're also known as hash maps, maps, dictionaries, and associative arrays. And hash tables are fast!You can get an item from an array instantly.

In python hash tables are called dictionaries. YOu can make a new hash table using the dict function:

book = dict()

Hash table has keys and values. 

## Examples 
Contacts list in your phone
Website to IP Addresses
Caching

## Preventing Duplicates
If it exists in the dictionary then it will not allow for the same key to be added.


Hashes are good for modeling relationships from one thing to another thing
Filtering out duplicates
Caching/Memorizing data instead of making your server do work

## Collisions 
Collisions are bad, and you need to work around them. The simplest approach if multiple keys map to the same slot, start a linked list at that slot.

***You hash function is really important*** A good hash function will give you very few collisions. 

In the average case hash tables take O(1) for everything. O(1) is called constant time. 

||Average Case|Worst Case|
|---||---|---|
|Search| O(1) | O(n)|
|Insert| O(1) | O(n)|
|Delete| O(1) | O(n)|

It doesn't mean instant. It means the time taken will stay the same, regardless of how big the hash table is.

Constant means flat line. That means it doesn't matter whether your hash table has 1 element or 1 billion elements - getting something out of a hash table will take the same amount of time. 

||Hash Tables (Average)| Hash Tables (Worst) | Arrays |Linked Lists|
|---|---|---|---|---|
|Search|O(1)|O(n)|O(1)|O(n)|
|Insert|O(1)|O(n)|O(n)|O(1)|
|Delete|O(1)|O(n)|O(n)|O(1)|

Collisions can be avoided by a low load factor and a good hash function

Typically we will never have to worry about this but allow for the programming language to worry about it. 

## Load Factor 
Load factor of a hash table is easy to calculate

Number of Items in hash table
--------
Total Number of Slots

Hash tables use an array for storage