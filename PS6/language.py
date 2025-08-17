import random
import textwrap

def run_language():
    """Call `generate_mm_text` with the provided parameters."""
    # set file name
    file_name = "tidy_heart_of_darkness.txt"
    # create list storing the orders of the MM we are building
    orders = [1,2,3,4]
    # M is the number of characters being generated
    M = 1000
    # create an artificial text for each order with the correct file name
    for order in orders:
        generated_text = generate_mm_text(file_name, order, M)

        # Save the generated text to a file with the markov order in the name
        output_file_name = f"heart_of_darkness_mm_{order}.txt"
        with open(output_file_name, "w") as f:
            f.write(generated_text)
            f.close()

    # update file name for next source text
    file_name = "tidy_paradise_lost.txt"
    # create artificial texts for each order
    for order in orders:
        generated_text = generate_mm_text(file_name, order, M)

        # Save the generated text to a file with the markov order in the name
        output_file_name = f"paradise_lost_mm_{order}.txt"
        with open(output_file_name, "w") as f:
            f.write(generated_text)
            f.close()
def generate_mm_text(file_name, order, M):
    """Create a Markov model for a given text file and output artificially
    generated text from the model.

    Args:
        file_name (str): path of the text to process
        order (int): order of the Markov model
        M (int): the length of the number of characters in the returned generated
        string

    Returns:
        A string of randomly generated text using a Markov model
    """
    # Read the contents of the file
    f = open(file_name, "r")

    if f is None:
        print("Can't open " + file_name)
    else:
        contents = f.read()
        f.close()
        contents = contents.replace("\n", "")
        contents = contents.replace("\r", "")

    # Collect the counts necessary to estimate transition probabilities
    # This dictionary will store all the data needed to estimate the Markov model:
    txt_dict = collect_counts(contents, order)

    # Generate artificial text from the trained model
    seed = contents[0:order]
    text = seed

    for _ in range(M):
        next_character = generate_next_character(seed, txt_dict)
        text += next_character
        seed = seed[1:] + next_character

    text_list = textwrap.wrap(text, 72)
    text = "\n".join(text_list)

    # Return the generated text
    return text


def display_dict(txt_dict):
    """Print the text dictionary as a table of keys to counts.
    Currently accepts a dictionary specified by the return documentation in the
    `build_dict` function.

    You will need to modify this function to accept the dictionary returned by
    the `collect_counts` function.

    Arguments:
        txt_dict (dict) - Mapping keys (as strings) to counts (as ints). After
        modification for `collect_counts`, the txt_dict will map keys (as strings)
        to dictionaries of counts and followers described in the return method
        of `collect_counts`.
    """

    print("key\tcount\tfollower counts")
    for key in sorted(txt_dict.keys()):
        print("%s\t%d " % (key, txt_dict[key]["count"]), "\t\t", end=" ")
        # sort the followers alphabetically
        followers = sorted(txt_dict[key]["followers"].keys())
        for follower in followers:
            # display each follower and its count
            print("%s:%d" % (follower, txt_dict[key]["followers"][follower]), end=" ")
        # new line
        print()


def build_dict(contents, k):
    """Builds a dictionary of k-character (k-tuple) substring counts. Store the
    dictionary mapping from the k-tuple to an integer count.

    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring

    Returns:
        a text dictionary mapping k-tuple to an integer
        Example return value with k=2:
        { 
            "ac": 1,
            "cg": 2,
            ... 
        }
    """
    # create dict to store counts of each tuple
    counts = {}
    # consider each tuple excluding the last k-tuple, which has nothing following it
    for ind in range(len(contents) - k):
        # store k-tuple in variable
        current = contents[ind:ind + k]
        # add key if k-tuple is not in dict and set count to 1
        if current not in counts:
            counts[current] = 1
        else:
            # increment count
            counts[current] += 1
    return counts


def collect_counts(contents, k):
    """Build a k-tuple dictionary mapping from k-tuple to a dictionary of
    of counts and dictionary of follower counts.
    
    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring

    Returns:
        a dictionary mapping k-tuple to a dictionary of counts and dictionary
        of follower counts. Example return value with k=2:
        {
            "ac": {
                "count": 1,
                "followers": {"g": 1, "c": 2}
            },
            ...
        }

    Note: This function will similar to `build_dict`. We separated the 
    k-character and follower counting to explain each as distinct concepts. You
    should use the k-character counting code you wrote in `build_dict` as a 
    starting point.

    While the Markov model only needs to use `collect_counts` to generate text,
    our auto-grader will test the behavior of `build_dict` so that function 
    does need to work properly.
    """
    # create dict to store counts of each tuple
    counts = {}
    # consider each tuple excluding the last k-tuple, which has nothing following it
    for ind in range(len(contents)-k):
        # store current k-tuple and the letter following it
        current = contents[ind:ind+k]
        next = contents[ind+k]
        # if not in the counts dict, add the tuple as a key with a count value of 1 and followers dict
        if current not in counts:
            counts[current] = {"count": 1, "followers": {}}
            # add the current follower to the followers dict
            counts[current]["followers"][next] = 1
        else:
            # increment count
            counts[current]["count"] += 1
            # increment followers count or add new follower to dict with count 1
            if next not in counts[current]["followers"]:
                counts[current]["followers"][next] = 1
            else:
                counts[current]["followers"][next] += 1
    return counts


def generate_next_character(seed, txt_dict):
    """Randomly select the next character of a k-tuple using the follower
    counts to determine the probability.

    Args:
        seed (str): k-tuple to follow from
        txt_dict (dict): k-tuple count follower dictionary

    Returns:
        (str) of the next character
    """
    # simulate choosing next character with the correct probability by adding each character in follows the number of
    # times it appears after seed
    # could also simulate with random ints, but this avoids the need for matching int with a char
    nexts = []
    # add each follower to next list count number of times
    for follower in txt_dict[seed]["followers"]:
        for num in range(txt_dict[seed]["followers"][follower]):
            nexts.append(follower)
    # choose a random next letter from the list
    next_char = random.choice(nexts)
    return next_char


if __name__ == "__main__":
    """Main method call, do not modify"""
    display_dict(collect_counts("agggcagcgggcg",2))
    run_language()

