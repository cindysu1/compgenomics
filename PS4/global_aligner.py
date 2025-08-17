from aligner_helpers import *
from compsci260lib import *


def run_global_aligner():
    """
    Given two sequences of either DNA or amino acids, initialize the
    appropriate substitution matrix, run the global aligner and report the
    optimal alignment score.
    """
    # test case to compare to manual table
    seq1 = "CGATCGAT"
    seq2 = "GCCATT"
    # set match, mismatch, and gap scores
    match = 2
    mismatch = -1
    gap_penalty = 2

    seq_type = validate_sequences(seq1, seq2)
    if seq_type == 1:
        # Both the sequences are DNA sequences so use the scores for match and
        # mismatch
        subst_matrix = create_subst_matrix_dna(match, mismatch)
    elif seq_type == 2:
        # Both the sequences are protein sequences so read in the BLOSUM62
        # substitution matrix
        subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
    else:
        sys.exit("Input sequences are of different types: not both DNA or both protein")

    # Obtain a dictionary of scores for aligning a pair of characters
    subst_dict = create_subst_matrix_dict(subst_matrix)

    optimal_score = solve_global_aligner(seq1, seq2, subst_dict, gap_penalty)

    # Report the optimal global alignment score

    print(f'The optimal global alignment score is {optimal_score}')
    #


def solve_global_aligner(seq1, seq2, subst_dict, gap_penalty):
    """The overall procedure for collecting the inputs, running the aligner,
    and displaying the table and return the optimal alignment score

    Args:
        seq1 (str): first sequence to be aligned
        seq2 (str): second sequence to be aligned
        subst_dict (dictionary string -> int): dictionary representation of the
            substitution matrix
        gap_penalty (int): penalty for a column containing a gap char (g: use a
            positive value because this value will be subtracted)

    Returns:
        (int) the optimal alignment score
    """

    # Initialize the DP table's data structure
    # as a list of lists of ints
    dp_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]

    # Compute the score of the optimal global alignment
    max_value = global_aligner(seq1, seq2, subst_dict, gap_penalty, dp_table)

    # Display the dp table
    display_dp_table(seq1, seq2, dp_table)

    return max_value


def global_aligner(seq1, seq2, subst_dict, gap_penalty, dp_table):
    """A dynamic programming algorithm that takes two sequences and returns the
    score of the optimal alignment.

    Args:
        seq1 (str): first sequence to be aligned
        seq2 (str): second sequence to be aligned
        subst_dict (dict): substitution matrix stored as a dictionary, with
            keys that reference the two characters being aligned, and values
            being the corresponding score.  See the create_subst_matrix_dict()
            function to know how this works.

        gap_penalty (int): linear gap penalty (penalty per gap character); this
            value should be positive because we will subtract it

        dp_table (list of list of ints): dynamic programming table, in the
            structure of dp_table[i][j]

    Returns:
        (int): the optimal alignment score
    """

    # the dp table has len(seq1) + 1 rows and len(seq2) + 1 columns
    I = len(dp_table)      # so I is 1 more than m
    J = len(dp_table[0])   # so J is 1 more than n

    # Initialize the dp table with solutions to base cases using linear gap
    # penalty

    for i in range(1,I):
        # base case for empty seq1 vs each position in seq2, add gap penalty for each additional gap
        dp_table[i][0] = dp_table[i-1][0] - gap_penalty
    for j in range(1, J):
        # base case for empty seq2 vs each position in seq1, add gap penalty for each additional gap
        dp_table[0][j] = dp_table[0][j-1] - gap_penalty

    # Compute the scores for the rest of the matrix,
    # i.e. all the elements in dp_table[i][j] for i > 0 and j > 0.

    # need cells above, to the left of, and diagonally up and to the left to be filled to solve for a cell
    # can iterate row by row down the table to fill in
    for i in range(1,I):
        for j in range(1,J):
            # type 1 when seq 1 and seq 2 both have nucleotides in this position, previous is diagonal
            # account for difference in sequence index and table indices
            match = seq1[i-1] + seq2[j-1]
            t1 = subst_dict[match] + dp_table[i-1][j-1]
            # type 2 when seq 1 has a nucleotide and seq 2 has a gap, previous is to the left
            t2 = - gap_penalty + dp_table[i-1][j]
            # type 3 when seq 2 has a nucleotide and seq 1 has a gap, previous is above
            t3 = - gap_penalty + dp_table[i][j-1]
            # maximize score for this position by finding max of t1,t2,t3
            dp_table[i][j] = max(t1,t2,t3)

    # The optimal score is found at the lower right corner of the dp table:
    return dp_table[I-1][J-1]



if __name__ == "__main__":
    run_global_aligner()
