graph = {}
parents = {}
processed = {}

def find_lowest_path(costs):
    node = find_lowest_cost(costs)
    while node is not None:
        neighbors = graph(node)
        cost = costs[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_path(costs)

    return costs

def find_lowest_cost(costs):
    lowest = float('inf')
    for n in costs.keys():
        cost = costs[n]
        if cost < lowest:
            lowest = cost
            lowest_node = n

    return lowest_node

