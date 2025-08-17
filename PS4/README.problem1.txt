COMPSCI 260 - Problem Set 4, Problem 1
Due: Fri 8 Mar 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) attached dp table as a pdf named DPTABLE.pdf

b) The score of an optimal alignment is -1, and there are 5 alignments that achieve this score.
The full set of optimal alignments is as follows:
-CGATCGAT
GCCAT---T

CGATCGAT–
-G-CC-ATT

CGATCGAT–
-GC-C-ATT

CGATCGAT
-G-CCATT

CGATCGAT-
-G--CCATT

c) An affline gap score takes into account the fact that a new gap requires a break in DNA, so there is a fixed cost
for opening the gap then lower linear cost for extending the gap. Therefore, we can look at how many consecutive gaps
each of the alignments has, and the first two alignments have several gaps of just a single nucleotide, each time the
cost of breaking the DNA must be paid, so alignments 2 and 3 will probably not be optimal. The fifth alignment also has
3 separate gap regions whereas 1 and 4 only have 2, so the third would most likely also not be optimal. Then,
depending on the value of the gap penalty, we may be able to rule out more. For example, if the gap penalty is decreased
significantly along with the addition of the affine penalty, the first alignment may be more optimal than the fourth
because there are more gaps which now have a reduced penalty relative to the mismatch penalty. However, the last point
is dependent on the gap penalty and sequences, so we primarily know we can eliminate alignments 2,3, and 5 as optimal.
