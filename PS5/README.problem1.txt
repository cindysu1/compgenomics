COMPSCI 260 - Problem Set 5, Problem 1
Due: Fri 29 Mar 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 

My solutions and comments for this problem are below.
-----------------------------------------------------
a)
Name      Gene expression profile     Class when k = 1    Class when k = 3
Alice           (2, 3)                      o                    o
Bobby           (6, 10)                    +/o                   o
Cindy           (8, 10)                     +                    +
Donny           (4, 7)                      +                    o
Ellen           (8, 7)                      o                    o

For Alice, I am pretty confident in the prognosis because both cases indicate she is a non-responder and looking at the
location of her expression, the closest 3 neighbors are non-responders that are pretty closely clustered around her
expression profile, and the nearest responder sample is significantly further. For Bobby, when we look at the case
k=1, there is uncertainty due to a tie between two samples for the closest neighbor, and one sample is a responder and
the other is not. Therefore, this is ambiguity because we do not have any method of choosing one or the other, so even
though an odd k prevents ties from the majority vote, it does not prevent ties based on distance initially.
When k=3 for Bobby, there are 2 non-responder samples and 1 responder sample, but all the samples are quite far from his
expression profile, so I am not as confident. For Cindy, the closest neighbor is clearly a responder, and the next
closest neighbors are much further away. When k=3, the two closest samples are responders while the 3rd closest neighbor
is a non-responder that is much further from Cindy's expression profile than the two responders, so I am more confident
that Cindy is a responder compared to the conclusion about Bobby. In Donny's case, when k=1, his class is a responder,
but when k=3, the next two closest neighbors are non-responders that are just slightly further from his expression
profile than the closest responder sample. Therefore, I am not confident in my prognosis because it is hard to determine
if the one closest sample is more important or if the two slightly further ones are (quantity vs. distance). Also, the
k=1 class does not seem to consider enough data to provide a confident prognosis. Finally, Ellen's expression profile is
closest to a non-responder, but the next nearest neighbor is a responder and a very similar distance away. The third
closest neighbor is much further and a non-responder, so Ellen's class is non-responder in both cases, but again, the
I am not sure due to the close proximity of the closest responder and non-responder samples and the significance
distance to the third closest sample. Overall, I am not that confident in these prognoses because the cases with k=1
just do not seem to have enough data to make an accurate conclusion, and even when k=3, the majority vote is usually 2-1
with variable distances that do not confer confidence.

b) look at code

c) The prognosis class for the new patients when k=5 is as follows:
Patient 1: R
Patient 2: N
Patient 3: R
Patient 4: N
Patient 5: R
Patient 6: R
Patient 7: N
Patient 8: N
Patient 9: R
Patient 10: R


