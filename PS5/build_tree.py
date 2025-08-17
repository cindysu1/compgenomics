from compsci260lib import *
from ultrametric_additive import is_ultrametric, is_additive
# from affine_global_aligner_plus import *


def build_tree():
    """
    Read the aligned student sequences, compute the dictionary of distances,
    construct the appropriate phylogenetic tree.
    """

    # Load the aligned student sequences and create the dictionary of distances
    # in the same format as found in ultrametric_additive.py. You will need to
    # convert the student names to integers ("Student_1" -> 1)
    student_dict = get_fasta_dict("students_aligned.fasta")
    students = []
    dist = {}
    for key in student_dict:
        student = key.split("_")
        students.append(int(student[1]))
    for first in range(len(students)):
        f_ind = students[first]
        for sec in range(first+1,len(students)):
            s_ind = students[sec]
            dist[str(f_ind)+","+str(s_ind)] = compute_dist(student_dict["Student_"+str(f_ind)],
                                                                             student_dict["Student_"+str(s_ind)])

    # make a copy of dist to keep values to find most similar/different sequences
    dist_copy = dist.copy()
    # Uncomment the following line to print out the distance dictionary
    print_dist(dist)

    # Check if the distances are ultrametric
    threshold = 0.005  # problem-specific distance threshold for this problem
    if is_ultrametric(dist, threshold=threshold):
        print("\nThe distance is ultrametric.")
    else:
        print("\nThe distance is not ultrametric.")

    # Check if the distances are additive
    if is_additive(dist, threshold=threshold):
        print("\nThe distance is additive.\n")
    else:
        print("\nThe distance is not additive.\n")

    # Report the Newick representation of the phylogenetic tree    
    newick = compute_nj_newick(students,dist)
    print(newick)

    # Call `summarize_alignment` to report the differences between the two
    # most similar and two most different sequence alignments

    # make a dict for just the SARS-CoV-2 genome sequences
    # students 2 and 5 had human coronavirus --> exclude all dists with 2 or 5 in the key
    covid19_dist = {}
    for key in dist_copy:
        if "2" not in key and "5" not in key:
            covid19_dist[key] = dist_copy[key]
    similar = two_min_in_dict(covid19_dist)
    differences = summarize_alignment(student_dict["Student_"+str(similar[0])],
                                      student_dict["Student_"+str(similar[1])])
    print(f'Sequences {similar[0]} and {similar[1]} are the two SARS-CoV-2 sequences that are the most similar, '
          f'and they have {differences[0]} matches, {differences[1]} mismatches, and {differences[2]} gaps.')
    diff_sars = two_max_in_dict(covid19_dist)
    differences = summarize_alignment(student_dict["Student_"+str(diff_sars[0])],
                                      student_dict["Student_"+str(diff_sars[1])])
    print(f'Sequences {diff_sars[0]} and {diff_sars[1]} are the two SARS-CoV-2 sequences that are the most different, '
          f'and they have {differences[0]} matches, {differences[1]} mismatches, and {differences[2]} gaps.')
    diff_overall = two_max_in_dict(dist_copy)
    differences = summarize_alignment(student_dict["Student_"+str(diff_overall[0])],
                                      student_dict["Student_"+str(diff_overall[1])])
    print(f'Sequences {diff_overall[0]} and {diff_overall[1]} are the two sequences that are the most different overall,'
          f'and they have {differences[0]} matches, {differences[1]} mismatches, and {differences[2]} gaps.')

    # code to find alignments between Students 3 + 7 and Students 1 + 7
    # commented out because it calls a file that is not required in submission

    # load in original student sequences
    # student_seq = get_fasta_dict("students.fasta")
    # gap_penalty = 1
    # affine_penalty = 11
    # # run affine global aligner on Students 7 and 3
    # # use helper method to report optimal score, top-most alignment, and bottom-most alignment
    # differences = summarize_alignment(student_dict["Student_3"],
    #                                   student_dict["Student_7"])
    # print(f'Sequences 3 and 7 have {differences[0]} matches, {differences[1]} mismatches, and {differences[2]} gaps.')
    # report_affine_protein_alignment(student_seq["Student_3"], student_seq["Student_7"], gap_penalty,
    #                                 affine_penalty, "Student_3", "Student_7")
    # # run affine global aligner on Students 7 and 3
    # # use helper method to report optimal score, top-most alignment, and bottom-most alignment
    # differences = summarize_alignment(student_dict["Student_1"],
    #                                   student_dict["Student_7"])
    # print(f'Sequences 1 and 7 have {differences[0]} matches, {differences[1]} mismatches, and {differences[2]} gaps.')
    # report_affine_protein_alignment(student_seq["Student_1"], student_seq["Student_7"], gap_penalty,
    #                                 affine_penalty, "Student_1", "Student_7")

def compute_nj_newick(seq_names, dist):
    """
    Performs Neighbor Joining to construct the phylogenetic tree from a
    distance table.

    Args:
        seq_names (list of ints): representing the sequence names.
                e.g. [1, 2, ..] for ["Student_1", "Student_2", ...]

        dist (dict of str to float): distance table mapping pairs of students 
            to float distances. Refer to ultrametric_additive.py for examples of
            distance tables.

    Returns:
        the Newick representation of the phylogenetic tree as a string
    """

    # ------------- Implementation of the Neighbor Joining algorithm ----------
    # Keeping track of variable names:

    # dist              - dictionary containing the computed pair-wise
    #                     distances between nodes
    # node_list         - array containing the list of current nodes (L), which
    #                     gradually decreases in size while iterating to build 
    #                     the tree
    # avg_dist          - dictionary containing the averaged distances 
    #                     (r values) for all of the current nodes (those in L)
    # D                 - dictionary containing the "adjusted" pairwise
    #                     distances between nodes
    # newick            - dictionary to maintain the Newick representation of
    #                     each leaf node or subtree

    # ------------- Initialization: -------------------------------------------

    node_list = seq_names  # L = the list of current nodes
    newick = {}
    for i in range(1, len(node_list)+1):
        newick[i] = "" + str(i)

    avg_dist = {}  # to hold the averaged distances (r values) for all current nodes

    for i in range(1, len(node_list) + 1):
        
        avg_dist[i] = 0       
        for j in range(1, len(node_list) + 1):
            
            if i != j:
                avg_dist[i] += dist["%d,%d" % (i,j)] if i<j else \
                               dist["%d,%d" % (j,i)]
        
        avg_dist[i] = avg_dist[i] / (len(node_list) - 2)

    max_node = len(node_list)  # the maximum key used for a node
    
    # -------------- Iteration to build the tree --------------------

    # As long as the list contains more than 2 nodes, iterate 
    while len(node_list) > 2:
        
        # ---------- Begin your code -------------
   
        # Compute the "adjusted" distances between nodes using the original
        # distances (from dist) and averaged distances (from avg_dist)

        # Let D be the dict to contain "adjusted" distances
        D = {}

        # Loop through each pair of nodes as entered in the dist dict
        # Use the entries from the avg_dist dict and calculate entries
        # for the D dict
        # nodes added to dist dict in the order they are listed in node_list, use indices because some nodes will be
        # deleted
        for i_ind in range(len(node_list)):
            i = node_list[i_ind]
            for j_ind in range(i_ind+1, len(node_list)):
                j = node_list[j_ind]
                # use adjusted distance formula
                D["%d,%d" % (i,j)] = dist["%d,%d" % (i,j)] - (avg_dist[i] + avg_dist[j])
        # print(D)

        # Pick the pair i,j in node_list for which adjusted distance D_ij is
        # minimal.
        # You may find the function two_min_in_dict helpful.
        (i,j) = two_min_in_dict(D)  # Replace with your pair
        # print(i,j)

        # Define a new node m and set dist[k,m] for all nodes k in node_list
        # as (dist[i,k] + dist[j,k] - dist[i,j]) / 2

        # max_node had been earlier set to the largest key used for a node
        m = max_node + 1
        max_node += 1
        for ind in range(len(node_list)):
            k = node_list[ind]
            if k != i and k != j:
                # only one dist is stored for each pair, so find which one is stored
                dik = dist["%d,%d" % (i,k)] if i<k else dist["%d,%d" % (k,i)]
                djk = dist["%d,%d" % (j,k)] if j<k else dist["%d,%d" % (k,j)]
                dij = dist["%d,%d" % (i,j)] if i<j else dist["%d,%d" % (i,j)]
                dist["%d,%d" % (k,m)] = (dik + djk - dij)/2

        # ---------- End your code -------------
   
        # Add the new node m to the Newick format representation of the tree
        # with edges of lengths 
        # dim = (dist[i,j] + avg_dist[i] - avg_dist[j])/2
        # djm = dist[i,j] - d[i,m], 
        # joining m to i and j
        
        if dist["%d,%d" % (i, j)] > 0:
            d_im = (dist["%d,%d" % (i, j)] + avg_dist[i] - avg_dist[j]) / 2
            d_jm = dist["%d,%d" % (i, j)] - d_im
        else:
            d_im = d_jm = 0

        newick[m] = ("(" + newick[i] + ":" + "%.7f" % d_im + ","
                     + newick[j] + ":" + "%.7f" % d_jm + ")")

        # Remove i and j from node_list and add m
        temp = []
        for idx in range(0, len(node_list)):
            
            if node_list[idx] != i and node_list[idx] != j:
                temp.append(node_list[idx])
   
        temp.append(m)
        
        node_list = list(temp)
        
        # Update the r terms, based on changes rather than recomputing from scratch
        if len(node_list) > 2:
            avg_dist[m] = 0
            
            for ind in range(0, len(node_list)-1):
                
                k = node_list[ind]
                avg_dist[k] = avg_dist[k] * (len(node_list)-1)
                avg_dist[k] -= dist["%d,%d" % (k, i)] if k < i \
                    else dist["%d,%d" % (i, k)]
                avg_dist[k] -= dist["%d,%d" % (k, j)] if k < j \
                    else dist["%d,%d" % (j, k)]
                avg_dist[k] += dist["%d,%d" % (k, m)]

                avg_dist[k] /= len(node_list)-2
                avg_dist[m] += dist["%d,%d" % (k, m)]

            avg_dist[m] = avg_dist[m] / (len(node_list)-2)
        
        # Remove any elements from the dict that contain nodes i or j
        delete_from_dict(dist, i, j)
        delete_from_dict(D, i, j)
        delete_from_dict(newick, i, j)
        delete_from_dict(avg_dist, i, j)

    # Return the Newick representation, joining together the final two nodes
    return ("(" + newick[node_list[0]] + ":" + 
            "%.7f" % (list(dist.values())[0]) +
            "," + newick[node_list[1]] + ":0);\n")


def summarize_alignment(seq1, seq2):
    """
    Summarize the alignment between two sequences by computing the number of
    matches, mismatches, and gaps. This code will contain similar logic to 
    the provided `compute_dist` function.

    Note: that we performed multiple sequence alignment to obtain the 
    aligned sequences in students.aligned.fasta. So, for any pair of sequences, 
    you may find a gap at the same place in the two aligned sequences. Gaps 
    should only be counted if they are matched with a non-gap character 
    (ignore a gap aligned to a gap).

    Args:
        seq1 (str): the first sequence, extracted from a multiple sequence
                    alignment
        seq2 (str): the second sequence, extracted from a multiple sequence
                    alignment

    Returns:
        a tuple of the number of (matches, mismatches, gaps) between the two
        sequences
    """
    # create counts for the number of gaps, mismatches, and matches in the alignment
    gaps = 0
    mismatches = 0
    matches = 0
    for ind in range(len(seq1)):
        # if both sequences have a gap ignore
        if seq1[ind] == "-" and seq2[ind] == "-":
            continue
        # check for gaps
        elif seq1[ind] == "-" or seq2[ind] == "-":
            gaps += 1
        # know there is not a gap, so now check for mismatces
        elif seq1[ind] != seq2[ind]:
            mismatches += 1
        # check for match, could also just use an else
        elif seq1[ind] == seq2[ind]:
            matches += 1

    # return the number of matches, mismatches and gaps as a tuple
    return (matches, mismatches, gaps)

########################################################################
# Provided functions for this problem
########################################################################


def compute_dist(seq1, seq2):
    """Returns the distance between two sequences. The distance is computed
    as the ratio between the number of mismatches and the total number
    of matches or mismatches.

    Args:
        seq1 (string) - first sequence
        seq2 (string) - second sequence

    Returns:
        the ratio of mismatches over the total number of matches or mismatches
        as a float
    """
    mismatch = 0
    match_or_mismatch = 0
    
    for i in range(len(seq1)):
        if seq1[i] == "-" or seq2[i] == "-":
            continue
        elif seq1[i] == seq2[i]:
            match_or_mismatch += 1
        else:
            mismatch += 1
            match_or_mismatch += 1

    return float(mismatch)/match_or_mismatch


def print_dist(dist):
    """
    Print the distance table
    """

    idx = [int(i.split(",")[0]) for i in list(dist.keys())]
    idx.extend([int(i.split(",")[1]) for i in list(dist.keys())])
    max_idx = max(idx)

    print("\t", end=" ")
    for col in range(2, max_idx + 1):
        print("{:>7}".format(col), end=" ")
    print() 

    for row in range(1, max_idx):
        print("%d\t" % row, end=" ")
        for col in range(2, row+1):
            print("       ", end=" ")
        for col in range(row+1, max_idx + 1):
            print("{:>7.4f}".format(dist[str(row)+","+str(col)]), end=" ")
        print() 

########################################################################
# Functions used by Neighbor Joining algorithm
########################################################################


def delete_from_dict(dictionary, i, j):
    """Deletes the dict entries with keys that contain i or j."""
      
    for k in list(dictionary.keys()):
        ks = [int(_) for _ in str(k).split(",")]
        if i in ks or j in ks:
            del dictionary[k]


def min_in_dict(wiki):
    """Returns the key associated with the minimum value in the dict."""
    import operator
    return min(iter(wiki.items()), key=operator.itemgetter(1))[0]


def two_min_in_dict(dictionary):
    import operator
    sorted_dict = sorted(iter(dictionary.items()), key=operator.itemgetter(1))
    element = sorted_dict[0][0]  # get the first element of the tuple
    (i, j) = element.split(",")
    return int(i), int(j)

def two_max_in_dict(dictionary):
    import operator
    sorted_dict = sorted(iter(dictionary.items()), key=operator.itemgetter(1), reverse = True)
    element = sorted_dict[0][0]  # get the first element of the tuple
    (i, j) = element.split(",")
    return int(i), int(j)

if __name__ == "__main__":
    build_tree()
