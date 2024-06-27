# Breadth-First Search
The Algorithm to solve shortest-path problem is called breadth-first search.

1. Model the probelm as a graph
2. Solve the problem using breadth-first search


## Graphs
A graph models a set of connections.
Nodes are the individual circles
The lines connecting them are the Edges.

Graphs are a way to model how different things are connected to one another. Now let's see breadth-first search in action.

## Questions answered
Is there a path from node A to node B (neighbors)? 
What is the shortest path from node A to node B? 

## Queues
Searching items in the order that they're added.

Queues are similar to stacks. You can't access random elements in the queue. Instead there are two only operations, enqueue and dequeue

Enqueue Add an item to the queue
Dequeue Take an item off the queue

Queue is called a FIFO data structure 
First In, First Out 
In contrast a stack is LIFO data structure. Last in, First Out 

Directed Graph - The relationship is only one way.

Undirected graph doesn't have any arrows, and both nodes are each other's neighbors. 

In queues we may also get the terminology push pop. Push is almost always the same thing as enqueue and pop is almost always the same thing as dequeue

Creating a queue in python starts by importing collections: 
from collections import deque

A problem you may encounter is that an infinite loop is created when something is added to the queue twice. 

To prevent loops you have to have a list of names (objects) that you've already checked.

## BIG O
O(V+E) (V for number of vertices, E for number of Edges)

## Topological 
Topological Sort is when the main dependency leads to dependencies that depend on the top dependency.

A Tree is a special type of graph, where no edges ever point back
