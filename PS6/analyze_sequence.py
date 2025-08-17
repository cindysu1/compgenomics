from generate_HMM_sequence import generate_HMM_sequence


def run_analyze_sequence(gen_seq_file):
    """Load the nucleotide sequence HMM file and generate a 100000 length sequence,
    then do some analysis of the results, including the average length in each state.

    Args:
        gen_seq_file: The name of the output file for the generated nucleotide sequence.
    """
    seq_length = 100000
    state_sequence, observed_sequence = generate_HMM_sequence(
        "HMM_parameters.txt", seq_length)

    # Write your generated sequence to file. Report the states that prevailed whenever
    # TCGA was observed, and their frequencies when observing TCGA. Finally, report
    # the average length spent in each state across the entire sequence.
    output_file_name = "nucleotide_sequence.txt"
    with open(output_file_name, "w") as f:
        f.write(''.join(state_sequence))
        f.write(''.join(observed_sequence))
        f.close()

    # compute the state frequencies given subsequence TCGA
    state_freq = compute_state_frequencies(state_sequence, observed_sequence, ["T","C","G","A"])
    sorted_states = sorted(state_freq.items(), key=lambda item: item[1], reverse=True)
    # print the frequencies of each state sequence
    print("Given the subsequence TCGA,")
    for state in sorted_states:
        print(f"The state sequence {state[0]} has a count of {state[1]}.")

    # compute and report average lengths
    avg_lengths = compute_average_length(state_sequence)
    avg_w = avg_lengths["W"]
    avg_s = avg_lengths["S"]
    print(f"The average length the system remains in state W is {avg_w:.2f}, and the average length it remains in "
          f"state S is {avg_s:.2f}.")


def compute_average_length(state_sequence):
    """Given a state sequence, return the average length in each state

    Arguments:
        state_sequence: generated sequence of states, represented as list of single-char strings

    Returns:
        a dictionary mapping the state name to the average length in the state.
        Example return:
        {
            "W": 5.5,
            "S": 4.5
        }
    """
    # Check the type of state_sequence
    if type(state_sequence) is not list:
        raise TypeError(f"The argument 'state_sequence' must be a list of strings. "
                        f"(received type {type(state_sequence)})")

    # Compute the average length in each state
    # store total occurrences and number of distinct blocks for each state
    count = {"W": 0, "S": 0}
    nums = {"W": 0, "S": 0}
    # store state as a global variable to compare each subsequent state to
    state = state_sequence[0]
    # increment count of first state in sequence
    count[state] += 1
    # iterate through the rest of the state sequence
    for ind in range(1, len(state_sequence)):
        # if state does not change, the current block continues
        if state_sequence[ind] == state:
            count[state] += 1
        # state changes, complete last block and udpate state
        else:
            nums[state] += 1
            state = state_sequence[ind]
            count[state] += 1

    # add one to account for the last chunk of a given state
    nums[state] += 1

    # calculate average lengths
    avg_w = count["W"]/nums["W"]
    avg_s = count["S"]/nums["S"]
    return {"W": avg_w, "S": avg_s}


def compute_state_frequencies(state_sequence, observed_sequence, subsequence):
    """Given the state and observed sequences, return the state sequences that
    emitted the query subsequence and frequency in which those state sequences
    sequences emitted the subsequence.

    Arguments:
        state_sequence (list of single-char strings): generated state sequence
        observed_sequence (list of single-char strings): generated observed sequence
        subsequence (list of single-char strings): the observed subsequence to count

    Returns:
        a dictionary mapping the state name to the frequency of observing the
        provided sequence. Example return:
        {
            "WWWW": 2,
            "WWWS": 1,
            ...
        }
    """

    # Check the types for each of the input arguments
    if type(state_sequence) is not list:
        raise TypeError(f"The argument 'state_sequence' must be a list of strings. "
                        "(received type {type(state_sequence)})")
    if type(observed_sequence) is not list:
        raise TypeError(f"The argument 'observed_sequence' must be a list of strings. "
                    "(received type {type(observed_sequence)})")
    if type(subsequence) is not list:
        raise TypeError(f"The argument 'subsequence' must be a list of strings. "
                    "(received type {type(subsequence)})")

    # create dict to store frequencies of each state that appears
    freq = {}
    # convert all lists of single chars to strings to use string search methods
    state_sequence = ''.join(state_sequence)
    observed_sequence = ''.join(observed_sequence)
    subsequence = ''.join(subsequence)
    # index marking the first occurrence of the subsequence
    ind = observed_sequence.find(subsequence)
    # start marking the start of the search range
    start = 0
    # continue until there are no more matches
    while ind != -1:
        # find state sequence by using the index of the match in observed sequence
        state = state_sequence[ind:ind + len(subsequence)]
        # increment start to one after current match to find next
        start = ind + 1
        # add state to the dict if necessary, increment count otherwise
        if state not in freq:
            freq[state] = 1
        else:
            freq[state] += 1
        ind = observed_sequence.find(subsequence, start)
    return freq


if __name__ == "__main__":
    """Main method call, do not modify"""
    run_analyze_sequence("nucleotide_sequence.txt")
