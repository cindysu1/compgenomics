import random
import timeit
import sys

sys.setrecursionlimit(10**6)  # Adjust the limit as needed
# random_list needs to be available as a global variable
# for the timeit function to work properly
random_list = None
ind = 0;


def brute_force(score_list):
    """Get the maximum collective similarity score using brute force.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """

    # store max collective similarity
    max_sum = 0

    # outer loop iterates through the entire list
    for index in range(len(score_list)):
        # will store the current collective similarity for sublists starting at index
        cur_total = 0

        # inner loop, start with index to get a one-element sublist, then iterate through the end of score_list
        for inner in range(index, len(score_list)):
            cur_total += score_list[inner]
            # compares current collective similarity to the max
            if cur_total > max_sum:
                max_sum = cur_total

    return max_sum  # the computed maximal score


def divide_conquer(score_list):
    """Get the maximum collective similarity score using divide and conquer.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """
    # base case when list is empty
    if len(score_list) == 0:
        return 0
    # base case when there is only one element in score_list, the max must be that element
    if len(score_list) == 1:
        return score_list[0]
    # base case when there are only two elements in score_list
    if len(score_list) == 2:
        return max(score_list[0], score_list[1])

    # calculate midpoint
    mid = len(score_list) // 2

    # recursive call on first half of list
    left_max = divide_conquer(score_list[:mid])
    # recursive call on second half of list
    right_max = divide_conquer(score_list[mid:])
    # use helper method to find max sublist including the midpoint
    mid_max = max_middle(score_list)
    return max(left_max, right_max, mid_max, 0)    # the computed maximal score of the current list

def max_middle(score_list):
    """Get the maximum collective similarity score including the midpoint of a list being split to divide and conquer
    by extending left and right from the midpoint

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """
    mid = len(score_list) // 2
    # cur_sum stores the running sum starting from the midpoint up to a certain element in the loop
    cur_sum = score_list[mid]
    # max_sum stores the max sum overall, starts with the value of the middle element
    max_sum = cur_sum
    # find max collective similarity extending left from the midpoint
    for i in range(mid-1, -1, -1):
        cur_sum += score_list[i]
        if cur_sum > max_sum:
            max_sum = cur_sum

    # set cur_sum to max_sum from left
    # if no sublist on the left led to a higher sum, max_sum is still the middle element's value
    cur_sum = max_sum

    # build upon left collective sum by extending right
    for i in range(mid+1, len(score_list)):
        cur_sum += score_list[i]
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum



def linear(score_list):
    """Get the maximum collective similarity score in linear time.

    Args: score_list (list): list of integer similarity scores

    Returns: (int) of the maximal computed score
    """
    # max_so_far stores the max of any sublist so far
    max_so_far = 0
    # max_including_here stores the maximum of sublists ending at the current element in the loop
    max_including_here = 0

    for score in score_list:
        # if the max of any sublist up to the previous element is negative, it is better to start over at 0
        if max_including_here < 0:
            max_including_here = 0
        # add the current value to max_including_here
        max_including_here += score
        # compare to global max and set new max_so_far if necessary
        if max_including_here > max_so_far:
            max_so_far = max_including_here

    return max_so_far  # the computed maximal score


def run_collective_similarity():
    """Run collective similarity and collect timing for each algorithm.

    Note: there is no reporting in this problem, `brute_force`,
    `divide_conquer`, and `linear` will be evaluated for correctness.
    """

    # Declare random_list as the same global variable defined
    # on line 7 above for use in the timeit library below.
    global random_list

    # You can use this to test the correctness of your code by using
    # sample_list as an input to each function.  You could also consider
    # creating other sample lists as tests, including a test case where
    # the right answer of zero occurs when an empty list would be optimal.

    sample_list = [2, -3, -4, 4, 8, -2, -1, 1, 10, -5]
    sample_2 = [-10, -10, -100, -10000, -100000, -10]

    brute_force(sample_list)
    divide_conquer(sample_list)
    linear(sample_list)

    # print(brute_force(sample_list))
    # print(divide_conquer(sample_list))
    # print(linear(sample_list))

    # This part below is used to test the runtime of your code, an example is
    # given below for brute force algorithm with a random list of length 100.
    # You will have to measure the runtime of each algorithm on every input size
    # given in the problem set.

    allowed_scores = [i for i in range(-10, 11)]

    brute = []
    div_con = []
    lin = []
    # random_list = [random.choice(allowed_scores) for _ in range(10 ** 8)]
    for i in range(2,9):
        length = 10**i
        print("generating random list of length " + str(length))
        random_list = [random.choice(allowed_scores) for _ in range(length)]
        if i < 6:
            print("starting brute force on length " + str(length))
            brute.append(timeit.timeit("brute_force(random_list)",
                                      setup="from __main__ import brute_force, random_list",
                                      number=1))
            print(str(length) + " brute time : " + str(brute[-1]))
        if i < 8:
             div_con.append(timeit.timeit("divide_conquer(random_list)",
                                       setup="from __main__ import divide_conquer, random_list",
                                       number=1))
             print(str(length) + " rec time : " + str(div_con[-1]))
        lin.append(timeit.timeit("linear(random_list)",
                                       setup="from __main__ import linear, random_list",
                                       number=1))
        print(str(length) + " lin time : " + str(lin[-1]))

    print(f"{'input length':<12}\t{'10^2':>8}\t{'10^3':>8}\t{'10^4':>8}\t{'10^5':>8}\t{'10^6':>8}\t{'10^7':>8}"
          f"\t{'10^8':>8}")
    print(f"{'brute force':<12}\t{brute[0]:>8.3g}\t{brute[1]:>8.3g}\t{brute[2]:>8.3g}\t{brute[3]:>8.3g}")
    print(f"{'div + conquer':<12}\t{div_con[0]:>8.3g}\t{div_con[1]:>8.3g}\t{div_con[2]:>8.3g}\t{div_con[3]:>8.3g}"
          f"\t{div_con[4]:>8.3g}\t{div_con[5]:>8.3g}")
    print(f"{'linear':<12}\t{lin[0]:>8.3g}\t{lin[1]:>8.3g}\t{lin[2]:>8.3g}\t{lin[3]:>8.3g}"
          f"\t{lin[4]:>8.3g}\t{lin[5]:>8.3g}\t{lin[6]:>8.3g}")


if __name__ == "__main__":
    """Run run_collective_similarity(). Do not modify this code"""
    run_collective_similarity()
