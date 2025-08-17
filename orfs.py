import re

from compsci260lib import get_fasta_dict


def run_orfs():
    """Report the number of ORFs if the minimum ORF length is 20 amino acids,
    40 amino acids, or 60 amino acids.  Also report the average length (in
    amino acids) of the identified ORFs for the three cases.
    """
    # read in the RNA sequence of sars_cov2
    sars_path = "sars_cov2_wu.fasta"
    fasta_dict = get_fasta_dict(sars_path)
    sars_rna = fasta_dict["MN908947.3"]
    print(sars_rna[29557:29674])

    # find and report the orfs for each minimum number of amino acids
    min_20 = summarize_orfs(find_orfs(sars_rna, 20))
    min_40 = summarize_orfs(find_orfs(sars_rna, 40))
    min_60 = summarize_orfs(find_orfs(sars_rna, 60))

    # report number and average length of ORFs for different min lengths
    print("When the minimum ORF length is 20 amino acids, there are " + str(min_20[0]) + " ORFs found in the "
          "SARS-CoV-2 genome, and the average ORF length is " + str(min_20[1]) + " amino acids.")
    print("When the minimum ORF length is 40 amino acids, there are " + str(min_40[0]) + " ORFs found in the "
            "SARS-CoV-2 genome, and the average ORF length is " + str(min_40[1]) + " amino acids.")
    print("When the minimum ORF length is 60 amino acids, there are " + str(min_60[0]) + " ORFs found in the "
            "SARS-CoV-2 genome, and the average ORF length is " + str(min_60[1]) + " amino acids.")

    print_orfs(find_orfs(sars_rna, 60))
    return  # placeholder code, just to ensure a valid function


def summarize_orfs(orfs):
    """Summarize ORFs identified from the find_orfs procedure as a count of the
    number of found orfs and the average length of the found ORFs (in amino
    acids)

    Args:
        orfs (list): a list of dictionaries of found ORFs

    Returns:
        tuple: (The number of ORFs found (int), Average ORF length (float))
    """

    # each item in the dict represents one orf, so total number is the length of the dict
    num_orfs = len(orfs)
    total_length = 0
    # calculate average orf length in amino acids
    for orf in orfs:
        total_length += orf['aalength']
    # round average length to nearest integer
    avg_length = round ((total_length / num_orfs), 2)

    return (num_orfs, avg_length)

def print_orfs(orfs):
    """Prints out information about ORFs identified from the find_orfs procedure as the location
    of the orfs and the length in nucleotides

    Args:
        orfs (list): a list of dictionaries of found ORFs

    """

    for orf in orfs:
        print("frame: " + str(orf['frame']) + ", start: " + str(orf['start']) + ", stop: " + str(orf['stop']) +
              ", length: " + str(orf['stop'] - orf['start'] + 1))
    return
def find_orfs(seq, min_length_aa=0):
    """This is a function for finding sufficiently long ORFs in all reading
    frames in a sequence of DNA or RNA.  By default, the sequence is assumed
    to be single-stranded.

    The function takes as input parameters: a string representing a genomic
    sequence, the minimum length (in amino acids) for an ORF before it will be
    considered valid and returned (this parameter defaults to 0).

    Args:
        seq (str): a genomic sequence
        min_length_aa (int): minimum length of found ORFs in amino acids

    Returns:
        list: of dictionaries with information on each ORF found.

    Where each ORF found is represented by a dictionary with the following keys:
        frame (int): the reading frame in which ORF was found (0, 1, or 2)
        start (int): the nucleotide position of the start of the ORF
        stop (int): the nucleotide position of the end of the ORF
        stopcodon (str): the nucleotide triplet of the stop codon
        nlength (int): the length (in nucleotides) of the ORF
        strand (str): the strand of the found ORF ("W" or "C")

    A valid return list may look something like this:
    [
        {
            "frame": 2,
            "start": 3,
            "stop": 98,
            "stopcodon": "UAA",
            "nlength": 96,
            "aalength": 31,
            "strand": "W"
        },
        {
            ...
        }
    ]
    """
    orfs_0 = find_orfs_in_single_frame(seq, 0, min_length_aa)
    orfs_1 = find_orfs_in_single_frame(seq, 1, min_length_aa)
    orfs_2 = find_orfs_in_single_frame(seq, 2, min_length_aa)
    orfs = orfs_0 + orfs_1 + orfs_2
    return orfs


def find_orfs_in_single_frame(seq, frame=0, min_length_aa=0):
    """This is a function for finding sufficiently long ORFs in one specified
    reading frame in a linear sequence of single-stranded DNA or RNA.

    It returns a list of dictionaries, one for each ORF of sufficient length 
    that is found in the desired reading frame, with information as follows:

    {
    "frame":      reading frame: 0, 1, or 2
    "start":      start position (first char of start codon), 1-indexed
    "stop":       stop position (last char before stop codon), 1-indexed
    "nlength":    nucleotide length
    "aalength":   amino acid length when ORF is translated
    "stopcodon":  stop codon used to terminate this ORF
    "strand":     label for the strand on which the ORF was found: W or C
    }
    """
 
    # use regular expression to define all stop codons and the start codon in rna or dna
    stop = re.compile(r"[ut]ga|[ut]aa|[ut]ag")
    start = r'a[ut]g'

    # find all start and stop codons and store their start location
    start_matches = re.finditer(start, seq)
    stop_matches = re.finditer(stop, seq)

    # create list to store start indices of all start codons in frame
    starts = []
    # create dict to store sequence and end indices of all stop codons in frame
    stops = {}
    for match in start_matches:
        # check if the match is in the correct reading frame
        if match.start() == 0 or (match.start() - frame)%3 == 0:
            starts.append(match.start())
    for match in stop_matches:
        # check if the match is in the correct reading frame
        if match.start() == 0 or (match.start() - frame)%3 == 0:
            stops[match.end()-1] = match.group()
    # matched codons will be in ascending order
    # find ORFs and store relevant information in dict
    orf_list = []
    index = 0
    while (index < len(starts)):
        start_val = starts[index]
        # find first stop codon after the given start codon
        stop_val = next((val for val, val in enumerate(stops) if val > start_val), len(seq)+1)
        # check if you reached the end of the sequence
        if stop_val > len(seq):
            break
        stopcodon = stops[stop_val].upper()
        nlength = (stop_val-start_val+1)
        aalength = int(nlength/3-1)
        if aalength >= min_length_aa:
            # add one to start and end to make them 1-indexed
            orf_list.append({'frame': frame, 'start': start_val+1, 'stop': stop_val+1, 'stopcodon': stopcodon,
                             'nlength': nlength, 'aalength': aalength, 'strand':'W'})
        # increment index to that of the first start codon after the current ORF
        index = next((ind for ind, val in enumerate(starts) if val > stop_val), len(starts))
    return orf_list


if __name__ == "__main__":
    """Run run_orfs(). Do not modify this code"""
    run_orfs()
