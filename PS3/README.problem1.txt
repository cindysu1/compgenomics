COMPSCI 260 - Problem Set 3, Problem 1
Due: Fri 23 Feb 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): none

My solutions and comments for this problem are below.
-----------------------------------------------------
a) First, I will find each suffix in the string then sort them alphabetically, with $ sorting first. Each character in
the sequence can be the prefix of a suffix, so there should be one suffix starting at each position.
$
A$
AGGCTGCA$
CA$
CTGCA$
GCA$
GCTGCA$
GGCTGCA$
TGCA$

Then, to create the Burrows-Wheeler Matrix, I will store the cyclic permutations of each substring starting at a given
position, in other words, I will wrap each string around after the $ until it contains all the characters in the
original string.
$AGGCTGCA
A$AGGCTGC
AGGCTGCA$
CA$AGGCTG
CTGCA$AGG
GCA$AGGCT
GCTGCA$AG
GGCTGCA$A
TGCA$AGGC

Then, the BWT is the last column of the BWM or AC$GGTGAC.

b) I will use the append and sort method. We are given a BWT, and we can find the character that follows each character
in the BWT because by the wraparound property, the last column wraps around to the first column. Then, given the
definition of a BWT, we know that the first column is sorted in alphabetical order, so if we sort the characters in the
BWT, we have the first column.
ATGAC$C --sort--> SAACCGT
Then, we combine the corresponding rows to obtain 2 character substrings, with the first character being from the BWT
and second from the sorted first column.
A$
TA
GA
AC
CC
$G
CT
Then, we can sort these substrings by the first column again, which would yield the first two columns of the BWM.
$G
A$
AC
CC
CT
GA
TA
The BWT can again be used to extend the substring, as it is still the last column of the BWM, and we repeat the last
step by appending the BWT to the beginning of the substring then sorting again to yield the first 3 columns of the BWM.
A$G      $GA
TA$      A$G
GAC      ACC
ACC  --> CCT
CCT      CTA
$GA      GAC
CTA      TA$
We repeat the append and sort steps until we obtain the whole matrix
A$GA      $GAC
TA$G      A$GA
GACC      ACCT
ACCT  --> CCTA
CCTA      CTA$
$GAC      GACC
CTA$      TA$G

A$GAC      $GACC
TA$GA      A$GAC
GACCT      ACCTA
ACCTA  --> CCTA$
CCTA$      CTA$G
$GACC      GACCT
CTA$G      TA$GA

A$GACC      $GACCT
TA$GAC      A$GACC
GACCTA      ACCTA$
ACCTA$  --> CCTA$G
CCTA$G      CTA$GA
$GACCT      GACCTA
CTA$GA      TA$GAC

A$GACCT      $GACCTA
TA$GACC      A$GACCT
GACCTA$      ACCTA$G
ACCTA$G  --> CCTA$GA
CCTA$GA      CTA$GAC
$GACCTA      GACCTA$
CTA$GAC      TA$GACC

Since there are 7 characters in the BWT, we know that the original sequence is also 7 characters (including the $), so
the BWM is complete because there are 7 columns. Reading any gives us the original sequence, which is GACCTA.

c. To implement forward_bwt, I plan on making a suffix array, then finding the BWT by getting the character at the index
before the prefix to each suffix. This avoids making the entire BWM to just get the last character. The ASCII value of $
is less than that of any letter, and since we are assuming that any input string contains no characters that sort
before the $ character, we can use a simple string comparison or array sort to find the correct order.

d. The BWT of the sequence GGACTAACGGACTAACGGACTAACGGACTAC$ is CTTTTAAAGGGGAAAAAAAAGGGG$CCCCCCC

e. The decoded message in the mystery text reads says the following:
Four score and seven years ago our fathers brought forth, on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived, and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting-place for those who here gave their lives, that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we cannot dedicate, we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth. --Abraham Lincoln$
