"""Greedy Algorithm

This will use a subset of states to define its point

"""

# STATES
states_needed = set(["mt", "wa", "ct", "ma", "nv", "ut", "ca", "az"])

# STATIONS

stations = {}
stations["kone"] = set(["ma", "nv", "ut"])
stations["ktwo"] = set(["wa", "ma", "mt"])
stations["kthree"] = set(["ct", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
# a set of all states this station covers that haven't been covered yet
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states  # set intersection!
    # does the covered station do a better job at covering states?
        if len(covered) > len(states_covered):
            best_station = station  # if so, make it the best station
            states_covered = covered
states_needed -= states_covered
final_stations.add(best_station)

print(final_stations)
