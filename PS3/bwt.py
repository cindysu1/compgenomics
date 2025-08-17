from compsci260lib import *

# Note that the "$" character will be used to designate the end of a given
# string.


def solve_bwt():
    """Load the mystery.txt file and decode its contents using the
    reverse BWT transformation. Report the decoded contents."""

    # Example sequences for forward_bwt() and reverse_bwt();
    # you may change them to different sequences to test your code.

    seq1 = "GATTACA$"
    seq2 = "ACTGA$TA"
    forward_bwt(seq1)
    reverse_bwt(seq2)
    print("The BWT of the sequence GGACTAACGGACTAACGGACTAACGGACTAC$ is " + forward_bwt(
        "GGACTAACGGACTAACGGACTAACGGACTAC$"))

    # Code to open the file mystery.txt in the correct encoding
    # across platforms, and read its contents into a variable.
    with open("mystery.txt", "r", encoding="UTF-8") as f:
        mystery_seq = f.read()

    print("The decoded message in the mystery text reads says the following: ")
    print(reverse_bwt(mystery_seq).replace("_"," "))


def forward_bwt(seq):
    """forward_bwt(seq) takes as input a string containing the EOF character to
    which the BWT must be applied. The method should then return the result of
    the BWT on the input string.

    For example:
        forward_bwt("GATTACA$") --> "ACTGA$TA"

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """

    suffixes = {}
    # store substrings as keys and prefix index as value
    for index in range(len(seq)):
        suffixes[seq[index:]] = index
    # empty string to store BWT, append each letter from the last row of the BWM
    bwt = ""
    # sort the suffixes in the dict alphabetically, $ has a lower ASCII value than letters
    for key in sorted(suffixes):
        # append last character of circular permutation using original sequence
        if suffixes[key] == 0:
            bwt = bwt + seq[-1]
        else:
            bwt = bwt + seq[suffixes[key]-1]
    return bwt


def reverse_bwt(seq):
    """reverse_bwt(seq) takes as input a string containing the EOF character to
    which the reverse of the BWT must be applied. The method should then return
    the result of the reversal on the input string.

    For example:
        reverse_bwt("ACTGA$TA") --> "GATTACA$"

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """

    # store first column (sorted bwt)
    bwm = sorted(seq)
    # outer loop is len(seq) - 1 because the first column is already in bwm
    for ind in range(len(seq)-1):
        # append each character of the bwt to the corresponding row in the bwm
        for i in range(len(bwm)):
            bwm[i] = seq[i] + bwm[i]
        # sort the extended bwm
        bwm = sorted(bwm)
    # first item in the bwm array starts with $ because of the sorting
    bwt = bwm[0][1:] + "$"
    return bwt



if __name__ == "__main__":
    """Run solve_bwt(). Do not modify this code"""
    solve_bwt()
