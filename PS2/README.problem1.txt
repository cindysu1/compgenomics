COMPSCI 260 - Problem Set 2, Problem 1
Due: Fri 9 Feb 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) The probability of a portion of length m from the genome matching the read sequence is (1/4)^m because each position
in the genome has a 25% chance of matching the nucleotide in the reading sequence since there are 4 nucleotides, and we
assume both the genome and the read are generated at random from a uniform nucleotide distribution. Then, we calculate
the expected number of times a read sequence will occur in a genome of size n by multiplying the probability of a
fragment being the read sequence by the number of possible substrings there could be. The sequence could start at any
nucleotide in the genome, but there have to be at least m nucleotides after it to match the full read sequence.
Therefore, there are n - m + 1 potential nucleotides for the sequence to start in the genome. The expected number of
reads in the genome is (n-m+1)*(1/4)^n. However, this does not account for the fact that if a sequence matches, there
are less potential start nucleotides.

b) A brute force algorithm would iterate through all n-m-1 nucleotides that could potentially start the read sequence
and check each of them. It could check either in a nested for loop that checks the reference genome and read sequence
nucleotide by nucleotide and stops if there is a match or use python string matching functions to check if the substring
of length m starting at a given nucleotide matches the read sequence. In either case, the worst case running time is
O(n*m) because the outer for loop iterates through n-m-1 nucleotides, and for each iteration, checks up to
m nucleotides to see if the genome matches the read sequence, so the worst case runtime has an upper bound of n*m
asymptotically, but we cannot be sure it is Θ(n*m) because if m is large enough, the -m in n-m-1 is significant.

c) The brute force approach's time complexity varies linearly with k, m, and n, as it looks through the entire genome
for each distinct read, so if there are a small number of reads, the brute force approach may be more efficient than the
pre-processing approach. Alternatively, it may only iterate through the genome once but check if each fragment
matches any of the k reads in an inner loop, but this would still yield a worst case runtime of Θ(kmn). With the
pre-processing approach, there is a high cost of making the pre-processed data structure. The cost is only worth it if
there are enough sequences that the faster lookup time balances out the added cost. Another trade off is that the
pre-processing approach takes more space because of the extra data structure, but the main trade-off is the time to
build the data structure in the pre-processing approach vs. the time to repeatedly iterate through the entire genome in
the brute force approach.

To get a better idea of the number of reads you would need to map in order for the pre-processing approach to be worth
it, we can set up an inequality with the total runtime for both methods and solve it for k. This will not yield an exact
value for the minimum value of k because we are using asymptotic terms, but it will help understand how k scales.
k(m*log n) + n*log n < k*m*n
n*log n < k*m*n - k*m*log n
(n*log n)/(m*n - m*log n) < k
k > (n*log n)/(m(n-log n))

When n is very large, log n is much less than n (e.g. if n = 1000000000, log n = 9), so the denominator can be
approximated to mn since n - log n ~ n, making the inequality: k > (n*log n)/(mn) --> k > (log n)/m
We know that a linear function grows asymptotically faster than a log function, so the limit to (log n)/m is 0 as n and
m approach infinity (the asymptotic behavior of the expression). Therefore, we see that when n and m are very large, any
positive value of k makes the initial cost worth it.


