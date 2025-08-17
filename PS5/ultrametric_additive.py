from compsci260lib import *


def solve_ultrametric_additive():
    
    # Distance metrics for table 1 and table 2
    dist_1 = {"1,2" : 0.3, "1,3" : 0.7, "1,4" : 0.7,
              "2,3" : 0.6, "2,4" : 0.6, "3,4" : 0.6} # fill in table 1 here

    dist_2 = {"1,2" : 0.9, "1,3" : 0.4, "1,4" : 0.6, "1,5" : 0.9,
              "2,3" : 0.9, "2,4" : 0.9, "2,5" : 0.4,
              "3,4" : 0.6, "3,5" : 0.9,
              "4,5" : 0.9}


    # Check if dist_1 and dist_2 are ultrametric and additive by
    # calling is_ultrametric and is_additive with the default
    # threshold value (1e-4).
    #
    if is_ultrametric(dist_1):
        print("dist_1 is ultrametric")
    if is_additive(dist_1):
        print("dist_1 is additive")
    if is_ultrametric(dist_2):
        print("dist_2 is ultrametric")
    if is_additive(dist_2):
        print("dist_2 is additive")
    #    

    # Construct the ATPA synthase distance metric table
    atpa_table = {"HUMAN,ECOLI": 0.5, "HUMAN,BACSU": 0.5, "HUMAN,MOUSE": 0.1, "HUMAN,YEAST": 0.4, "HUMAN,SCHPO":0.4,
           "ECOLI,BACSU": 0.3, "ECOLI,MOUSE": 0.5, "ECOLI,YEAST": 0.5, "ECOLI,SCHPO": 0.5,
           "BACSU,MOUSE": 0.5, "BACSU,YEAST": 0.5, "BACSU,SCHPO": 0.5,
           "MOUSE,YEAST": 0.4, "MOUSE,SCHPO": 0.4,
           "YEAST,SCHPO": 0.3} #  fill in ATPA synthase distance metric table

    # Determine if the ATPA synthase distance metrics
    # are ultrametric and additive using the default
    # threshold value (1e-4).
    if is_ultrametric(atpa_table):
        print("The distance metric for ATP synthases is ultrametric")
    if is_additive(atpa_table):
        print("The distance metric for ATP synthases is additive")


def is_ultrametric(dist, threshold=1e-4):
    """Check that a set of pairs of point distances are ultrametric.

    Note: When making comparisons between distances, use `is_almost_equal` with
    the input parameterized threshold. This will be useful for subsequent
    problems where `is_ultrametric` is called. e.g. When comparing x and y, 
    also pass the threshold parameter: is_almost_equal(x, y, threshold).

    Args:
        dist (dict): exhaustive dict of pairs of points mapped to distances. 
        e.g.
            {"1,2" : 0.5, "1,3" : 0.1, "2,3" : 0.6}
        threshold (float): maximium difference in which numeric values are 
            considered equal
    Returns:
        (bool) True if the given distance metric is an ultrametric,
    False otherwise."""

    # create a list to store the sequence numbers/names
    sequences = []
    # find the number of nodes and their numbers based on the keys of the dict
    for key in dist:
        nodes = key.split(",")
        for node in nodes:
            # do not store duplicates
            if node not in sequences:
                sequences.append(node)
    # iterate through all triplets of sequences
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            for k in range(j + 1, len(sequences)):
                    # find all the pairwise distances
                    dij = dist[sequences[i] + "," + sequences[j]]
                    dik = dist[sequences[i] + "," + sequences[k]]
                    djk = dist[sequences[j] + "," + sequences[k]]
                    # sort vals by distance value
                    vals = [dij, dik, djk]
                    vals = sorted(vals)
                    # compare largest two values
                    if not is_almost_equal(vals[1], vals[2], threshold):
                        # print the triplet that violates ultrameticity
                        print(f'This distance metric is not ultrametric. The triplet {sequences[i]}, {sequences[j]}, '
                              f'and {sequences[k]} (distances {dij}, {dik} and {djk}) violate ultrametricity')
                        return False
    return True



def is_additive(dist, threshold=1e-4):
    """Check that a set of pairs of point distances are additive.

    Note: When making comparisons between distances, use `is_almost_equal` with
    the input parameterized threshold. This will be useful for subsequent
    problems where `is_ultrametric` is called. e.g. When comparing x and y, 
    also pass the threshold parameter: is_almost_equal(x, y, threshold).

    Args:
        dist (dict): exhaustive dict of pairs of points mapped to distances. 
        e.g.
            {"1,2" : 0.5, "1,3" : 0.1, "2,3" : 0.6}
        threshold (float): maximium difference in which numeric values are 
            considered equal

    Returns:
        (bool) Return True if the given distance metric is additive, 
        False otherwise."""

    # create a list to store the sequence names/numbers
    sequences = []
    # find the number of nodes and their numbers based on the keys of the dict
    for key in dist:
        nodes = key.split(",")
        for node in nodes:
            # do not store duplicates
            if node not in sequences:
                sequences.append(node)
    # iterate through all quartets of sequences (i < j < k < l)
    for i in range (len(sequences)):
        for j in range(i+1, len(sequences)):
            for k in range(j+1, len(sequences)):
                for l in range(k+1, len(sequences)):
                    # calculate all pairwise distances
                    dij = dist[sequences[i] + "," + sequences[j]]
                    dik = dist[sequences[i] + "," + sequences[k]]
                    dil = dist[sequences[i] + "," + sequences[l]]
                    djk = dist[sequences[j] + "," + sequences[k]]
                    djl = dist[sequences[j] + "," + sequences[l]]
                    dkl = dist[sequences[k] + "," + sequences[l]]
                    # sort by additivity metrics summing up pairwise distances
                    vals = [dij+dkl, dik+djl, dil+djk]
                    vals = sorted(vals)
                    if not is_almost_equal(vals[1], vals[2], threshold):
                        print(f'This distance metric is not additive. The quadruplet {i+1}, {j+1}, {k+1}, and {l+1} ('
                              f'distances {vals[0]}, {vals[1]} and {vals[2]}) violate ultrametricity')
                        return False
    return True


def is_almost_equal(num_1, num_2, threshold):
    """
    Return true if the difference between the two parameters is negligible
    enough that the parameters can be considered equal.
    """
    return abs(num_1 - num_2) <= threshold


if __name__ == '__main__':
    solve_ultrametric_additive()
