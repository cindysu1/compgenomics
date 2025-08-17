COMPSCI 260 - Problem Set 3, Problem 3
Due: Fri 23 Feb 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) Since each fragmentation is random with respect to location and each fragment is at least L nucleotides, we see that
the total number of nucleotides sequenced by all the reads is R*L, since there are R sequence reads of length L. The
significance of the random fragmentation is that any sequenced nucleotide has an equal probability of being any
nucleotide in the genome, so we don't need to account for any special factors. Then, the find the coverage of C, we look
the total number of nucleotides sequenced divided by the number of nucleotides in the genome (G), as this gives us the
expected number of times any give nucleotide has been sequenced. C = (R*L)/G

b) Since we are ignoring edge effects, each position i will be sequenced if a read covers any of the following ranges:
from i-(L-1) to i, from i-(L-2) to i+1, from i-(L-3) to i+2, .... , from i to i+L-1. Therefore, there are L potential
reads indices that would sequence i, and the probability of i being sequenced in a genome of length G is L/(G-L+1)
because a read cannot start within the last L-1 nucleotides and be L nucleotides long. Since L is much, much smaller
than G, this is approximately L/G. The complement (probability that nucleotide i is not sequenced by a given read) is
1-L/G. Since there are R reads, the probability that a specific location in the genome will not be covered by any of the
R reads is (1-L/G)^R. In part (a), we found that C = (R*L)/G, so it follows that C/R = L/G and the probability can be
rewritten as (1-C/R)^R. The limit as R approaches infinity of (1-C/R)^R = e^-C. We can use this limit equation because
genome sizes are very large, then our sequencing technique involves making billions of copies of the genome and
fragmenting each copy into many different pieces that each produce a read, so R is a very large number. e^-C is the
probability that a specific location in the genome is not covered by any of the reads, so to find the expected number of
nucleotides that remain unsequenced, we multiply this probability by the number nucleotides in the genome, so the
expected number of unsequenced nucleotides is G*e^-C.

c) Contigs are sets of contiguously assembled nucleotides, meaning they are separated by one or more unsequenced
nucleotides in the genome. Therefore, we know that every contig is followed by an unsequenced nucleotide. Given a random
read, the probability of the nucleotide after the end of that read being unsequenced is e^-C as calculated in (b). To
find the expected number of contigs, we consider that every read has the possibility of being followed by an unsequenced
nucleotide, so the expected number of contigs is R*e^-C.

Then, to calculate the expected length of each contig, we simply take the length of the genome minus the number of
unsequenced nucleotides and divide it by the expected number of contigs. Therefore, the expected length of each contig
is (G-G*e^-C)/(R*e^-C) = e^C(G-G*e^-C)/R = (G*e^C - G*e^C*e^-C)/R = (G*e^C-G)/R nucleotides.

d) I chose to ignore the edge effect as we have been doing, as it only affects a relatively very small number of reads.
Specifically, after the first L-1 nucleotides and before the last L-1 nucleotides, any nucleotide has an equal
probability of being sequenced. This means that only 2L-2 nucleotides will be effected, and since L is significantly
less than G, the model should still perform quite well.

Another approach would be to expand the potential start indexes from 0:G-L+1 to 0-L+1:G because this allows the first
and last L-1 nucleotides to be sequenced with the same probability as any other nucleotide in the sequence. With this
approach, we would still only increment the list elements in the proper range (0-G) but use the expanded range just for
the sake of negating the edge effect.

e)
The values for simulation 1 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 19971
Number of contigs = 233
Average length of contigs = 14935.7511 nucleotides

The values for simulation 2 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 22303
Number of contigs = 248
Average length of contigs = 14022.9758 nucleotides

The values for simulation 3 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 21216
Number of contigs = 233
Average length of contigs = 14930.4077 nucleotides

The values for simulation 4 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 20813
Number of contigs = 229
Average length of contigs = 15192.9607 nucleotides

The values for simulation 5 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 22063
Number of contigs = 239
Average length of contigs = 14552.0418 nucleotides

The values for simulation 6 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 21526
Number of contigs = 236
Average length of contigs = 14739.3008 nucleotides

The values for simulation 7 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 20303
Number of contigs = 231
Average length of contigs = 15063.6277 nucleotides

The values for simulation 8 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 19961
Number of contigs = 221
Average length of contigs = 15746.7873 nucleotides

The values for simulation 9 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 22344
Number of contigs = 255
Average length of contigs = 13637.8706 nucleotides

The values for simulation 10 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 19469
Number of contigs = 221
Average length of contigs = 15749.0136 nucleotides

The values for simulation 11 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 19790
Number of contigs = 227
Average length of contigs = 15331.326 nucleotides

The values for simulation 12 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 20061
Number of contigs = 228
Average length of contigs = 15262.8947 nucleotides

The values for simulation 13 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 16974
Number of contigs = 222
Average length of contigs = 15689.3108 nucleotides

The values for simulation 14 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 19985
Number of contigs = 230
Average length of contigs = 15130.5043 nucleotides

The values for simulation 15 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 20216
Number of contigs = 249
Average length of contigs = 13975.0402 nucleotides

The values for simulation 16 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 23706
Number of contigs = 230
Average length of contigs = 15114.3261 nucleotides

The values for simulation 17 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 22073
Number of contigs = 245
Average length of contigs = 14195.6245 nucleotides

The values for simulation 18 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 22813
Number of contigs = 243
Average length of contigs = 14309.4156 nucleotides

The values for simulation 19 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 19114
Number of contigs = 214
Average length of contigs = 16265.8271 nucleotides

The values for simulation 20 are as follows:
Empirical Coverage = 5.1429
Number of nucleotides not covered by any read = 16319
Number of contigs = 199
Average length of contigs = 17505.9397 nucleotides

f) The average empirical coverage is 5.143. The average number of nucleotides not covered by any read is
20551.0. The average number of contigs is 231.65. The average length of each contig is 15067.5 nucleotides.
All the observed values are almost the same as the calculated, with the small variation being reasonable differences
based on randomly generated trials.

Computed Values using a-c
G = 3.5*10^6, R = 4*10^4, L = 450
C = (R*L)/G = 4*10^4*450 / 3.5*10^6 = 5.143. The experimental value is the same

Unsequenced nucleotides = G*e^-C = 3.5*10^6 * e^-5.143 = 20440.5. The experimental value is slightly larger, but seems
to be due to the randomly generated nature of the reads and maybe the edge effect.

# of contigs = R*e^-C = 4*10^4 * e^-5.143 = 233.6. The experimental value of 231.65 is close to the calculated value.

Average length of contigs = G(e^C-1)/R = 3.5 * 10^6 (e^5.143-1) / (4*10^4) = 14895. The experimental value of 15067.5 is
larger but very close, but this is due to the experimental number of contigs being lower.

g) Unsequenced nucleotides = G*e^-C = 3*10^9 * e^-7.5 = 1.65*10^6 nucleotides
C = (R*L)/G --> R = C*G/L = 7.5 * 3*10^9 / 500 = 4.5*10^7 reads

h) Each read will need to compared to another read and that reads reverse complement, so there are 2 comparisons to
check whether or not two reads match to account for the potential relative orientations (you don't need to test all 4
permutations because either the two original reads match, or one matches the reverse complement of the other, but
reverse complementing either one will do the job). One possible complicating factor is that the first read we are
comparing needs to compared to all other reads except for itself, but then the second does not need to be compared to
itself or the first read, and the third does not need to be compared to the first, second, or third, and so on. In this
case, the number of read comparisons would be 2(R-1) + 2(R-2) + 2(R-3) + .... + 2(R-(R-1)) + 2*1 = 2(R-1 + R-2 + R-3 + .
.. + 1) = 2(R(R-1)/2) = R(R-1) = 2.025*10^15

For a simplified brute force analysis, we would just assume each read is being compared to all other reads despite the
later ones having already been compared to the earlier ones. In this case, each of the R reads needs to be compared to
R-1 reads as well as their reverse complements, yielding 2R(R-1) read comparisons. Given 4.5*10^7 reads, there would be
approximately 4.05*10^15 read comparisons.

i) 2.025 *10^15 comparisons * 1 second/4*10^7 comparisons * 1 hour/3600 seconds * 1 day/ 24 hours * 1 year/365 days =
1.605 years.
Simplified/inefficient model:
4.05*10^15 comparisons * 1 second/4*10^7 comparisons * 1 hour/3600 seconds * 1 day/ 24 hours * 1 year/365 days =
3.21 years.

j)
# of contigs = R*e^-C = 4.5*10^7 * e^-7.5 = 24888
Average length of contigs = G(e^C-1)/R = 3 * 10^9 (e^7.5-1) / (4.5*10^7) = 120469 nucleotides
Unsequenced nucleotides = G*e^-C = 3*10^9 * e^-7.5 = 1659253 nucleotides
To find the average length of an unsequenced region between two adjacent contigs, we take the number of unsequenced
nucleotides and divide it by the number of unsequenced regions. The number of unsequenced regions is the number of
contigs - 1 because each pair of contigs is separated by one unsequenced region and to account for the first and last
contig.
Average length of unsequenced region = 1659253/24887 = 66.7 nucleotides

k) Celera started attempting to sequence the human genome in 1999 and released a draft in 2001, so the estimate of 1.6
years using the more accurate calculation of read comparisons seems to make sense with this timeline, as the extra time
oculd have been used to figure out logistical issues or a multitude of other reasons. The sheer number of comparisons
necessary using this technique is shocking (I've never heard of the prefix peta- for 10^15). Also, it is impressive how
efficient Celera must have been to pull off such a large feat in such a short amount of time.