# This is for the code for Dijkstra's Algorithm.

"""Graph Used

        A
       / \
    6 /   \ 1
     /     \
START       FINISH
     \     /
    2 \   / 5
       \ /
        B

To code this example, we will need 3 hash tables, Graph, Costs and Parents

"""

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}  # this node doesn't have any neighbors

# COSTS

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# PARENTS

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# keep track of nodes you've already processed

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # go through each node
        costs = costs[node]
        # if its the lowest cost so far and hasn't been processed yet
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # set it as the new lowest cost node
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:  # if you've processed all the nodes, the while loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # go through all the neighbors of this node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # if it's cheaper to get to this neighbor by going through this node
            costs[n] = new_cost  # update the cost for this node
            # this node becomes the new parent for this neighbor
            parents[n] = node
    processed.append(node)  # mark the node as processed
    # find the next node to process, and loop
    node = find_lowest_cost_node(costs)
