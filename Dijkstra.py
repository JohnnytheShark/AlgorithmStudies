graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# Get all neighbors for Start like this: 
print(graph['start'].keys())

# Get the weights of those edges
print(graph['start']['a'])
print(graph['start']['b'])

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {} # Finish Node doesn't have any neighbors


# Cost Table for your nodes
infinity = float("inf")

costs = {}

costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents Hash Table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None 

# Need an array to keep track of all the nodes you've already processed, because you don't need to process a node more than once

processed = []

def find_lowest_cost_node(costs):
    lower_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Go through each node
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # If it's the loest cost so far and hasn't been processed yet...
            lowest_cost = cost # ... set it as the new lowest-cost node.
            lowest_cost_node = node 
    return lowest_cost_node 
# Algorithm: 
node = find_lowest_cost_node(costs) # Find the lowest cost node that you haven't processed yet
while node is not None: # If you've processed all the nodes, this while loop is done.
    cost = costs(node)
    neighbors = graph(node) 
    for n in neighbors.keys(): #Go through all the neighbors of this node
        new_cost = costs + neighbors(n) # If it's cheaper to get to this neighbor 
        if costs[n] > new_cost: # by going through this node ...
            costs[n] = new_cost # ... update thecost for this node
            parents[n] = node # This node becomes the new parent for this neighbor
    processed.append(node) # Mark the node as processed
    node = find_lowest_cost_node(costs) # Find the next node to process and loop
