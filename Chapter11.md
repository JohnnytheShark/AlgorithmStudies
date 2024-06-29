# Finale 

## Trees
Binary Search Tree Data Structures
For every node, the nodes to its left are smaller in value, and the nodes to the right are larger in value. 

Searching for an element in a binary search tree takes O(log n) time on average and O(n) time in the worst case.

| Operation | Array | Binary Search Tree | 
| --- | --- | --- |
| Search | O(log n) | O(log n) | 
| Insert | O (n) | O (log n) | 
| Delete | O (n) | O (log n) | 

Binary search trees have some downsides tooL for one thing you don't get random access. You can't say "give me the 2nd element of the tree" 

Sometimes trees are inbalanced leaning more towards one side then the other. 

A type of tree that balances itself is the red-black tree. 

## Usage
B-trees, are commonly used to store data in databases.

More advance data structures look at:
- B-trees
- Red-black trees 
- Heaps
- Splay Trees

## Inverted Indexes: 
A hash that maps words to places where they appear. 

## Fourier Transform 
Is one of those rare algorithms: brilliant, elegant, and with a million use cases. The best analogy for the Fourier transform: given a smoothie, the Fourier transform will tell you the ingredients in the smoothie, or to put another way, given a song the trnasform can seperate it into individual frequencies.

It's great for processing signals. YOu can also use it to compress music. 

## Parallel Algorithms: 
Your algorithms need to be changed to run in parallel to be able to run faster.

Things to keep in mind when doing this is: 
- Overhead of managing the parallelism how do you divide the data up then merge the two subsets back into one
- Load Balancing - Suppose you have 10 tasks to do so you give each core 5 tasks. One core might have harder tasks to do then the other. How do you balance the difficult tasks out. 

### MapReduce
The distributed algorithm. It's fine to run a parallel algorithm on your laptop if you need two to four cores, but what if you need hundreds of cores? THen you can write your algorithm to run across multiple machines. The MapReduce algorithm is a popular distributed algorithm. You can use it through the popular open source tool Apache Hadoop. 

#### Why is it useful? 
Suppose you have a table with billions or trillions of rows, and you want to run a complicated SQL query on it. You can't run it on MySql, because it struggles after a few billion rows. Use MapReduce through Hadoop! 

Distributed Algorithms are great when you have a lot of work to do and want to speed up the time required to do it. 

MapReduce in particular is built up from two simple ideas: the map function and the reduce function. 

MapReduce uses these two simple concepts to run queries about data across multiple machines. WHen you have a large dataset, MapReduce can give you an answer in minutes where a traditional database might take hours.

##### Map 
Map function is simple: it takes an array and applies the same function to each item in the array. 

#### Reduce 
The reduce function confuses people sometimes. THe ideas is that you reduce a whole list of items down to one item. With map you go from one array to another. 

With reduce, you transform an array to a single item.


### Bloom Filters and HyperLogLog

Bloom Filters are probablistic data structures. They give you an answer that could be wrong but it is probably correct. 

Bloom Filters give you an answer that's probably correct: 
- False Positives are possible. Example: Google tells you you've already crawled this site. 
- False negatives aren't possible. If it says you haven't then you haven't. 

Bloom filters are great because they take up very little space. 


### HyperLogLog 
Approximates the number of unique elements in a set. Won't give you an exact answer, but it comes very close and uses only a fraction of the memory a task like this would otherwise take.

## SHA Algorithms 
SHA Secure Hash Algorithm
SHA is a hash function, it generates a hash, which is just a short string. SHA hashes are long. Great for determine if files are the same by creating a hash for files. Also great for comparing strings without revealing what the original string was.

Google uses Simhash to detect duplicates while crawling the web. 

A teacher could use Simhash to see whether a student was copying an essay from the web.

## Diffie-Hellman 
Encrypting a message so it can only be read by the person you sent the message to.

This ended up becoming RSA. Think cryptography. 

Solves two: 
1. Both parties don't need to know the cipher. So we don't have to meet and agree to what the cipher should be. 
2. THe encrypted messages are extremely hard to decode.

## Linear Programming
Used to Maximize something given some contraints.

Linear programming uses the Simplex algorithm. It's a complex algorithm. All graph algorithms can be done through linear programming instead. Linear Programming is a much more general framework, and graph probelms are a subset of that.
