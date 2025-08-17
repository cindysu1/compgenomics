COMPSCI 260 - Problem Set 1b, Problem 3
Due: Fri 26 Jan 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) No, it is not possible to have overlapping ORFs within a single reading frame if we define ORFs as the longest
possible among those that share a given stop codon as described in the project description. An ORF begins with AUG, or
the start codon, and ends with a stop codon. AUG may also appear as a codon between the start and stop codon,
but in this case, it is translated into Methionine rather than starting a new ORF, so the start of one ORF will never
be in the middle of another. However, if we considered every ORF based on start and stop codons (not just the  longest
one), there could be overlapping ORFs when there are multiple start codons before a single stop codon. In this  case,
all the ORFs would share a stop codon and have a variable length depending on which start codon was being used.It is
possible to have overlapping ORFs in different reading frames since they are separate. For example, if a given mRNA is
5'-AUGCAAUGGUAAUGAAAUAA-3'. Reading frame 0 has triplets AUG CAA UGG UAA UGA AAU, and reading frame 2 has triplets GCA
AUG GUA AUG AAA UAA. We see that the ORF in frame 0 start with nucleotide 1 and end with nucleotide 12 while in frame 2,
the ORF is from nucleotides 6 to 20, so they are overlapping.

b-d) I decided to use regex and dicts to find all the start and stop codons in the sequence rather than iterating
through the entire sequence codon by codon and finding ORFs as I went, but I realized my approach might be overly
complicated and maybe more inefficient. I was thinking the time complexity may be less depending on the runtime of regex
 finditer.

refer to code in mentioned functions

e) When the minimum ORF length is 20 amino acids, there are 104 ORFs found in the SARS-CoV-2 genome, and the average
ORF length is 124.08 amino acids.
When the minimum ORF length is 40 amino acids, there are 34 ORFs found in the SARS-CoV-2 genome, and the average ORF
length is 321.59 amino acids.
When the minimum ORF length is 60 amino acids, there are 17 ORFs found in the SARS-CoV-2 genome, and the average ORF
length is 594.59 amino acids.

f) There are 12 ORFs in the SARS-CoV-genome. ORF10 spans from 29558-29674, and it is 117 nucleotides. The coordinates of
 the spike protein are 21563-25384, and there are 1273 amino acids in the spike protein after it is translated because
 the stop codon is not translated into an amino acid.

g) As we increase minimum ORF length, we would expect to identify less ORFs because we are increasing the criteria that
ORFs are filtered on. In other words, there is a certain amount of ORFs defined by start and stop codons, and setting a
minimum length filters for a subset of that, so setting a higher maximum makes this filter more selective. Increasing
minimum ORF length should also lead to an increase in average length of the identified ORFs because the ORFs that are
lower than the new minimum are not considered anymore, so the mean would be higher. My results do accord with these
expectations, as when the minimum length increases, the number of ORFs decreases while average length increases.

h) The orfs identified when the minimum length is 60 are as following:
frame: 0, start: 13768, stop: 21555, length: 7788
frame: 0, start: 25393, stop: 26220, length: 828
frame: 0, start: 26245, stop: 26472, length: 228
frame: 0, start: 27202, stop: 27387, length: 186
frame: 0, start: 27394, stop: 27759, length: 366
frame: 1, start: 266, stop: 13483, length: 13218
frame: 1, start: 15461, stop: 15667, length: 207
frame: 1, start: 21536, stop: 25384, length: 3849
frame: 1, start: 28274, stop: 29533, length: 1260
frame: 2, start: 2958, stop: 3206, length: 249
frame: 2, start: 6156, stop: 6350, length: 195
frame: 2, start: 10215, stop: 10400, length: 186
frame: 2, start: 21936, stop: 22199, length: 264
frame: 2, start: 26523, stop: 27191, length: 669
frame: 2, start: 27894, stop: 28259, length: 366
frame: 2, start: 28284, stop: 28577, length: 294
frame: 2, start: 28734, stop: 28955, length: 222

On the genome browser, there is are two overlapping genes: ORF1a and ORF1ab, and the function identifies one that
correlates to ORF1a (based on coordinates: 266-13483 and length) but not ORF1ab. There is another ORF that starts right
after the ORF1a identified that would have the same start and stop coordinates as ORF1ab if combined with ORF1a
(266-2155). On the genome browser, there is a note on ORF1ab that says translated by -1 ribosomal frameshift, which
explains why our function did not return it because we did not incorporate this. Also, the two consecutive fragments are
in different reading frames, which confirms that this is due to a shift in the middle of the ORF.
The starting coordinate of the S gene is also slightly off (by 27). This may be due to a new mutation in the
spike protein that changed the start codon identified by my function to a non-AUG codon, which may have shifted the
start codon 27 nucleotides down. My function also does not identify ORF10 or ORF7b because their products are less than
60 amino acids. There are also many more ORFs identified by my function than are shown in the genome browser, and this
may be due to not all ORFs being annotated on the genome browser, or potentially some ORFs being excluded from
annotation by some criteria I am not sure of.
