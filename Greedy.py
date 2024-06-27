states_needed = set(['mt', 'wa','or','id','nv','ut','ca','az']) # You pass an array in, and it gets convereted to a set
# Sets are nice since they can't have duplicates.


stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items(): 
        covered = states_needed & states_for_station # New Syntax! This is called a set intersection
        if len(covered) > len(states_covered):
            best_station = station 
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)

# Covered is a set of states that were in both states_needed and states_for_station. So covered is the set of uncovered states that this station covers! Next you check whether the station coveres more states than the current best_station


# Example of Set Manipulations: 

fruits = set(['avocado','tomato','banana'])
vegetables = set(['beets', 'carrots', 'tomato'])
fruits | vegetables # Set Union 
fruits & vegetables # Set Intersection 
fruits - vegetables # Set Difference