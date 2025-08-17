from compsci260lib import *
from aligner_helpers import *

def run_ag_aligner_plus():
    """Align atpa_Hs.fasta and atpaEc.fasta and report the optimal
    alignment score, the top-most alignment, and the bottom-most
    alignment.
    """
    # test case to compare to manually calculated result
    # seq1 = "CGATCGAT"
    # seq2 = "GCCATT"
    # match = 2
    # mismatch = -1
    # gap_penalty = 2
    # affine_penalty = 4
    # subst_matrix = create_subst_matrix_dna(match, mismatch)
    # subst_dict = create_subst_matrix_dict(subst_matrix)
    # alignment = solve_ag_aligner_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty)
    # print(f"The optimal score for the alignment is {alignment[0]}")
    # print("The top most alignment is ")
    # print_alignment(alignment[1][0], alignment[1][1])
    # print(f"The bottom most alignment is ")
    # print_alignment(alignment[2][0], alignment[2][1])

    # load dicts in from fasta files and save as sequences
    hs_path = "atpa_Hs.fasta"
    fasta_dict = get_fasta_dict(hs_path)
    atpa_hs = fasta_dict[
        ("sp|P25705|ATPA_HUMAN ATP synthase subunit alpha, mitochondrial OS=Homo sapiens OX=9606 GN=ATP5F1A PE=1 SV=1")]
    ec_path = "atpa_Ec.fasta"
    fasta_dict = get_fasta_dict(ec_path)
    atpa_ec = fasta_dict[
        "sp|P0ABB0|ATPA_ECOLI ATP synthase subunit alpha OS=Escherichia coli (strain K12) OX=83333 GN=atpA PE=1 SV=1"]
    # set gap and affine penalty values
    gap_penalty = 2
    affine_penalty = 12
    # use helper method to report optimal score, top-most alignment, and bottom-most alignment
    report_affine_protein_alignment(atpa_hs, atpa_ec, gap_penalty, affine_penalty, "atpa_hs", "atpa_ec")

def report_affine_protein_alignment(seq1, seq2, gap_penalty, affine_penalty, name1, name2):
    """Prints the alignment between two sequences as line-broken chunks, considers if there are multiple alignments or 1

        Args:
            seq1 (str): the subsequence (from the first sequence) of the
                alignment
            seq2 (str): the subsequence (from the second sequence) of the
                alignment
            gap_penalty (int): gap penalty (penalty per gap character);
                this value should be positive because we will subtract it
            affine_penalty (int): affine penalty; as a positive integer
            name1 (str): the name of the first sequence. Defaults to
                "Seq 1"
            name2 (str): the name of the second sequence. Defaults to
                "Seq 2"
        """
    seq_type = validate_sequences(seq1, seq2)
    if seq_type == 2:
        # Both the sequences are protein sequences so read in the BLOSUM62
        # substitution matrix
        subst_matrix = create_subst_matrix_aa("BLOSUM62.txt")
    else:
        sys.exit("Input sequences are not protein")

    # Obtain a dictionary of scores for aligning a pair of characters
    subst_dict = create_subst_matrix_dict(subst_matrix)
    alignment = solve_ag_aligner_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty)
    # report optimal score
    print(f"The optimal score for the alignment of {name1} and {name2} is {alignment[0]}")
    # report unique or top-most and bottom-most alignments
    if alignment[1][0] == alignment[2][0] and alignment[1][1] == alignment[2][1]:
        print(f"The optimal alignment is unique and it is")
        print_alignment(alignment[1][0], alignment[1][1], name1=name1, name2=name2)
    else:
        print("The top most alignment is ")
        print_alignment(alignment[1][0], alignment[1][1], name1=name1, name2=name2)
        print(f"The bottom most alignment is ")
        print_alignment(alignment[2][0], alignment[2][1], name1=name1, name2=name2)

def solve_ag_aligner_plus(seq1, seq2, subst_dict, gap_penalty, affine_penalty):
    """The procedure for collecting the inputs, running the aligner,
    and returning the score and optimal alignments.

    Args:
        seq1 (str): first sequence to match
        seq2 (str): second sequence to match
        subst_dict (dictionary string -> int): dictionary
            representation of the substitution matrix
        gap_penalty (int): gap penalty (penalty per gap character);
            this value should be positive because we will subtract it
        affine_penalty (int): affine penalty; as a positive integer

    Returns a tuple of:
        (the optimal alignment score as an int,
         the top-most alignment achieving this score as a tuple of
         strings, the bottom-most alignment achieving this score as a
         tuple of strings)

        Example output:
            (6, ("AT-AGG", "ATCCGG"), ("ATA-GG", "ATCCGG"))
    """
    # the dp table has len(seq1) + 1 rows and len(seq2) + 1 columns
    I = len(seq1) + 1  # so I is 1 more than m
    J = len(seq2) + 1  # so J is 1 more than n

    # Initialize the DP tables' data structure
    # as a list of lists of tuples of (int,(pointers))
    # Initialize dp_1 (D), the dp table storing values for when the final column is type 1
    dp_1 = [[(float('-inf'), [])] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    dp_1[0][0] = (0, [])
    # Initialize dp_2 (E), the dp table storing values for when the final column is type 2
    dp_2 = [[(float('-inf'), [])] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    dp_2[1][0] = (-(affine_penalty + gap_penalty), [1])
    for ind in range(2,I):
        # value is -h - g*i, points to table 2 because other tables have -inf
        dp_2[ind][0] = (-(affine_penalty + gap_penalty*ind), [2])
    # Initialize dp_2 (F), the dp table storing values for when the final column is type 3
    dp_3 = [[(float('-inf'), [])] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    dp_3[0][1] = (-(affine_penalty + gap_penalty), [1])
    for ind in range(2, J):
        # value is -h - g*j, points to table 3 because other tables have -inf
        dp_3[0][ind] = (-(affine_penalty + gap_penalty * ind), [3])

    # Compute the scores for the rest of the matrix,
    # i.e. all the elements in dp_table[i][j] for i > 0 and j > 0.

    # need cells above, to the left of, and diagonally up and to the left to be filled to solve for a cell
    # can iterate row by row down the table to fill in
    for i in range(1, I):
        for j in range(1, J):
            # fill in each table cell by cell to make sure all the cells being referenced in each table have a value
            for dp_table in [dp_1, dp_2, dp_3]:
                # choose scores/penalties, indices of lookup, and pointers based on which table it is
                pointers = []
                if dp_table == dp_1:
                    # dp_1 when last column is type 1, so previous cell is at i-1,j-1
                    # find max value from the 3 tables
                    prev = max(dp_1[i-1][j-1][0], dp_2[i-1][j-1][0], dp_3[i-1][j-1][0])
                    # lookup match in substitution matrix
                    match = seq1[i - 1] + seq2[j - 1]
                    max_score = subst_dict[match] + prev
                    # append pointers based on which table(s) has the max value
                    if prev == dp_2[i-1][j-1][0]:
                        pointers.append(2)
                    if prev == dp_1[i-1][j-1][0]:
                        pointers.append(1)
                    if prev == dp_3[i-1][j-1][0]:
                        pointers.append(3)
                    # add value and pointers to dp_table[i][j]
                    dp_table[i][j] = (max_score, pointers)
                elif dp_table == dp_2:
                    # store values at i-1,j from each table for concision
                    t1 = dp_1[i - 1][j][0]
                    t2 = dp_2[i - 1][j][0]
                    t3 = dp_3[i - 1][j][0]
                    # dp_2 when last column is type 2, if previous cell is from dp_1 or dp_3, pay affine penalty
                    prev = max(t1 - affine_penalty, t2, t3 - affine_penalty)
                    max_score = - gap_penalty + prev
                    if prev == t2:
                        pointers.append(2)
                    if prev == t1 - affine_penalty:
                        pointers.append(1)
                    if prev == t3 - affine_penalty:
                        pointers.append(3)
                    dp_table[i][j] = (max_score, pointers)
                elif dp_table == dp_3:
                    t1 = dp_1[i][j-1][0]
                    t2 = dp_2[i][j-1][0]
                    t3 = dp_3[i][j-1][0]
                    prev = max(t1 - affine_penalty, t2 - affine_penalty, t3)
                    max_score = - gap_penalty + prev
                    if prev == t2 - affine_penalty:
                        pointers.append(2)
                    if prev == t1 - affine_penalty:
                        pointers.append(1)
                    if prev == t3:
                        pointers.append(3)
                    dp_table[i][j] = (max_score, pointers)
                # we know if the pointer should point up, to the left, or diagonal based on the table number
                # store which table the pointer should point to in the pointers array (1:dp_1, 2:dp_2, 3:dp_3)
    # display_dp_table_plus(seq1, seq2, dp_1)
    # display_dp_table_plus(seq1, seq2, dp_2)
    # display_dp_table_plus(seq1, seq2, dp_3)
    # max affine global score is the max value in the bottom right corner from the 3 tables
    opt_score = max(dp_1[I - 1][J - 1][0], dp_2[I - 1][J - 1][0], dp_3[I - 1][J - 1][0])
    table = 0
    # trace back top-most alignment
    row = I - 1
    col = J - 1
    al1_top = ""
    al2_top = ""
    # figure out which table the top-most optimal alignment comes from
    # dp_2 would have the top-most alignment, followed by dp_1 then dp_3
    if opt_score == dp_2[I - 1][J - 1][0]:
        table = 2
    elif opt_score == dp_1[I - 1][J - 1][0]:
        table = 1
    else:
        table = 3
    while row > 0 or col > 0:
        # print(f'row: {row}, col: {col}')
        # add characters to alignment and adjust row and col depending on which table the value is (shows col type)
        if table == 2:
            al1_top = seq1[row - 1] + al1_top
            al2_top = "-" + al2_top
            # update table type to the table the preceding character is in
            table = dp_2[row][col][1][0]
            row -= 1
        elif table == 1:
            al1_top = seq1[row - 1] + al1_top
            al2_top = seq2[col - 1] + al2_top
            # update table type to the table the preceding character is in
            table = dp_1[row][col][1][0]
            row -= 1
            col -= 1
        elif table == 3:
            al1_top = "-" + al1_top
            al2_top = seq2[col - 1] + al2_top
            # update table type to the table the preceding character is in
            table = dp_3[row][col][1][0]
            col -= 1

    # trace back bottom-most alignment
    row = I - 1
    col = J - 1
    al1_bot = ""
    al2_bot = ""
    # figure out which table the top-most optimal alignment comes from
    # dp_3 would have the bottom-most alignment, followed by dp_1 then dp_1
    if opt_score == dp_3[I - 1][J - 1][0]:
        table = 3
    elif opt_score == dp_1[I - 1][J - 1][0]:
        table = 1
    else:
        table = 2
    while row > 0 or col > 0:
        # add characters to alignment and adjust row and col depending on what table the value is from
        if table == 3:
            al1_bot = "-" + al1_bot
            al2_bot = seq2[col - 1] + al2_bot
            # update table type to the table the preceding character is in
            table = dp_3[row][col][1][-1]
            col -= 1
        elif table == 1:
            al1_bot = seq1[row - 1] + al1_bot
            al2_bot = seq2[col - 1] + al2_bot
            # update table type to the table the preceding character is in
            table = dp_1[row][col][1][-1]
            row -= 1
            col -= 1
        elif table == 2:
            al1_bot = seq1[row - 1] + al1_bot
            al2_bot = "-" + al2_bot
            # update table type to the table the preceding character is in
            table = dp_2[row][col][1][-1]
            row -= 1
    # return optimal score, top-most, and bottom-most alignments
    return (opt_score, (al1_top, al2_top), (al1_bot, al2_bot))

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
    run_ag_aligner_plus()
