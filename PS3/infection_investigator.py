from bwt import *
from fm_index import *
from compsci260lib import *


def align_patient_reads():
    """Align patient reads to each bacterial genome"""

    # Patients
    patients = ["patient1",
                "patient2",
                "patient3"]

    # Bacterial species
    panel = ["Bacteroides_ovatus",
             "Bacteroides_thetaiotaomicron",
             "Bifidobacterium_longum",
             "Eubacterium_rectale",
             "Lactobacillus_acidophilus",
             "Peptoniphilus_timonensis",
             "Prevotella_copri",
             "Roseburia_intestinalis",
             "Ruminococcus_bromii",
             "Vibrio_cholerae"]

    # Store the genome sequence and bwt structures for each bacterial species
    bact_sequences = {}
    bact_bwt_structures = {}
    for bacteria in panel:
        # For each of the bacteria in our panel, create a dictionary entry
        # where keys are bacterial names and values are their genome sequences.
        bact_sequences[bacteria] = list(get_fasta_dict(
            f"reference_genomes/{bacteria}.fasta").values())[0]

        # For each of the bacterial genome sequences, create a dictionary entry
        # where keys are bacterial names and values are their BWT data
        # structures.
        bact_bwt_structures[bacteria] = make_all(bact_sequences[bacteria])
    # Store a mapping of patient names to reads
    patient_reads = {}
    for patient in patients:
        reads = list(get_fasta_dict(f"patients/{patient}.fasta").values())
        patient_reads[patient] = reads

    # Store the reads mapped per bacterial species per patient
    mapped_patient_reads = {}
    # Consider all patients
    for patient in patients:
        count = 0
        # Find uniquely mapped reads for each bacteria for the patient
        # and store the read start positions
        mapped_reads = find_aligned_reads_for_patient(
            patient_reads[patient], bact_bwt_structures)
        # update dict containing all patient mappings
        mapped_patient_reads[patient] = mapped_reads

    with open('mapped_reads.txt', 'w') as f:
        print(mapped_patient_reads, file=f)
    f.close()

    # Report the microbe prevalences for each of your patients
    for patient in patients:
        count = 0
        for bact in panel:
            count += len(mapped_patient_reads[patient][bact])
        for bact in panel:
            bact_prev = round(len(mapped_patient_reads[patient][bact])/count,4)
            print(f"The prevalence of {bact} in {patient} is {bact_prev}.")

    # Use `read_mapper` and `longest_zeroes` to identify unmapped regions
    # for the relevant patients and species (questions 2f-h)
    bacteria = "Vibrio_cholerae"
    gen = bact_sequences[bacteria]
    one_zeros = longest_zeros(read_mapper(mapped_patient_reads["patient1"][bacteria], gen))
    two_zeros = longest_zeros(read_mapper(mapped_patient_reads["patient2"][bacteria], gen))

    # print the coordinates of the longest stretch of zeros if it exists for the two patients of interest
    if one_zeros:
        print(f"The start and stop positions of the longest stretch of zeros for patient 1 are {one_zeros[0] + 1} and "
              f"{one_zeros[1] + 1} (1-indexed) respectively.")
    else:
        print("There are no stretches of zeros for patient 1.")

    if two_zeros:
        print(f"The start and stop positions of the longest stretch of zeros for patient 2 is {two_zeros}.")
    else:
        print("There are no stretches of zeros for patient 2.")

    # print the part of the genome identified as the longest stretch of zeros
    print(gen[one_zeros[0]:one_zeros[1]])

def find_aligned_reads_for_patient(reads, bact_bwt_structures):
    """
    Given a list of reads for a patient, identify the reads that uniquely map
    to each bacteria's genome using its relevant BWT data structure. Reads that
    are mapped to a bacteria's genome should be stored as starting positions in
    a list.

    Args:
        reads (list of str):
            mapping a patient's read names (str) to read sequences (str).

        bact_bwt_structures: dictionary mapping bacterial names (str) to 
            structures required for efficient exact string matching). Refer
            to the return tuple from `make_all` in fm_index.py.

    Returns:
        a dictionary mapping bacterial names (str) to the start positions of
        reads mapped to that bacteria's genome. Note that the end positions are
        not needed as the reads are all 50 bases long. Start positions should
        be stored using 0-indexing.

        Example return structure:
        {
            "Bacteroides_ovatus": [8, 124, 179, ...],
            ...
        }
    """
    # store the start positions of reads mapped to each bacterium's genome
    counts = {}
    panel = list(bact_bwt_structures.keys())
    # dict mapping bacterial names to reads that map multiple times to the same genome
    # key is bacterial name, value is a list of lists (start positions that a single read maps to)
    for read in reads:
        read = reverse_complement(read)
        # use to check how many genomes each read matches to, resets for each read
        positions = {}
        for bac in panel:
            matches = find(read, bact_bwt_structures[bac])
            # only append to positions if there is a match in the genome
            if len(matches) > 0:
                positions[bac] = matches
        # check if the read uniquely matches to one genome
        if len(positions.keys()) == 1:
            # add matches to overall counts
            for bact in positions:
                counts[bact] = counts.get(bact, []) + positions[bact]
    # sort start positions to make it easier to comprehend
    for bact in counts:
        counts[bact] = sorted(counts[bact])
    return counts


def read_mapper(starting_positions, genome):
    """
    Using the starting positions of reads that were aligned to a bacterial
    genome, construct a count vector (as a list) that counts how many reads
    were aligned to a position in the genome. The vector's size will be the 
    length of the genome. You may assume that each read is 50 base pairs long.

    Args:
        starting_positions (list of ints): 
            starting positions of reads that were aligned to a genome.

        genome (str): the genomic nucleotide sequence to which the reads 
                      were aligned.

    Returns:
        (list of ints): vector of aligned read counts to the genome.
        i.e. [c_1, c_2, ..., c_i, ..., c_n], where n=length of the genome
        and c_i = the count of aligned reads for the patient at genome
        position i.
    """
    # instantiate list with 0s representing each nucleotide in the genome
    count_vector = [0] * len(genome)
    for pos in starting_positions:
        for ind in range(pos, pos+50):
            # readme says we can assume each read only appears once in a given genome
            # increment count for each index the read aligns to
            count_vector[ind] += 1

    return count_vector

# It may be helpful to read the documentation for the methods
# given below, but you will NOT have to make any changes to
# them in order to complete the problem set.


def longest_zeros(count_vector):
    """Given a count vector, return the start and stop position (inclusive) of
    the longest string of internal zeros in the vector. If there is no
    internal string of zeros, return None.

    Examples to understand behavior:
    input -> output
    contain valid internal string of zeros:
    [1, 1, 1, 0, 0, 1, 1] -> (3, 4)
    [1, 1, 1, 0, 1, 1, 1]  -> (3, 3)
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0] -> (5, 6)

    do not contain internal string of zeros:
    [0, 0, 0, 1, 1, 1, 1] -> None
    [1, 1, 1, 1, 0, 0, 0] -> None
    [0, 0, 0, 0, 0, 0, 0] -> None
    [1, 1, 1, 1, 1, 1, 1] -> None

    Args:
        count_vector (list of ints): vector of aligned read counts to the
        genome.  see: the return value for `read_mapper()`

    Returns:
        (tuple of (int, int)): the start and stop position (inclusive) of the longest
        internal string of zeros in the count_vector. If there are no internal
        runs-of-zero the return will be None.
    """

    zero_nums = []
    genome_len = len(count_vector)
    for i in range(0, genome_len):
        if count_vector[i] == 0:
            zero_nums.append(i)

    if len(zero_nums) == 0:
        return None

    counter = 1
    longest_run = {1: [zero_nums[0]]}

    for z in zero_nums[1:]:
        if (z - longest_run[counter][-1]) == 1:
            longest_run[counter].append(z)
        else:
            counter += 1
            longest_run[counter] = []
            longest_run[counter].append(z)

    for run in list(longest_run.keys()):
        if 0 in longest_run[run] or genome_len-1 in longest_run[run]:
            del longest_run[run]

    longest = []
    for run in list(longest_run.values()):
        if len(run) > len(longest):
            longest = run

    # There was no run of zeroes found, return None
    if len(longest) == 0:
        return None

    start = longest[0]
    stop = longest[-1]

    # Return the start and end positions of the longest zeroes (0-indexed)
    return start, stop


if __name__ == "__main__":
    align_patient_reads()
