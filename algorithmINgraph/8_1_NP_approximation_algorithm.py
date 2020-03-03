

while states_needed:
    best_station = None
    states_covered = set()
    for station,states in station.items():
        covered = states_covered & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

# in first round, we look for a station which contains most states. Then in while circulation, we continue to look for second station which
#contains most states(in fact, after fjrst round, we minimus the ranege we need for states)
# this algorithm means do best choice in one round and then do repetition to get a almost best result.


#NP is used to solve complex question such as factorial function, we can find a almost best solution. just choose one path which
# 1 it is not be choosed
# 2 it is best from now(it means that we need to traverse this list in n times-----time complexity is O(n*n))
# in factorial function it is O(n!)