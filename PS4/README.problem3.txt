COMPSCI 260 - Problem Set 4, Problem 3
Due: Fri 8 Mar 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
b) The optimal score for the alignment of atpa_hs and atpa_ec is 1270
The top most alignment is
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |                                                | |     ||            |   |  ||  | |||      ||
atpa_ec: M-------------------------------------------QLNSTEISELIKQRIAQFNVVSEAHNEGTIVSVSDGVIRIHGLADCMQGEMISLPG (1-57)

atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
               |||| | || || |      ||  || || |  ||||  ||||||  ||  ||||||        |   ||| | | ||  | ||| |||||
atpa_ec: NRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVGRGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMI (58-157)

atpa_hs: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         |||||||||||||||||||  ||| ||||              ||||||||| ||    |  |    |   |||| ||||  | ||||||| || |||||
atpa_ec: PIGRGQRELIIGDRQTGKTALAIDAIINQR--------DSGIKCIYVAIGQKASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYF (158-249)

atpa_hs: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMN----DAF-------GGGSLTALPVIETQAGDVSAYIPTNVISIT (301-389)
         || |  ||||||||||||||||| |||||||||||| ||||||||||||||||  |     ||         ||||||| ||||||||||  ||||||||
atpa_ec: RDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLERAARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISIT (250-349)

atpa_hs: DGQIFLETELFYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIY (390-489)
         |||||||| ||  ||||| | | |||||| ||||  ||   |     |||||| ||| || |||| ||   |  |   |||||| || ||    |  |
atpa_ec: DGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQYRELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLF (350-449)

atpa_hs: AGVRGYLDKLEPSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLKEIVTNFLAGFEA                                     (490-553)
         |  ||||   | |||  || | |  |   |  |   |   |        ||| |   | |
atpa_ec: AAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYNDEIEGKLKGILDSFKATQSW                                     (450-513)

The bottom most alignment is
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |                                                | |     ||            |   |  ||  | |||      ||
atpa_ec: M-------------------------------------------QLNSTEISELIKQRIAQFNVVSEAHNEGTIVSVSDGVIRIHGLADCMQGEMISLPG (1-57)

atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
               |||| | || || |      ||  || || |  ||||  ||||||  ||  ||||||        |   ||| | | ||  | ||| |||||
atpa_ec: NRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVGRGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMI (58-157)

atpa_hs: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         |||||||||||||||||||  ||| ||||              ||||||||| ||    |  |    |   |||| ||||  | ||||||| || |||||
atpa_ec: PIGRGQRELIIGDRQTGKTALAIDAIINQR--------DSGIKCIYVAIGQKASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYF (158-249)

atpa_hs: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMN----DAFGGG-------SLTALPVIETQAGDVSAYIPTNVISIT (301-389)
         || |  ||||||||||||||||| |||||||||||| ||||||||||||||||  |     ||  |       |||||| ||||||||||  ||||||||
atpa_ec: RDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLERAARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISIT (250-349)

atpa_hs: DGQIFLETELFYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIY (390-489)
         |||||||| ||  ||||| | | |||||| ||||  ||   |     |||||| ||| || |||| ||   |  |   |||||| || ||    |  |
atpa_ec: DGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQYRELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLF (350-449)

atpa_hs: AGVRGYLDKLEPSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLKEIVTNFLAGFEA                                     (490-553)
         |  ||||   | |||  || | |  |   |  |   |   |        ||| |   | |
atpa_ec: AAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYNDEIEGKLKGILDSFKATQSW                                     (450-513)

c) Like the result of the linear penalty global aligner, the alignment is much worse at the beginning compared to the
middle and the end, and there are still a lot of matches (high degree of similarity) after the beginning of the
sequence). The affine alignment actually has a higher optimal score than the linear gap penalty alignment. This makes sense
because the gap penalty is 2 whereas it was 8 in the linear gap penalty. This observation also goes hand in hand with
the next. Considering a chain of consecutive gaps as a gap block, there are many less gap blocks in the affine alignment
(4 gap blocks) compared to the linear penalty, which also has many individual gaps. This makes sense because starting a
new gap block has the added cost of the affine gap penalty (12), so the affine alignment is very unlikely to have very
short gap blocks and likely to have less gap blocks. Adding on to the first observation, since there are not many gap
blocks, the affine penalty is not paid as often, so even though it is higher than the linear gap penalty in the first
alignment, the average gap penalty (considering both affine and added gap penalties) is less in the affine alignment
leading to the higher optimal score. Both aligners indicate that there is more variation between the two sequences at
the beginning, and changing the algorithm changes how these differences manifest. The affine aligner may be a more
accurate representation of the real alignment as in nature, it is more likely to have one insertion or deletion chunk
that leads to the gain or loss of a number of nucleotides than have the same number of nucleotides inserted or deleted
as individuals or in small groups, as each insertion or deletion requires breaking the DNA. Therefore, looking at the
results of the affine aligner, a large proportion of the variance between ATP synthase in E. coli and humans could be
due to a large insertion into the human ATP synthase or deletion in the bacterial ATP synthase near the beginning of the
sequence.


d) Yes, it will always return the same score for an optimal alignment as global_aligner_plus.py because if h = 0, there
is no affine penalty, meaning there is no extra cost to start a new block of gaps. It is functionally the same as a
linear gap penalty of 3 since the first and every other gap has a penalty of 3.
Another way to get to this conclusion is by looking at the equations used to calculate each cell's value. In the
original global aligner with the linear gap penalty, the value of any cell that is not a base case is max((s(Xi, Yj) + V
(i-1, j-1)), (-g + V(i-1, j)), (-g + V(i,j-1))), where V is the dp table and i and j are the current indices of sequence
x and y respectively.  With the affine algorithm, we add a dimension to the table, so we have 3 separate tables for each
type of column, but to calculate the value of each cell, we look at the same relative locations (type 1 --> i-1, j-1,
type 2 --> i-1, j, type 3 --> i, j-1) and add the affine gap penalties to the dp tables for type 2 and type 3 columsn
when necessary. However, when the affine penalty (h) is 0, the equations we use to calculate the values for each table
can be simplified. D is the table for type 1 columns, E is the table for type 2, and F is the table for type 3, and
sequence X is written along the rows of each table while sequence Y is written on the columns.
D(i,j) = s(Xi,Yj) + max (D(i-1,j-1), E(i-1,j), F(i, j-1)) We can see that the calculation for a type 1 column is already
the same as in the linear gap penalty algorithm, as it is not affected by the affine penalty. In the linear algorithm,
V(i-1, j-1) is the max value of that cell from D,E,F assuming the calculations for E and F are the same as the linear
algorithm. Now, I will discuss why that is true.
E(i,j) = -g + max(D(i-1,j) - 0, E(i-1,j), F(i-1,j) - 0) = -g + max(D(i-1,j), E(i-1,j), F(i-1,j)). When the affine gap
penalty is 0, we see that for type 2 columns, the calculation is also the same as the linear algorithm (-g + V(i-1,j))
because again, V(i-1,j) would store max(D(i-1,j), E(i-1,j), F(i-1,j)).
F(i,j) = -g + max(D(i,j-1) - 0, E(i,j-1) - 0, F(i,j-1)) = -g + max(D(i,j-1), E(i,j-1), F(i,j-1)). Using the same logic
as with table E, we see that type 3 columns also have the same calculations as the linear algorithm.
Finally, the base cases are initialized to the same value, as in affine algorithm, column 0 in table E has values -h -
gi for i>0 and the linear algorithm has -gi for i>0. Row 0 in table F is -h - gj for j>0, and the linear algorithm
is -gj for j>0, so the base cases have the same value when h = 0.
Overall, an affine algorithm with h = 0 would just delay finding the max value for each cell. Even though it stores
values for type 1,2, and 3 columns for each location, only the max value from the 3 tables at a given location is used
to calculate a new cells value. This is the same as in the linear algorithm, which just stores the max directly in the
location because it is 2-d.


e) For the linear gap aligner, the time complexity is ϴ(mn) using dynamic programming because the dp table has m+1 rows
for the m characters in sequence 1 and n+1 columns for the n characters in sequence 2, making it have ϴ(mn) cells to
fill. Filling each cell only requires 3 lookups on lists and arithmetic, which in total is ϴ(1) time, so the total time
to fill the table is ϴ(mn). For the affine gap aligner, the dynamic table becomes 3d or can be represented as 3 2d
tables that mirror the one in the linear gap aligner. To fill each cell still only requires constant time operations
(and still only 3 lookups because now we are looking up a certain cell location in 3 tables rather than 3 separate
locations). Therefore, the time complexity of the affine algorithm is just ϴ(3mn) = ϴ(mn), so the linear and affine
algorithms have the same asymptotic time complexity. However, the affine algorithm will take longer in terms of real
time because of the added tables (around 3 times more time) because the procedure is mirrored but just conducted on 3
separate tables, and the traceback time (which is not factored into the asymptotic runtime) is the same because the
traceback will still only visit one table per step. I predict the asymptotic space complexity will be the same because
as with time, the affine gap algorithm stores 3 versions of the dp table, and each dp table is essentially the same as
the dp table in the linear algorithm. Both algorithms will have a space complexity of ϴ(mn) Furthermore, even though the
pointers are different because they store tables rather than which direction the previous cell is in, they do not take
up any more space because in both algorithms, the pointers are designed to be one integer. Therefore, the coefficient 3
is not factored into the asymptotic space complexity and the space just varies linearly with mn. However, the actual
space used is also higher in the affine algorithm due to the added dimension of the dp table (triple the space because
the new dimension is 3 units).