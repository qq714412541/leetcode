graph = {}
graph['you'] = ['aa','bb','cc']
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}


infinity = float('inf')  #python float('inf') stands for positive infinity,  float('-inf') stand for negative infinity

cost  = {}#cost is designed to save the cost of current path
cost['a'] = 6
cost['b'] = 2
cost['fin'] = infinity

parents = {}#parents is designed to save parents' information of current path
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None  #because current path has not reach this node

processed = []#record what i have processed

costs = {}


def find_lowest_path(costs):
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors
            if cost[n] >new_cost:
                cost[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return  costs

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#idea: find lowest costs(in all), we need to set a lowest node from start, then we find its neighbors and cost, if under neighbors' path we can
# get a shorter path, we turn cost to be the sum. Then we change it to next lowest node(except what we have choosed), and we can do repetition
# until find all lowest path in costs.
#as for looking for lowest node, we can search in costs from samllest to biggest until traversing all the data(in fact,
# the elements in costs change in every repetiton, and it used to be changed in big element because above algorithm
# ,)