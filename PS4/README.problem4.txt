COMPSCI 260 - Problem Set 4, Problem 4
Due: Fri 8 Mar 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):

My solutions and comments for this problem are below.
-----------------------------------------------------
b) The optimal score of the local alignment of P63015 and O18381 is: 644.
The total number of locations in the table achieving this optimal score is 4, and the locations are [(136, 188), (137, 189), (138, 190), (139, 191)].
One optimal alignment aligns nucleotide 5-136 with nucleotides 57-188 (indices are inclusive).
P63015: HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRD (5-104)
        |||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| |||||| ||||||||||||||||
O18381: HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRD (57-156)

P63015: RLLSEGVCTNDNIPSVSSINRVLRNLASEKQQ                                                                     (105-136)
        ||| | |||||||||||||||||||||  | |
O18381: RLLQENVCTNDNIPSVSSINRVLRNLAAQKEQ                                                                     (157-188)

c) P63015 is paired box protein Pax-6 in the mouse, which is a "transcription factor with important functions in the
development of the eye, nose, central nervous system and pancreas. Required for the differentiation of pancreatic islet
alpha cells."[1] O18381 is a paired box protein Pax-6 in drosophila, and it is involved in eye morphogenesis.[2] They
are the same type of protein and seem to have overlapping functions in eye development/morphogenesis. The local
alignment results represent a region of high similarity, which would suggest it is regions with similar functions
that lead to highly conserved sequences and structure. Specifically, since the shared function of these two proteins is
eye development, the local alignment results are probably proteins that play a role in eye development. Even though it
returns 4 locations for the optimal score, we see that these four locations actually represent the same segment of the
sequence with slightly different start and end points, meaning that the highest score is only in one region.

1. https://www.uniprot.org/uniprotkb/P63015/entry
2. https://www.uniprot.org/uniprotkb/O18381/entry#function

d) V'(m,n) is the optimal local alignment of some substring of the first sequence ending at m (the last nucleotide of
the sequence) and some substring of the second sequence ending at n (the last nucleotide). In the global alignments, we
could just the value at m,n to be the optimal score because the alignment had to include all the nucleotides, so the
dp table would ensure the value at m,n was optimal overall, but in the local alignment, it is possible that the optimal
alignment does not include the nucleotides at m and n. Therefore, although V'(m,n) is the optimal score for a suffix of
the m-prefix of sequence 1 and a suffix of the n-prefix of sequence 2, there are other substrings that may have a better
score. In this case V'(m,n) is 34, which is much less than the optimal score of 644. However, depending on the
sequences, it is possible that V'(m,n) is the value of the best alignment, it just varies based on what the optimal
alignment is and if it includes nucleotide m of sequence 1 and nucleotide n of sequence 2.
