COMPSCI 260 - Problem Set 2, Problem 2
Due: Fri 9 Feb 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 

My solutions and comments for this problem are below.
-----------------------------------------------------
a) When n is the length of the input list, the inefficient brute force algorithm's worst case run time is Θ(n^3)
since it iterates through all n elements in the outer loop, then the inner loop iterates through every possible sublist,
and within the inner loop, summing the collective similarity takes O(n) time because it looks at each value in the
sublist for each iteration of the inner loop.

We can make the brute force approach more efficient by storing a variable for the current sum in the other loop. The
outer loop iterates though the input list, while the inner loop iterates through the rest of the list to obtain the
collective similarity of every sublist. However, as long as we are in the same iteration of the outer loop, the sum of a
certain sublist is the sum of the sublist up to the previous element plus the current element, which saves us from
summing up all the values independently for each sublist. For each value in the inner loop, after we add to the curent
sum, we can compare this sum to a global maximum sum. Therefore, summing the collective similarity does not take
O(n) time for every single iteration now, and instead it just has to retrieve the value at a current index, which takes
constant time. Therefore, the total runtime is Θ(n^2).

b) Recursion can help us write a more efficient algorithm because we can use it to divide the larger problem into
smaller problems that satisfy the optimal substructure property. For example, if we broke the list into two halves and
found the max collective similarity in each half, this max would be the max of the whole list unless there was a sublist
that had a higher collective similarity that crossed the midpoint. To account for a max sublist that could cross the
midpoint, I have a helper function that starts at the midpoint then iterates through the list to the left, storing the
max value. Then I iterate through the right side, building on the max sublist value from the left if it is greater than
the midpoint or just starting from the midpoint otherwise. The base cases of this algorithm are if the length of the
list is 0 (returns 0), if the length of the list is 1 (returns the value of the sole element), or if the sublist is 2
(returns the max of the two elements). Therefore, we have to consider the left side, right side, and a sublist
containing the midpoint and the max out of those three will be the max of the combined elements or 0 if all the elements
are less than 0 since in that case, an empty list is optimal.

As for the worst-case running time, we can use a recurrence relation. We will define T(n) as the time required to
calculate the maximum collective similarity of a list of length m with divide_and_conquer.
T(n) = T(n/2) + T(n/2) + n = 2*T(n/2) + n.
    This is because the function calls two copies of itself, each running on a sublist half the size of the original,
    and it also calls max_middle, which iterates through all the elements in the list once and only does constant-time
    functions within the for loop. Therefore, the runtime for max_middle is O(n), and the runtime for each recursive of
    divide_and_conquer is T(n/2).
Using the master theorem with a = 2, b = 2, and f(n) = n, we see that the T(n) can be bounded asymptotically by
Θ(n*log n).

c) In this approach, we store the max so far and max including here (maximum sublist sum that ends at a given value).
This is useful because when we want to move the end element of the sublist one element to the right, we know that we can
just build upon the previous max including here value if it is greater than 0 rather than recalculating the maximum
sublist sum, since at a given index n, the sublist up to n-1 is part of the sublist up to n. As long as the maximum
including here is positive, we know it is optimal to keep building upon that because it will always have a higher value
than the sublist starting at that point that begins at 0. If the max sum of the sublist at a certain point dropped below
0, it would be optimal to start with an empty list with a sum of 0 for the subsequent elements. If the maximum until
here value exceeds max so far, then we update max so far to equal the new value. This maintains the meaning of the
two variables because max including here is updated every time we change the ending point of the sublist, while max so
far stores the overall max which may be a previous sublist not including the current element.

d) Evaluated runtimes
input length	    10^2	    10^3	    10^4	    10^5	    10^6	    10^7	    10^8
brute force 	0.000369	  0.0374	    3.74	     385
div + conquer	0.000109	 0.00134	  0.0147	   0.165	    2.11	      23
linear      	9.72e-06	7.01e-05	0.000711	 0.00735	  0.0753	   0.759	     7.9

e) The asymptotic run time of the brute force approach is Θ(n^2) as described in (a), and looking at the evaluated
run times in (d), we see that the measurements align with our calculated runtime, as increasing the input size n by a
factor of 10 causes the run time to increase by about a factor of 100. Therefore, we can estimate the run times of
inputs of length 10^6, 10^7, 10^8, and 10^9 to be about 3.9e4, 3.9e6, 3.9e8, and 3.9e10 seconds respectively.

The asymptotic run time of the divide and conquer approach is Θ(n log(n)). If we want to compare the runtimes of two
input sizes, say 100 and 1000, we see that the proportion of the runtimes is:
[1000 * log (1000)] / [100 * log (100)] which simplifies to 10 * log(100) of 1000. Multiplying this by the
runtime of n = 100, we see that our evaluated runtimes agree with this relation. Generalizing this to values input
values x and y, we see that the runtime of y = y/x * log(x) of y * runtime of x.
runtime for (n = 10^8) = 23 * 10 * log(10^7) of 10^8 = 262
runtime for (n = 10^9) = 262 * 10 * log(10^8) of 10^9 = 2948

The asymptotic run time of the linear algorithm is Θ(n), and in (d), we observe the run time increases proportionally to
the increase in the input size. For every factor of 10 n is increased by, the run time increases by a factor of 10, so
we can estimate the run time when n = 10^9 to be around 80.

For all three approaches, the increase is not exactly proportional to n or log n but this may just be due to a constant
coefficient or operations that add to the run time that are less than the asymptotic term.

Estimated runtimes
input length	    10^6	    10^7	    10^8        10^9
brute force 	   39000	   3.9e6	   3.9e8	  3.9e10
div + conquer		 	  	         	     262	    2948
linear      	                                	      80

f) As mentioned before, the relationship between the list length n and the running time depends on the asymptotic run
time of a given algorithm. Namely, for the brute force algorithm, the run time varies proportionally to n^2; for the
divide and conquer, the run time varies proportionally to n log n; and for the linear algorithm, the run time varies
linearly with n. For all the algorithms, increasing n increases run time, and for a given list length, brute force takes
the most time, then divide and conquer, then linear, with the differences in runtimes increasing as n increases.
Copied from part e):
The asymptotic run time of the brute force approach is Θ(n^2) as described in (a), and looking at the evaluated
run times in (d), we see that the measurements align with our calculated runtime, as increasing the input size n by a
factor of 10 causes the run time to increase by about a factor of 100.
The asymptotic run time of the divide and conquer approach is Θ(n log(n)). If we want to compare the runtimes of two
input sizes, say 100 and 1000, we see that the proportion of the runtimes is:
[1000 * log (1000)] / [100 * log (100)] which simplifies to 10 * log(100) of 1000. Generalizing this to values input
values x and y, we see that the runtime of y = y/x * log(x) of y * runtime of x.
The asymptotic run time of the linear algorithm is Θ(n), and in (d), we observe the run time increases proportionally to
the increase in the input size. For every factor of 10 n is increased by, the run time increases by a factor of 10.