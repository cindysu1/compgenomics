COMPSCI 260 - Problem Set 5, Problem 3
Due: Fri 29 Mar 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a)
	       2       3       4       5       6       7
1	  0.6672  0.0071  0.0055  0.7170  0.0047  0.0047
2	          0.6661  0.6669  0.7231  0.6669  0.6669
3	                  0.0031  0.7154  0.0024  0.0024
4	                          0.7154  0.0008  0.0008
5	                                  0.7154  0.7154
6	                                          0.0000

b) The pairwise distance between student 6 and student 7 is 0 up to 4 decimal places, but this does not necessarily tell
us that they have identical spike protein sequences. Our compute_dist function only considers mismatches over
matches_or_mismatches, meaning it completely ignores any gaps. All columns that have no gaps are matches. Therefore, we
know that there are no mismatches between the sequences of student 6 and 7's spike protein sequences in the columns that
there are no gaps, but we don't know if there are gaps or not.

c) This distance metric is not ultrametric. The triplet 1, 2, and 5 (distances 0.6672, 0.7170 and 0.7231) violate ultrametricity
The distance is additive.

The distance is additive but not ultrametric, so we can use the NJ algorithm to construct a tree because the NJ
algorithm can be used on additive distance metrics, but UPGMA is more strict and can only be used on ultrametric
distance metrics.

e) The newick representation of the genomic sequences from the student are
(7:0.0000000,(6:-0.0000000,(4:0.0006876,(3:0.0017311,(1:0.0032891,(2:0.3371325,5:0.3860156):0.3272632):0.0011244):0.0005929):0.0000980):0);


g)
Student     Accession       Virus name                                              Common name of virus
1           QQH18545.1      Severe acute respiratory syndrome coronavirus 2         SARS-CoV-2 or COVID-19
2           AOL02453.1      Human coronavirus OC43                                  HCoV-0C43
3           QPJ72086.1      Severe acute respiratory syndrome coronavirus 2         SARS-CoV-2 or COVID-19
4           BCN86353.1      Severe acute respiratory syndrome coronavirus 2         SARS-CoV-2 or COVID-19
5           APT69856.1      Human coronavirus 229E                                  HCoV-229E
6           CAD0240757.1    Severe acute respiratory syndrome coronavirus 2         SARS-CoV-2 or COVID-19
7           CAD0240757.1    Severe acute respiratory syndrome coronavirus 2         SARS-CoV-2 or COVID-19

h) The results of the BLAST show that students 1, 3, 4, 6, and 7 have SARS-CoV-2 while students 2 and 5 have strains of
human coronavirus, which despite the similarity of their names, is a different virus than SARS-CoV-2. This matches
with our tree because 1, 3, 4, 6, and 7 are the subset that are very tightly clustered with each other, while 2 and 5
have much higher levels of accumulated mutations from the subset. All of their spike proteins are from SARS-CoV-2,
but we see that all of them except 6 and 7 have different accession numbers, meaning that the specific proteins are
different (due to mutations). The viruses Student 2 and 5 also have significantly difference in my tree, indicating that
although they are both human coronaviruses, the two strains (HCoV-0C43 vs HCoV-229E) are different and most likely have
had a lot of accumulated mutations. Furthermore, we see that student 6 and 7's queries actually have the same accession
number, indicating that not only are they both COVID-19 spike proteins, they are actually from the same virus. This
matches with my tree, where the distance between 6 and 7 is 0, indicating that they are identical based on the pairwise
distance metric we used.

i) Sequences 6 and 7 are the two SARS-CoV-2 sequences that are the most similar, and they have 1273 matches, 0 mismatches, and 0 gaps.
Sequences 1 and 3 are the two SARS-CoV-2 sequences that are the most different, and they have 1261 matches, 9 mismatches, and 3 gaps.
Sequences 2 and 5 are the two sequences that are the most different overall,and they have 299 matches, 781 mismatches, and 369 gaps.

These differences represent variation in the spike protein sequences of the given students. Gaps indicate either
insertions or deletions, and mismatches could be point mutations. It is helpful to compare the most different COVID-19
sequences to the most different overall because the COVID-19 sequences are all very closely clustered, so it useful to
have a reference to a greater level of accumulated mutations.

j) The two SARS-CoV-2 genomic sequences that are the most different are sequences 1 and 3, but looking at the
differences, we see there are only 9 mismatches and 3 gaps. Especially when we compare this to the overall most
different sequences that have 781 mismatches and 369 gaps. However, these mutations are in the spike protein, which
plays a very significant role in how the COVID-19 virus works, so even a small amount of divergence may indicate
significant evolutionary distance between virus strains. Students 6 and 7 have 0 gaps and 0 mismatches, indicating the
spike protein sequences isolated from them actually are identical. Because of this, I would guess that there was direct
transmission from one of them to the other or they both got it from the same source at the same time. This is because if
they got it from different sources, the spike protein would most likely have at least one non-match column due to random
mutation. For the rest of the students with SARS-CoV-2, it is more difficult because they have some mismatches or gaps,
but each pairing of students still has at most 12 indiscrepancies, so it is hard to say whether they were infected from
different sources of if mutations accumulated during their infection. However, since different strains of SARS-CoV-2 can
be seen to have at least 5-10 mutations in the spike protein, I think some of the students definitely could be infected
with a different strain. Since Students 1 and 3 have the most difference overall, they probably are the most likely to
have gotten it from different sources. The rest of the students fall somewhere on the spectrum of no differences to 12,
so it is definitely possible that some with higher deviation from the rest caught it from someone outside of the school,
 but some of the more similar sequences may have originated from the same source and accumulated mutations during the
 time they were spread, or the source itself may have mutated and transmitted a slightly different version.

This all excludes students 2 and 5, who we have established are infected with human coronaviruses, and their large
divergence from each other and all the SARS-CoV-2 sequences confirms that their infections are not related.

k)
The optimal score for the alignment of Student_3 and Student_7 is 6697
The optimal alignment is unique and it is
Student_3: MFVFLVLLPLVSIQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNI (1-100)
           |||||||||||| |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNI (1-100)

Student_3: IRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSCMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGY (101-200)
           ||||||||||||||||||||||||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: IRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGY (101-200)

Student_3: FKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETK (201-300)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: FKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETK (201-300)

Student_3: CTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSF (301-400)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: CTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSF (301-400)

Student_3: VIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYRYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPT (401-500)
           ||||||||||||||||||||||||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: VIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPT (401-500)

Student_3: NGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITP (501-600)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: NGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITP (501-600)

Student_3: GTNTSNQVAVLYQGVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLG (601-700)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: GTNTSNQVAVLYQGVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLG (601-700)

Student_3: AENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGF (701-800)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: AENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGF (701-800)

Student_3: NFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAM (801-900)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: NFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAM (801-900)

Student_3: QMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGR (901-1000)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: QMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGR (901-1000)

Student_3: LQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGT (1001-1100)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: LQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGT (1001-1100)

Student_3: HWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDL (1101-1200)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: HWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDL (1101-1200)

Student_3: QELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT                            (1201-1273)
           |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: QELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT                            (1201-1273)

The optimal score for the alignment of Student_1 and Student_7 is 6639
The top most alignment is
Student_1: MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAI--SGTNGTKRFDNPVLPFNDGVYFASTEKSNI (1-98)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  ||||||||||||||||||||||||||||||
Student_7: MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNI (1-100)

Student_1: IRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGV-YHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGY (99-197)
           ||||||||||||||||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: IRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGY (101-200)

Student_1: FKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETK (198-297)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: FKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETK (201-300)

Student_1: CTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSF (298-397)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: CTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSF (301-400)

Student_1: VIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPT (398-497)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: VIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPT (401-500)

Student_1: YGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIDDTTDAVRDPQTLEILDITPCSFGGVSVITP (498-597)
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||
Student_7: NGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITP (501-600)

Student_1: GTNTSNQVAVLYQGVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSHRRARSVASQSIIAYTMSLG (598-697)
           |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| |||||||||||||||||||
Student_7: GTNTSNQVAVLYQGVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLG (601-700)

Student_1: AENSVAYSNNSIAIPINFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGF (698-797)
           ||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: AENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGF (701-800)

Student_1: NFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAM (798-897)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: NFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAM (801-900)

Student_1: QMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILARLDKVEAEVQIDRLITGR (898-997)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ||||||||||||||||||
Student_7: QMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGR (901-1000)

Student_1: LQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGT (998-1097)
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: LQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGT (1001-1100)

Student_1: HWFVTQRNFYEPQIITTHNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDL (1098-1197)
           ||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: HWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDL (1101-1200)

Student_1: QELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT                            (1198-1270)
           |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Student_7: QELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT                            (1201-1273)

Looking at the alignment of Sequences 3 and 7, we see that there are only 3 mismatches and no gaps. The mutations from
sequence 7 are as follows: S-->I at 13, W-->C around 150, and L-->R around 450. The L452R mutation is a mutation of
concern that the NYT article highlights, but it appears in many variants. All of the variants have more than 3 mutations
compared to the original spike protein, and the mutations found in Student 3 do not match with any of the variant maps
other than L452R. Because of this, I believe Student 3 still has the original variant like Student 7 since there are
not any characteristic mutations that suggest it is a variant, or it is some intermediate form that is not exactly
aligned with any of the variant. In the spike protein region, Delta has 8 mismatches, Beta has 8, Alpha has 6 and 3
deletions, and Omicron has 30.

Sequences 1 and 7 produce an alignment with 3 gaps and 6 mismatches. In sequence 1, near the beginning of the sequence,
there is an HV deleted, then a Y deleted slightly after. The mismatches are: N-->Y, A-->D, P--H, T-->I, S-->A, and D-->H.
Looking at the map for the Alpha Variant (B.1.1.7 Lineage), we see that the deletions and mismatches are exactly the
same as listed, so Student 1 has the Alpha Variant.
