from aligner_helpers import *
from compsci260lib import *
from global_aligner import *


def run_global_aligner_plus():
    """Generate the optimal global alignments between:

        2.c)
        atpa_Hs.fasta, atpaEc.fasta

        2.f)
        atpaMm.fasta, atpaHs.fasta
        atpaMm.fasta, atpaEc.fasta

        atpaBs.fasta, atpaHs.fasta
        atpaBs.fasta, atpaEc.fasta

        atpaMm.fasta, atpaBs.fasta

    For each alignment, report the optimal alignment score,
    the top-most alignment, and the bottom-most alignment.
    """
    # load in sequences of all 4 proteins for parts c and f
    hs_path = "atpa_Hs.fasta"
    fasta_dict = get_fasta_dict(hs_path)
    atpa_hs = fasta_dict[("sp|P25705|ATPA_HUMAN ATP synthase subunit alpha, mitochondrial OS=Homo sapiens OX=9606 GN=ATP5F1A PE=1 SV=1")]
    ec_path = "atpa_Ec.fasta"
    fasta_dict = get_fasta_dict(ec_path)
    atpa_ec = fasta_dict["sp|P0ABB0|ATPA_ECOLI ATP synthase subunit alpha OS=Escherichia coli (strain K12) OX=83333 GN=atpA PE=1 SV=1"]
    mm_path = "atpa_Mm.fasta"
    fasta_dict = get_fasta_dict(mm_path)
    atpa_mm = fasta_dict["sp|Q03265|ATPA_MOUSE ATP synthase subunit alpha, mitochondrial OS=Mus musculus OX=10090 GN=Atp5f1a PE=1 SV=1"]
    bs_path = "atpa_Bs.fasta"
    fasta_dict = get_fasta_dict(bs_path)
    atpa_bs = fasta_dict["sp|P37808|ATPA_BACSU ATP synthase subunit alpha OS=Bacillus subtilis (strain 168) OX=224308 GN=atpA PE=1 SV=3"]
    # set gap penalty
    gap_penalty = 8

    # find and report optimal alignments for all combinations of sequences
    report_protein_alignment(atpa_hs, atpa_ec, gap_penalty, "atpa_hs", "atpa_ec")
    report_protein_alignment(atpa_mm, atpa_hs, gap_penalty, "atpa_mm", "atpa_hs")
    report_protein_alignment(atpa_mm, atpa_ec, gap_penalty, "atpa_mm", "atpa_ec")
    report_protein_alignment(atpa_bs, atpa_hs, gap_penalty, "atpa_bs", "atpa_hs")
    report_protein_alignment(atpa_bs, atpa_ec, gap_penalty, "atpa_bs", "atpa_ec")
    report_protein_alignment(atpa_mm, atpa_bs, gap_penalty, "atpa_mm", "atpa_bs")

def report_protein_alignment(seq1, seq2, gap_penalty, name1, name2):
    seq_type = validate_sequences(seq1, seq2)
    if seq_type == 2:
        # Both the sequences are protein sequences so read in the BLOSUM62
        # substitution matrix
        subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
    else:
        sys.exit("Input sequences are of different types: not both DNA or both protein")

    # Obtain a dictionary of scores for aligning a pair of characters
    subst_dict = create_subst_matrix_dict(subst_matrix)
    alignment = solve_global_aligner_plus(seq1, seq2, subst_dict, gap_penalty)
    print(f"The optimal score for the alignment of {name1} and {name2} is {alignment[0]}")
    if alignment[1][0] == alignment[2][0] and alignment[1][1] == alignment[2][1]:
        print(f"The optimal alignment is unique and it is")
        print_alignment(alignment[1][0], alignment[1][1], name1=name1, name2=name2)
    else:
        print("The top most alignment is ")
        print_alignment(alignment[1][0], alignment[1][1], name1=name1, name2=name2)
        print(f"The bottom most alignment is ")
        print_alignment(alignment[2][0], alignment[2][1], name1=name1, name2=name2)

def solve_global_aligner_plus(seq1, seq2, subst_dict, gap_penalty):
    """The overall procedure for collecting the inputs, running the aligner,
    filling in the DP table, and returning the final value and alignments.

    Args:
        seq1 (str): first sequence to be aligned
        seq2 (str): second sequence to be aligned
        subst_dict (dictionary string -> int): dictionary representation of the
            substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character); this
            value should be positive because we will subtract it

    Returns a tuple of:
        (the optimal alignment score as an int,
         the top-most alignment achieving this score as a tuple of strings,
         the bottom-most alignment achieving this score as a tuple of strings)

        Example output:

            (6, ("AT-AGG", "ATCCGG"), ("ATA-GG", "ATCCGG"))

    Note: If you do the extra challenge to report all optimal alignments,
    you can lengthen the size of the return tuple, but ensure that its second
    element (i.e., the first alignment) remains the top-most alignment, while
    the last element is the bottom-most alignment. e.g.

        (optimal score, (top-most alignment sequences), ...,
         (bottom-most alignment sequences))
    """
    # Initialize the DP table's data structure
    # as a list of lists of ints, later updated to tuples of (int,(pointers))
    dp_table = [[(0, [])] * (len(seq2)+1) for _ in range(len(seq1)+1)]

    # the dp table has len(seq1) + 1 rows and len(seq2) + 1 columns
    I = len(dp_table)  # so I is 1 more than m
    J = len(dp_table[0])  # so J is 1 more than n

    # Initialize the dp table with solutions to base cases using linear gap
    # penalty

    for i in range(1, I):
        # base case for empty seq1 vs each position in seq2, add gap penalty for each additional gap
        value = dp_table[i - 1][0][0] - gap_penalty
        pointer = (i - 1, 0)
        dp_table[i][0] = (value, [2])
    for j in range(1, J):
        # base case for empty seq2 vs each position in seq1, add gap penalty for each additional gap
        value = dp_table[0][j - 1][0] - gap_penalty
        pointer = (0, j - 1)
        dp_table[0][j] = (value, [3])

    # Compute the scores for the rest of the matrix,
    # i.e. all the elements in dp_table[i][j] for i > 0 and j > 0.

    # need cells above, to the left of, and diagonally up and to the left to be filled to solve for a cell
    # can iterate row by row down the table to fill in
    for i in range(1, I):
        for j in range(1, J):
            # type 1 when seq 1 and seq 2 both have nucleotides in this position, previous is diagonal
            # account for difference in sequence index and table indices
            match = seq1[i - 1] + seq2[j - 1]
            t1 = subst_dict[match] + dp_table[i - 1][j - 1][0]
            # type 2 when seq 1 has a nucleotide and seq 2 has a gap, previous is above
            t2 = - gap_penalty + dp_table[i-1][j][0]
            # type 3 when seq 2 has a nucleotide and seq 1 has a gap, previous is to the left
            t3 = - gap_penalty + dp_table[i][j-1][0]
            # maximize score for this position by finding max of t1,t2,t3
            max_score = max(t1, t2, t3)
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
    max_score = (dp_table[I - 1][J - 1])[0]

    # trace back top-most alignment
    row = I-1
    col = J-1
    al1_top = ""
    al2_top = ""
    # stop when you reach the top left corner of the table (dp_table[0][0] is the empty string)
    while row > 0 or col > 0:
        type = dp_table[row][col][1][0]
        # check the value in the order of top-most to bottom-most step (2>1>3)
        # depending on the col type, add the correct characters to the alignments and adjust the row and column values
        if type == 2:
            al1_top = seq1[row-1] + al1_top
            al2_top = "-" + al2_top
            row -= 1
        elif type == 1:
            al1_top = seq1[row-1] + al1_top
            al2_top = seq2[col-1] + al2_top
            row -= 1
            col -= 1
        elif type == 3:
            al1_top = "-" + al1_top
            al2_top = seq2[col-1] + al2_top
            col -= 1
    # trace back bottom-most alignment
    row = I - 1
    col = J - 1
    al1_bot = ""
    al2_bot = ""
    while row > 0 or col > 0:
        # since pointers are added from top-most to bottom-most, choose the pointer at the end of the pointer list
        type = dp_table[row][col][1][-1]
        # check the value in the order of bottom-most to top-most step (3>1>2)
        # depending on the col type, add the correct characters to the alignments and adjust the row and column values
        if type == 3:
            al1_bot = "-" + al1_bot
            al2_bot = seq2[col-1] + al2_bot
            col -= 1
        elif type == 1:
            al1_bot = seq1[row-1] + al1_bot
            al2_bot = seq2[col-1] + al2_bot
            row -= 1
            col -= 1
        elif type == 2:
            al1_bot = seq1[row-1] + al1_bot
            al2_bot = "-" + al2_bot
            row -= 1
    # return score of optimal alignment, top-most alignment, and bottom-most alignment
    return (max_score, (al1_top,al2_top), (al1_bot,al2_bot))

def display_dp_table_plus(seq1, seq2, dp_table):
    """A function that displays the dp table once it's been computed."""

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
    run_global_aligner_plus()
