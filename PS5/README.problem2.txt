COMPSCI 260 - Problem Set 5, Problem 2
Due: Fri 29 Mar 2024, 5pm

Name: 
NetID: 

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 

My solutions and comments for this problem are below.
-----------------------------------------------------
a) look at code
ultrameticity: return false if any of the triplets are not ultrametric, true if all triplets are iterated through
without a return
additive: number of entries in dist = 0.5n^2 - 0.5n
    2 * len(dist) = n(n-1)

b)
dist_1 is not ultrametric: The triplet 1, 2, and 3 (distances 0.3, 0.7 and 0.6) violate ultrametricity
dist_1 is additive
dist_2 is ultrametric
dist_2 is additive

c) images attached

d) In the last problem set, our pairwise alignments indicated that mouse and human ATP synthase had a very high optimal
score and an optimal alignment with only a small number of mismatches and no gaps. The bacterial sequences had a
slightly higher optimal alignment with each other compared to with human and mouse ATP synthase sequences, but not
significantly higher, meaning that we cannot say that they were significantly closer to each other than the eukaryotes.
In our reconstructed tree, the similarity of human and mouse ATP synthase is clear, as they were the first pair merged
together and have a much lower merge height (0.05) than the other merges. The two bacterial sequences were also merged
with each other before any other sequences, indicating that they are most closely related to each other compared to
eukaryotes. The two fungi sequences were also merged together, and they have the same merge height (distance) as the two
bacterial sequences, which tells us that the fungi and bacterial sequences have the same level of genetic similarity
ignoring gap columns. Next, we see that the human and mouse cluster is more closely related to the fungi cluster than
the bacterial cluster. Finally, all the eukaryotes had the same evolutionary distance from the two bacteria sequences.