# Dijkstra's Algorithm
Finds you the fastest path, instead of the shortest path like Breadth First Search.

## Four Steps
1. Find the "Cheapest" Node. This is the node you can get to in the least amount of time.
2. Update the costs of the neighbors of this node.
3. Repeat until you've done this for every node in the graph. 
4. Calculate the Final Path

## Terminology: 
Dijkstra's algorithm, each edge(line) has a number associated  with it called a weight. 

A graph with weights is called a weighted graph. A graph without weights is called an unweighted group.

Undirected graph means both nodes point to each other. (Cycle) 

Dijkstra's algorithm only works on graphs with no cycles, or on graphs with a positive weight cycle 

## Example 

Say we are trading an item upwards from a goldfish up to a piano. 

Steps: 
1. Create a table ranking how expensive each item is. (This table will be updated as the algorithm continues)

2. Figure out how long it takes to get to its neighbors (the cost)

3. Repeat but with the new cheaper node as the parent. 


## Negative Weights 
We can not do Dijkstra's algorithm if there are negative-weight edges. Negative-weight edges break the algorithm.

## Coding this example:

./Dijkstra.py 

### Code Walkthrough: 
1. While we have nodes to process 
2. Grab the node that is closest to the start 
3. Update costs for its neighbors 
4. If any of the neighbor's costs were updated, update the parents too
5. Mark this node as processed 

## Recap
Breadth-first search is used to calculate the shortest path for an unweighted graph.

Dijkstra’s algorithm is used to calculate the shortest path for a weighted graph.

Dijkstra’s algorithm works when all the weights are positive.

If you have negative weights, use the Bellman-Ford algorithm.