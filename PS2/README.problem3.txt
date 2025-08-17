COMPSCI 260 - Problem Set 2, Problem 3
Due: Fri 9 Feb 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 

My solutions and comments for this problem are below.
-----------------------------------------------------
a) In a single row, we just need to account for the fact that no two pebbles lie on horizontally adjacent squares.
Therefore, if a row has x spots, there can be a max of x/2 pebbles in that row. There are 4 columns in this board, so a
single row can be thought of as a 1x4 array with 0-2 pebbles, where P indicates a pebble is in a given position, and 0
indicates an empty position. Assuming all pebbles are the same, the possible valid placements are as follows:
    0. 0 0 0 0
    1. P 0 0 0
    2. 0 P 0 0
    3. 0 0 P 0
    4. 0 0 0 P
    5. P 0 0 P
    6. P 0 P 0
    7. 0 P 0 P

b) The pattern types would be the 8 row patterns enumerated above, and we can see that only certain combinations of
pattern types are compatible, and the set of compatible patterns for a given pattern are as follows:
0: {1,2,3,4,5,6,7}
1: {0,2,3,4,7}
2: {0,1,3,4,5,6}
3: {0,1,2,4,5,7}
4: {0,1,2,3,6}
5: {0,2.3}
6: {0,2,4,7}
7: {0,1,3,6}
We can solve this problem by storing the maximum value up to a given row for each pattern type of the last row. This can
be visualized as an nx8 table, with each row in the table corresponding to the subproblem with the grid up to that row,
and each column corresponding to a pattern type. For each row, we find the maximum value by ending pattern type by
looking at the previous row and considering all the columns with compatible pattern types. THen we add the values for
the given pattern type in the last row. This runs in O(n) time because it only iterates through each of the n rows a
constant number of times and just has to look up a constant number of values from the previous row. Then, at the end, we
can just take the maximum value from the nth row to give the max value of a valid placement of pebbles

c) refer to code

d) The max score for this grid is 10710.

e) 10000	0	    100000	0
   1	    1	    1	    1
   0	    10000	0	    100000
   In this example grid, the optimal solution has no pebbles in the second row from the top. This is because the row
   above and the row below have very high value squares that do not share any compatible pattern types, so it is not
   worth it to place a pebble for only 1 and sacrifice 1000. In general, any combination of two high value rows with no
   shared compatible row in between them will lead to an optimal solution with an empty row.