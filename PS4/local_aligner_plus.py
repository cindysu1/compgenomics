from compsci260lib import *
from aligner_helpers import *


def run_local_aligner_plus():
    """Locally align O18381.fasta and P63015.fasta and report the
    optimal score and optimal local alignment information.
    """
    # load in protein sequences from fasta files
    fasta_dict = get_fasta_dict("P63015.fasta")
    P63015_seq = fasta_dict["sp|P63015|PAX6_MOUSE Paired box protein Pax-6 OS=Mus musculus OX=10090 GN=Pax6 PE=1 SV=1"]
    fasta_dict = get_fasta_dict("O18381.fasta")
    O18381_seq = fasta_dict[
        "sp|O18381|PAX6_DROME Paired box protein Pax-6 OS=Drosophila melanogaster OX=7227 GN=ey PE=1 SV=3"]
    # set gap penalty
    gap_penalty = 8
    # create protein substitution matrix
    subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
    subst_dict = create_subst_matrix_dict(subst_matrix)
    # find an optimal alignment and other information
    alignment = solve_local_aligner_plus(P63015_seq, O18381_seq, subst_dict, gap_penalty)
    # report optimal score, number of locations achieving this score, and one optimal alignment
    print(f'The optimal score of the local alignment of P63015 and O18381 is: {alignment[0]}.')
    print(f'The total number of locations in the table achieving this optimal score is {len(alignment[1])}, '
          f'and the locations are {alignment[1]}.')
    print(f'One optimal alignment aligns nucleotide {alignment[2][0]}-{alignment[2][1]} with nucleotides '
          f'{alignment[3][0]}-{alignment[3][1]} (indices are inclusive)')
    print_alignment(alignment[4], alignment[5], seq1_start=alignment[2][0], seq2_start=alignment[3][0], name1="P63015",
                    name2="O18381")


def solve_local_aligner_plus(seq1, seq2, subst_dict, gap_penalty):
    """The procedure for collecting the inputs, running the aligner,
    and returning the score and optimal alignment(s).

    Note that for each returned local alignment, starting positions
    also need to be returned. These are the positions of the first
    character in each aligned sequence relative to the original
    sequence.

    Args:
        seq1 (str): first sequence to match
        seq2 (str): second sequence to match
        subst_dict (dictionary string -> int): dictionary
            representation of the substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character);
            this value should be positive because we will subtract it

    A max score may be in multiple locations, so return the optimal
    score, the locations of all the maxima, and any one optimal
    alignment as a tuple.

    Returns a tuple of:
        (the optimal alignment score as an int,

         the locations of the maxima in the dp table as a list of
         tuples. these positions will include the offset of the
         initialized penalty row and column, so that location (i,j)
         refers to the i-prefix of X and the j-prefix of Y, just as in
         lecture,

         tuple for an optimal alignment)

        The alignment will be in the form:

              (tuple of indices of the characters of the first aligned
               sequence used in the alignment),

              (tuple of indices of the characters of the second aligned
               sequence used in the alignment),

              the first aligned sequence as a string,

              the second aligned sequence as a string)

        As an example with the sequences:

            Sequence 1: TAG
            Sequence 2: TAAGATAAG

        A possible return may be:

            (11, # the optimal score

             # the two maximal locations in the dp table
             [(3, 4), (3, 9)],

             # one possible alignment:
             ((1, 3), # the nt positions mapping TA-G from TAG
              (1, 4), # the nt positions mapping TAAG from TAAGATAAG

              "TA-G", "TAAG") # the sequences of the alignment
            )

        Corresponding to two maxima with an optimal
        alignment score of 11.
    """
    #
    # Initialize the DP table's data structure
    # as a list of lists of ints, later updated to tuples of (int,(pointers))
    dp_table = [[(0, [])] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

    # the dp table has len(seq1) + 1 rows and len(seq2) + 1 columns
    I = len(dp_table)  # so I is 1 more than m
    J = len(dp_table[0])  # so J is 1 more than n

    # need cells above, to the left of, and diagonally up and to the left to be filled to solve for a cell
    # can iterate row by row down the table to fill in
    # store the optimal score and its coordinates
    opt_score = (float('-inf'),(-1,-1))
    # store locations that achieve the optimal score
    locations = []
    for i in range(1, I):
        for j in range(1, J):
            # type 1 when seq 1 and seq 2 both have nucleotides in this position, previous is diagonal
            # account for difference in sequence index and table indices
            match = seq1[i - 1] + seq2[j - 1]
            t1 = subst_dict[match] + dp_table[i - 1][j - 1][0]
            # type 2 when seq 1 has a nucleotide and seq 2 has a gap, previous is above
            t2 = - gap_penalty + dp_table[i - 1][j][0]
            # type 3 when seq 2 has a nucleotide and seq 1 has a gap, previous is to the left
            t3 = - gap_penalty + dp_table[i][j - 1][0]
            # maximize score for this position by finding max of t1,t2,t3
            max_score = max(t1, t2, t3, 0)
            # increment number of locations an optimal alignment is found at
            if max_score == opt_score[0]:
                locations.append((i,j))
            # only update opt_score if a higher score is found e.g. keep old score in ties
            # reset number of locations to 1 when a new optimal score is found
            if max_score > opt_score[0]:
                opt_score = (max_score, (i,j))
                locations.clear()
                locations.append((i,j))
            # pointers will remain empty if the optimal fragment ends (0 is max and not equal to t1,t2,t3)
            pointers = []
            # append corresponding pointers to pointers array, add in order of top to bottom alignment
            # type 2 column results in the previous cell being above, which is the top-most
            if max_score == t2:
                # pointers.append((i-1, j))
                pointers.append(2)
            if max_score == t1:
                # pointers.append((i - 1, j - 1))
                pointers.append(1)
            if max_score == t3:
                # pointers.append((i, j-1))
                pointers.append(3)
            dp_table[i][j] = (max_score, pointers)
    # display_dp_table_plus(seq1, seq2, dp_table)
    # trace back top-most alignment
    row = opt_score[1][0]
    col = opt_score[1][1]
    # optimal score is given from the end of the local alignment, store values
    end1 = row
    end2 = col
    al1_top = ""
    al2_top = ""
    # with local alignment stop when you reach the beginning of both sequences or end of local alignment
    while (row > 0 or col > 0) and len(dp_table[row][col][1]) > 0:
        # take first element of pointer list since we can return any optimal alignment
        type = dp_table[row][col][1][0]
        # depending on the type, add the correct characters to the alignments and adjust the row and column values
        if type == 2:
            al1_top = seq1[row - 1] + al1_top
            al2_top = "-" + al2_top
            row -= 1
        elif type == 1:
            al1_top = seq1[row - 1] + al1_top
            al2_top = seq2[col - 1] + al2_top
            row -= 1
            col -= 1
        elif type == 3:
            al1_top = "-" + al1_top
            al2_top = seq2[col - 1] + al2_top
            col -= 1
    # the local alignment may end anywhere in the table, so store the values of row and col
    start1 = row
    start2 = col
    # example format of return tuple:
    # print(dp_table[I-1][J-1][0])
    # add 1 to the start values to make them 1-indexed.
    return (opt_score[0], locations, (start1+1, end1), (start2+1, end2), al1_top, al2_top)

def display_dp_table_plus(seq1, seq2, dp_table):
    """A function that displays the dp table with pointers once it's been computeds."""

    # Add gap character in front of the two sequences
    seq1 = "-" + seq1
    seq2 = "-" + seq2

    form = ("{:>6}" * (len(seq2) + 1))
    header = form.format(*(" " + seq2))
    print(header)

    for i in range(len(seq1)):
        data = []
        for j in range(len(seq2)):
            data.append(dp_table[i][j][0])
        row = form.format(*([seq1[i]] + data))
        print(row)

if __name__ == "__main__":
    run_local_aligner_plus()
