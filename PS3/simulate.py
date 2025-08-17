import random

from compsci260lib import *


def run_simulate():
    """
    Simulates the sequencing process then empirically compute and report
    the quantities from parts a-c.
    """

    # fill in values
    iterations = 20
    G = 3500000
    R = 40000
    L = 450

    # Call simulate(G, R, L) `iteration` times. Report the empirical values
    # from parts a-c for each iteration
    emp_cov = 0
    unsequenced = 0
    num_contigs = 0
    avg_length = 0

    for i in range(iterations):
        data = simulate(G,R,L)
        # specify iteration
        print(f"The values for simulation {i+1} are as follows:")
        # store and print empirical coverage
        emp_cov += data[0]
        print(f"Empirical Coverage = {round(data[0],4)}")
        # store and print number of unsequenced nucleotides
        unsequenced += data[1]
        print(f"Number of nucleotides not covered by any read = {data[1]}")
        # store and print number of contigs
        num_contigs += data[2]
        print(f"Number of contigs = {data[2]}")
        # store and print average length of each contig
        avg_length += data[3]
        print(f"Average length of contigs = {round(data[3],4)} nucleotides")
        print()
    # print averages of all variables from all 20 trials
    print(f"The average empirical coverage is {round(emp_cov/iterations,3)}. The average number of nucleotides not covered "
          f"by any read is {unsequenced/iterations}. The average number of contigs is {num_contigs/iterations}. The "
          f"average length of each contig is {round(avg_length/iterations,2)} nucleotides")


def simulate(G, R, L):
    """
    Simulates one iteration of the sequencing process and empirically compute
    the empirical coverage (average number of times a nucleotide in the genome
    was sequenced), the number of nucleotides not covered by any read, the
    number of contigs assuming you can use the oracular assembly algorithm to
    assemble all the reads, and the average length of these contigs.

    Args:
        G (int) - the length of the genome
        R (int) - the number of reads
        L (int) - the length of each read

    Returns
        a tuple of floats:

            (Empirical coverage,
             Number of nucleotides not covered by any read,
             Number of contigs,
             Average length of these contigs)
    """

    # create list of size G to track how many times each position has been sequenced
    genome = [0] * G
    for int in range(R):
        # ignore edge effects since L<<G, could also expand random int range to negate edge effect
        start = random.randint(0, G-L)
        for add in range(start, start+L):
            # indicate each nucleotide in the read covers the correct index in the genome
            genome[add] += 1
    # calculate empirical coverage with total number of mapped nucleotides over genome length
    empirical_coverage = sum(genome) / len(genome)
    # count number of nucleotides in the genome that were not sequenced at all
    unsequenced = genome.count(0)
    # store lengths of all contigs in this array
    contigs = []
    start = 0
    nuc = 1
    while nuc < len(genome):
        # case if it reaches the last nucleotide in the genome, it will add the last contig whether or not last nuc is 0
        if nuc == len(genome)-1:
            contigs.append(nuc-start+1)
            break
        # 0 marks the end of a contig
        if genome[nuc] == 0:
            # add length of current contig
            contigs.append(nuc-start)
            start = nuc
            # if there are consecutive 0s, continue without adding to contig array and increment start index
            while genome[nuc] == 0:
                if nuc == len(genome)-1:
                    break
                nuc += 1
                start += 1
        nuc += 1
    num_contigs = len(contigs)
    # another way to calculate average length
    avg_length1 = (len(genome)-unsequenced)/num_contigs
    # sum up all lengths in contigs array and divide by the number of contigs
    avg_length = sum(contigs)/num_contigs

    return (empirical_coverage, unsequenced, num_contigs, avg_length, avg_length1)


if __name__ == "__main__":
    """Call run_simulate(), do not modify"""
    run_simulate()
