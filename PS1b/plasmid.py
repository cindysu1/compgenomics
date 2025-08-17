from compsci260lib import get_fasta_dict


def run_plasmid():
    """Function to run the simple_assembler function to assemble the plasmid from a .fasta of reads.
    """
    # Load the plasmid reads from fasta, and ensure they are in proper order to be assembled
    read_path = "plasmid.fasta"
    read_dict = get_fasta_dict(read_path)
    # Your code goes here
    #
    reads = []
    reads.append(read_dict["start"])
    for read in read_dict:
        if read != "start":
            reads.append(read_dict[read])
    # Assemble the reads into a single-stranded linearized version of the plasmid:
    plasmid_dna = simple_assembler(reads)

    # Report the length of the assembled plasmid
    print("The assembled plasmid sequence is " + plasmid_dna)
    print("The assembled plasmid is " + str(len(plasmid_dna)) + " nucleotides long. The first 15 nucleotides using "
          "the start read are " + plasmid_dna[0:15] + " and the last 15 are " + plasmid_dna[-15:] + ".")


def simple_assembler(reads):
    """Given a list of reads, as described in the problem, return an assembled
    DNA sequence, as a string. For consistency, use the first entry in the
    fragment reads list as the starting position of the returned sequence.

    For example, if we were to take in a list of three reads, 31 nucleotides
    long each. The last 15 nucleotides of each read would overlap with one
    other read, and the assembled sequence would be 48 nucleotides long with
    the sequence starting with the beginning of the first read.

    Args:
        reads (list): list of sequence strings as reads

    Returns:
         str: an assembled genomic sequence as a string starting with the first
              read in `reads`
    """

    # make a dict with the key being a sequence of 15 nucleotides and the value being a list of lists with the read #
    # and if the sequence was from the start or emd of the read
    # define read number arbitrarily as the index of the read in the input list

    sequences = {}

    for index in range(len(reads)):
        start = reads[index][0:15]
        end = reads[index][-15:]
        if start not in sequences:
            sequences[start] = []
        sequences[start].append([index, "start"])
        if end not in sequences:
            sequences[end] = []
        sequences[end].append([index, "end"])
    # two reads can be assembled together if the start of one is the end of another (will be under the same key value)
    # starting with read #1, assemble the source genome

    cur_seq = reads[0][-15:]
    genome = reads[0]
    for i in range(len(reads)):
        ind = 0
        # match the end of the current sequence to the start of the next using the dict
        matches = sequences[cur_seq]
        for match in matches:
            if match[1] == "start":
                ind = match[0]
                break
        frag = reads[ind]
        # add the next read excluding the overlapping portion
        if (cur_seq == reads[0][0:15]):
            # remove last 15 nucleotides because it overlaps with the start read
            genome = genome[0:-15]
            break
        else:
            genome += frag[15:]
            cur_seq = frag[-15:]

    return genome


if __name__ == "__main__":
    run_plasmid()
