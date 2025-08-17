COMPSCI 260 - Problem Set 4, Problem 2
Due: Fri 8 Mar 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):

My solutions and comments for this problem are below.
-----------------------------------------------------
c)
The optimal score for the alignment of atpa_hs and atpa_ec is 1015
The top most alignment is
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |                  |          ||   |   |        |      |    |  |         | |  ||  | |||      ||
atpa_ec: M-QLN-STEI--S--E---LIKQR------IA-Q-F---NV-VSE---AH-N---E----G--T-I-------V-SVSDGVIRIHGLADCMQGEMISLPG (1-57)

atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
               |||| | || || |      ||  || || |  ||||  ||||||  ||  ||||||        |   ||| | | ||  | ||| |||||
atpa_ec: NRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVGRGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMI (58-157)

atpa_hs: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         |||||||||||||||||||  ||| |||| |  | |  |    ||||||||| ||    |  |    |   |||| ||||  | ||||||| || |||||
atpa_ec: PIGRGQRELIIGDRQTGKTALAIDAIINQ-R--D-SGIK----CIYVAIGQKASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYF (158-249)

atpa_hs: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMN----DAF--G---G--GSLTALPVIETQAGDVSAYIPTNVISIT (301-389)
         || |  ||||||||||||||||| |||||||||||| ||||||||||||||||  |     ||  |   |  ||||||| ||||||||||  ||||||||
atpa_ec: RDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLERAARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISIT (250-349)

atpa_hs: DGQIFLETELFYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIY (390-489)
         |||||||| ||  ||||| | | |||||| ||||  ||   |     |||||| ||| || |||| ||   |  |   |||||| || ||    |  |
atpa_ec: DGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQYRELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLF (350-449)

atpa_hs: AGVRGYLDKLEPSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLKEIVTNFLAGFEA                                     (490-553)
         |  ||||   | |||  || | |  |   |  |   |   |        ||| |   | |
atpa_ec: AAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYNDEIEGKLKGILDSFKATQSW                                     (450-513)

The bottom most alignment is
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |                  |          | |  |   |         |      |   |  |         | |  ||  | |||      ||
atpa_ec: M-QLN-STE-I-S---E--LI-K----QR-I-AQ-F---N--V----VSE-AH--NE---G--T-I-------V-SVSDGVIRIHGLADCMQGEMISLPG (1-57)

atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
               |||| | || || |      ||  || || |  ||||  ||||||  ||  ||||||        |   ||| | | ||  | ||| |||||
atpa_ec: NRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVGRGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMI (58-157)

atpa_hs: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         |||||||||||||||||||  ||| |||| |  | |    |  ||||||||| ||    |  |    |   |||| ||||  | ||||||| || |||||
atpa_ec: PIGRGQRELIIGDRQTGKTALAIDAIINQ-R--D-SG--IK--CIYVAIGQKASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYF (158-249)

atpa_hs: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMN-D---AF--G---G--GSLTALPVIETQAGDVSAYIPTNVISIT (301-389)
         || |  ||||||||||||||||| |||||||||||| ||||||||||||||||  |     ||  |   |  ||||||| ||||||||||  ||||||||
atpa_ec: RDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLERAARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISIT (250-349)

atpa_hs: DGQIFLETELFYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIY (390-489)
         |||||||| ||  ||||| | | |||||| ||||  ||   |     |||||| ||| || |||| ||   |  |   |||||| || ||    |  |
atpa_ec: DGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQYRELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLF (350-449)

atpa_hs: AGVRGYLDKLEPSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLKEIVTNFLAGFEA                                     (490-553)
         |  ||||   | |||  || | |  |   |  |   |   |        ||| |   | |
atpa_ec: AAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYNDEIEGKLKGILDSFKATQSW                                     (450-513)



d) Both the proteins are ATP synthases, but the first is found in humans while the second is found in E. coli. However,
since they are both ATP synthases, they have similar functions (producing ATP from ADP in the presence of a proton
gradient). Furthermore, given how important ATP production is as an energy source to all living organisms, the amino
acid sequence of ATP synthases is likely less subject to evolutionary change and is conserved across species as
mutations could potentially disrupt ATP synthesis and have an extremely detrimental effect. Looking at the optimal score
and the alignments themselves, we can see there is a high degree of similarity. The segment of the sequence in the
middle (~110-480) has the most matches, while the beginning end have a more significant number of mismatches and gaps
(especially the beginning). The large regions of consecutive matches may indicate those regions are  more evolutionarily
conserved to preserve the shared function, while other more dissimilar regions may account for the other differences
between the human and bacterial environment or differences in the specific functions of ATP synthase in each organism,
as bacteria and humans have some differences in terms of metabolism and cellular respiration which both use and produce
ATP. Also, there are not many gaps in the sequences, probably due to the high gap penalty compared to the values of the
 mismatches.

1. https://www.uniprot.org/uniprotkb/P25705/entry
2. https://www.uniprot.org/uniprotkb/P0ABB0/entry

e) Given these are also ATP synthases in other organisms, we expect a high level of similarity at least in certain
regions of the sequence that show the shared function of synthesizing ATP and the evolutionary pressure to conserve the
function and sequence. Since the proteins are found in different organisms, there may be regions with more mismatches
and gaps like between human and E. coli in regions that may be turns or loops connecting the functional parts of the
protein or just insertions or deletions that do not significantly impact the ATP synthases ability to synthesize ATP. I
think the mouse ATP synthase will be more similar to the human because they are both mammals and mice are often used as
an animal model due to most of the genes in mice having a counterpart in humans and they are far more similar than a
human is to bacteria. Likewise, E. coli and B. subtilis are both bacteria, so they are probably more divergent from
mammals and more similar to each other.

f)
The optimal score for the alignment of atpa_mm and atpa_hs is 2689
The optimal alignment is unique and it is
atpa_mm: MLSVRVAAAVARALPRRAGLVSKNALGSSFVGARNLHASNTRLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |||||||||| ||||||||||| |||||||  ||| ||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)

atpa_mm: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDVVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
         ||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)

atpa_mm: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         ||||||||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
atpa_hs: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)

atpa_mm: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDSFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETELF (301-400)
         ||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ||||||||||||||||||||||||||||||||||||||||||
atpa_hs: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDAFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETELF (301-400)

atpa_mm: YKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKLE (401-500)
         ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
atpa_hs: YKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKLE (401-500)

atpa_mm: PSKITKFENAFLSHVISQHQSLLGNIRSDGKISEQSDAKLKEIVTNFLAGFEP                                                (501-553)
         ||||||||||||||| |||| ||| || ||||||||||||||||||||||||
atpa_hs: PSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLKEIVTNFLAGFEA                                                (501-553)

The optimal score for the alignment of atpa_mm and atpa_ec is 1016
The top most alignment is
atpa_mm: MLSVRVAAAVARALPRRAGLVSKNALGSSFVGARNLHASNTRLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |            |        |      |    |   |         |      |    |  |         | |  ||  | |||      ||
atpa_ec: M-QLN-STEISE-L------I-KQRI-AQF----NV-VS----E----AH-N---E----G--T-I-------V-SVSDGVIRIHGLADCMQGEMISLPG (1-57)

atpa_mm: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDVVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
               |||| | || || |      ||  || || |  ||||  ||||||  ||  ||||||        |   ||| | | ||  | ||| |||||
atpa_ec: NRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVGRGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMI (58-157)

atpa_mm: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         |||||||||||||||||||  ||| |||| |   |   |    ||||||||| ||    |  |    |   |||| ||||  | ||||||| || |||||
atpa_ec: PIGRGQRELIIGDRQTGKTALAIDAIINQ-R-DSGI--K----CIYVAIGQKASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYF (158-249)

atpa_mm: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMN----DSF--G---G--GSLTALPVIETQAGDVSAYIPTNVISIT (301-389)
         || |  ||||||||||||||||| |||||||||||| ||||||||||||||||  |      |  |   |  ||||||| ||||||||||  ||||||||
atpa_ec: RDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLERAARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISIT (250-349)

atpa_mm: DGQIFLETELFYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIY (390-489)
         |||||||| ||  ||||| | | |||||| ||||  ||   |     |||||| ||| || |||| ||   |  |   |||||| || ||    |  |
atpa_ec: DGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQYRELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLF (350-449)

atpa_mm: AGVRGYLDKLEPSKITKFENAFLSHVISQHQSLLGNIRSDGKISEQSDAKLKEIVTNFLAGFEP                                     (490-553)
         |  ||||   | |||  || | |  |   |  |   |   |        ||| |   | |
atpa_ec: AAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYNDEIEGKLKGILDSFKATQSW                                     (450-513)

The bottom most alignment is
atpa_mm: MLSVRVAAAVARALPRRAGLVSKNALGSSFVGARNLHASNTRLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         |                  |  |      |    |   |         |       |   |  |         | |  ||  | |||      ||
atpa_ec: M-QLN-STEI--S---E--LI-KQRI-AQF----NV-VS----E----AH--N---E---G--T-I-------V-SVSDGVIRIHGLADCMQGEMISLPG (1-57)

atpa_mm: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDVVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSLV (101-200)
               |||| | || || |      ||  || || |  ||||  ||||||  ||  ||||||        |   ||| | | ||  | ||| |||||
atpa_ec: NRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVGRGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMI (58-157)

atpa_mm: PIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYF (201-300)
         |||||||||||||||||||  ||| |||| |   |     |  ||||||||| ||    |  |    |   |||| ||||  | ||||||| || |||||
atpa_ec: PIGRGQRELIIGDRQTGKTALAIDAIINQ-R-DSGI----K--CIYVAIGQKASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYF (158-249)

atpa_mm: RDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMN-D---SF--G---G--GSLTALPVIETQAGDVSAYIPTNVISIT (301-389)
         || |  ||||||||||||||||| |||||||||||| ||||||||||||||||  |      |  |   |  ||||||| ||||||||||  ||||||||
atpa_ec: RDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLERAARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISIT (250-349)

atpa_mm: DGQIFLETELFYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIY (390-489)
         |||||||| ||  ||||| | | |||||| ||||  ||   |     |||||| ||| || |||| ||   |  |   |||||| || ||    |  |
atpa_ec: DGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQYRELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLF (350-449)

atpa_mm: AGVRGYLDKLEPSKITKFENAFLSHVISQHQSLLGNIRSDGKISEQSDAKLKEIVTNFLAGFEP                                     (490-553)
         |  ||||   | |||  || | |  |   |  |   |   |        ||| |   | |
atpa_ec: AAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYNDEIEGKLKGILDSFKATQSW                                     (450-513)

The optimal score for the alignment of atpa_bs and atpa_hs is 1137
The top most alignment is
atpa_bs: M-SIK-AEE-I-S----T-LI-K----QQ-I--QNYQ-SD--I------E---V-QD-V-G--T-V-I-Q---V---GDGIARVHGLDNCMAGELVEFSN (1-57)
         | |   |            |          |   |   |          |          |  | |       |   |||||||||| |  | | ||||
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)

atpa_bs: GVLGMAQNLEESNVGIVILGPFSEIREGDEVKRTGRIMEVPVGEELIGRIVNPLGQPVDGLGPILTSKT-RPIESPAPGVMDRKSVHEPLQTGIKAIDAL (58-156)
         |  ||  |||  ||| |  |    | ||| ||||| |  ||||||| || |  ||   || |||  ||| |     |||   | || || |||||| | |
atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPI-GSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSL (101-199)

atpa_bs: IPIGRGQRELIIGDRQTGKTSVAIDAILNQK---D-QD----MICVYVAIGQKESTVRGVVETLRKHGALDYTIVVTASASQPAPLLYLAPYAGVTMAEE (157-248)
          |||||||||||||||||||| ||| | |||   |  |      | ||||||| |||   |  |    |  ||||| | ||  ||| ||||| |  | |
atpa_hs: VPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEY (200-299)

atpa_bs: FMYNGKHVLVVYDDLSKQAAAYRELSLLLRRPPGREAFPGDVFYLHSRLLERAAKLSDAKGAGSITALPFVETQAGDISAYIPTNVISITDGQIFLQSDL (249-348)
         |  |||| |  |||||||| |||  |||||||||||| |||||||||||||||||  || | || ||||  |||||| ||||||||||||||||||   |
atpa_hs: FRDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDAFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETEL (300-399)

atpa_bs: FFSGVRPAINAGLSVSRVGGSAQIKAMKKVSGTLRLDLASYRELEAFAQFGSDLDQATQAKLNRGARTVEVLKQDLNKPLPVEKQVAILYALTKGYLDDI (349-448)
         |  | ||||| ||||||||  ||  ||| | ||  | || |||  |||||||||| |||  | || |  | |||    |   | |||  ||   ||||
atpa_hs: FYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKL (400-499)

atpa_bs: PVADIRRFEEEYYMYLDQNHKDLLDGIAKTGNLPADEDFKAAIEGFKRTFAP-SN                                              (449-502)
             |  ||          |  ||  |   |      | |   |      |
atpa_hs: EPSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLK-EIVTNFLAGFEA                                              (500-553)

The bottom most alignment is
atpa_bs: M-SIK-AEEI--S----T-LI-KQ---Q--I--QNYQ-SD--I------E---V-QD-V-G--T-V-IQ----V---GDGIARVHGLDNCMAGELVEFSN (1-57)
         | |   |            |          |   |   |          |          |  | |       |   |||||||||| |  | | ||||
atpa_hs: MLSVRVAAAVVRALPRRAGLVSRNALGSSFIAARNFHASNTHLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)

atpa_bs: GVLGMAQNLEESNVGIVILGPFSEIREGDEVKRTGRIMEVPVGEELIGRIVNPLGQPVDGLGPILTSKTRP-IESPAPGVMDRKSVHEPLQTGIKAIDAL (58-156)
         |  ||  |||  ||| |  |    | ||| ||||| |  ||||||| || |  ||   || |||  ||||      |||   | || || |||||| | |
atpa_hs: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPI-GSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSL (101-199)

atpa_bs: IPIGRGQRELIIGDRQTGKTSVAIDAILNQK---D-QD-M--I-CVYVAIGQKESTVRGVVETLRKHGALDYTIVVTASASQPAPLLYLAPYAGVTMAEE (157-248)
          |||||||||||||||||||| ||| | |||   |  |      | ||||||| |||   |  |    |  ||||| | ||  ||| ||||| |  | |
atpa_hs: VPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGSDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEY (200-299)

atpa_bs: FMYNGKHVLVVYDDLSKQAAAYRELSLLLRRPPGREAFPGDVFYLHSRLLERAAKLSDAKGAGSITALPFVETQAGDISAYIPTNVISITDGQIFLQSDL (249-348)
         |  |||| |  |||||||| |||  |||||||||||| |||||||||||||||||  || | || ||||  |||||| ||||||||||||||||||   |
atpa_hs: FRDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDAFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETEL (300-399)

atpa_bs: FFSGVRPAINAGLSVSRVGGSAQIKAMKKVSGTLRLDLASYRELEAFAQFGSDLDQATQAKLNRGARTVEVLKQDLNKPLPVEKQVAILYALTKGYLDDI (349-448)
         |  | ||||| ||||||||  ||  ||| | ||  | || |||  |||||||||| |||  | || |  | |||    |   | |||  ||   ||||
atpa_hs: FYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKL (400-499)

atpa_bs: PVADIRRFEEEYYMYLDQNHKDLLDGIAKTGNLPADEDFKAAIEGFKRTFAPSN-                                              (449-502)
             |  ||          |  ||  |   |      | |   |      |
atpa_hs: EPSKITKFENAFLSHVVSQHQALLGTIRADGKISEQSDAKLK-EIVTNFLAGFEA                                              (500-553)

The optimal score for the alignment of atpa_bs and atpa_ec is 1344
The top most alignment is
atpa_bs: MSIKAEEISTLIKQQIQNYQSDIEVQDVGTVIQVGDGIARVHGLDNCMAGELVEFSNGVLGMAQNLEESNVGIVILGPFSEIREGDEVKRTGRIMEVPVG (1-100)
         |     ||| |||| |       |    ||   | ||  | |||  || ||           | |||   || |  ||     ||  || |||| |||||
atpa_ec: MQLNSTEISELIKQRIAQFNVVSEAHNEGTIVSVSDGVIRIHGLADCMQGEMISLPGNRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVG (1-100)

atpa_bs: EELIGRIVNPLGQPVDGLGPILTSKTRPIESPAPGVMDRKSVHEPLQTGIKAIDALIPIGRGQRELIIGDRQTGKTSVAIDAILNQKDQDMICVYVAIGQ (101-200)
           | || || || | || ||         |  ||||  | ||  | ||| || |  ||||||||||||||||||||  ||||| || |    | ||||||
atpa_ec: RGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMIPIGRGQRELIIGDRQTGKTALAIDAIINQRDSGIKCIYVAIGQ (101-200)

atpa_bs: KESTVRGVVETLRKHGALDYTIVVTASASQPAPLLYLAPYAGVTMAEEFMYNGKHVLVVYDDLSKQAAAYRELSLLLRRPPGREAFPGDVFYLHSRLLER (201-300)
         | ||   ||  |  ||||  |||| | ||  | | |||||||  | | |   |   |  |||||||| |||  |||||||||||||||||||||||||||
atpa_ec: KASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYFRDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLER (201-300)

atpa_bs: AAKL-S---DA------KG-AGSITALPFVETQAGDISAYIPTNVISITDGQIFLQSDLFFSGVRPAINAGLSVSRVGGSAQIKAMKKVSGTLRLDLASY (301-389)
         ||        |      ||  || ||||  |||||| ||  ||||||||||||||   ||  | ||| | | ||||||| || | ||| ||  |  || |
atpa_ec: AARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISITDGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQY (301-400)

atpa_bs: RELEAFAQFGSDLDQATQAKLNRGARTVEVLKQDLNKPLPVEKQVAILYALTKGYLDDIPVADIRRFEEEYYMYLDQNHKDLLDGIAKTGNLPADEDFKA (390-489)
         ||| || || |||| ||   |  |    | |||    |  |  |   | |   ||| |     |  ||     | |  |  |   |  ||    ||
atpa_ec: RELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLFAAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGYN-DE-IEG (401-498)

atpa_bs: AIEGFKRTF-APSN-                                                                                      (490-502)
            |    | |
atpa_ec: KLKGILDSFKATQSW                                                                                      (499-513)

The bottom most alignment is
atpa_bs: MSIKAEEISTLIKQQIQNYQSDIEVQDVGTVIQVGDGIARVHGLDNCMAGELVEFSNGVLGMAQNLEESNVGIVILGPFSEIREGDEVKRTGRIMEVPVG (1-100)
         |     ||| |||| |       |    ||   | ||  | |||  || ||           | |||   || |  ||     ||  || |||| |||||
atpa_ec: MQLNSTEISELIKQRIAQFNVVSEAHNEGTIVSVSDGVIRIHGLADCMQGEMISLPGNRYAIALNLERDSVGAVVMGPYADLAEGMKVKCTGRILEVPVG (1-100)

atpa_bs: EELIGRIVNPLGQPVDGLGPILTSKTRPIESPAPGVMDRKSVHEPLQTGIKAIDALIPIGRGQRELIIGDRQTGKTSVAIDAILNQKDQDMICVYVAIGQ (101-200)
           | || || || | || ||         |  ||||  | ||  | ||| || |  ||||||||||||||||||||  ||||| || |    | ||||||
atpa_ec: RGLLGRVVNTLGAPIDGKGPLDHDGFSAVEAIAPGVIERQSVDQPVQTGYKAVDSMIPIGRGQRELIIGDRQTGKTALAIDAIINQRDSGIKCIYVAIGQ (101-200)

atpa_bs: KESTVRGVVETLRKHGALDYTIVVTASASQPAPLLYLAPYAGVTMAEEFMYNGKHVLVVYDDLSKQAAAYRELSLLLRRPPGREAFPGDVFYLHSRLLER (201-300)
         | ||   ||  |  ||||  |||| | ||  | | |||||||  | | |   |   |  |||||||| |||  |||||||||||||||||||||||||||
atpa_ec: KASTISNVVRKLEEHGALANTIVVVATASESAALQYLAPYAGCAMGEYFRDRGEDALIIYDDLSKQAVAYRQISLLLRRPPGREAFPGDVFYLHSRLLER (201-300)

atpa_bs: AAKLS-D---A--KG-A-G---SITALPFVETQAGDISAYIPTNVISITDGQIFLQSDLFFSGVRPAINAGLSVSRVGGSAQIKAMKKVSGTLRLDLASY (301-389)
         ||        |  ||   |   | ||||  |||||| ||  ||||||||||||||   ||  | ||| | | ||||||| || | ||| ||  |  || |
atpa_ec: AARVNAEYVEAFTKGEVKGKTGSLTALPIIETQAGDVSAFVPTNVISITDGQIFLETNLFNAGIRPAVNPGISVSRVGGAAQTKIMKKLSGGIRTALAQY (301-400)

atpa_bs: RELEAFAQFGSDLDQATQAKLNRGARTVEVLKQDLNKPLPVEKQVAILYALTKGYLDDIPVADIRRFEEEYYMYLDQNHKDLLDGIAKTGNLPADEDFKA (390-489)
         ||| || || |||| ||   |  |    | |||    |  |  |   | |   ||| |     |  ||     | |  |  |   |  ||    ||
atpa_ec: RELAAFSQFASDLDDATRKQLDHGQKVTELLKQKQYAPMSVAQQSLVLFAAERGYLADVELSKIGSFEAALLAYVDRDHAPLMQEINQTGGY-NDE-IEG (401-498)

atpa_bs: AIEGFKRTF-APSN-                                                                                      (490-502)
            |    | |
atpa_ec: KLKGILDSFKATQSW                                                                                      (499-513)

The optimal score for the alignment of atpa_mm and atpa_bs is 1143
The top most alignment is
atpa_mm: MLSVRVAAAVARALPRRAGLVSKNALGSSFVGARNLHASNTRLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         | |   |      |        |           |   |          |          |  | |       |   |||||||||| |  | | ||||
atpa_bs: M-SIK-AEEIS-TL------I-KQ---Q--I--QN-YQSD--I------E---V-QD-V-G--T-V-IQ----V---GDGIARVHGLDNCMAGELVEFSN (1-57)

atpa_mm: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDVVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPI-GSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSL (101-199)
         |  ||  |||  ||| |  |    | ||| ||||| |  ||||||| || |  ||   || |||  ||||      |||   | || || |||||| | |
atpa_bs: GVLGMAQNLEESNVGIVILGPFSEIREGDEVKRTGRIMEVPVGEELIGRIVNPLGQPVDGLGPILTSKTRP-IESPAPGVMDRKSVHEPLQTGIKAIDAL (58-156)

atpa_mm: VPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEY (200-299)
          |||||||||||||||||||| ||| | |||   |  |      | ||||||| |||   |  |    |  ||||| | ||  ||| ||||| |  | |
atpa_bs: IPIGRGQRELIIGDRQTGKTSVAIDAILNQK---D-QD-M--I-CVYVAIGQKESTVRGVVETLRKHGALDYTIVVTASASQPAPLLYLAPYAGVTMAEE (157-248)

atpa_mm: FRDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDSFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETEL (300-399)
         |  |||| |  |||||||| |||  |||||||||||| |||||||||||||||||  |  | || ||||  |||||| ||||||||||||||||||   |
atpa_bs: FMYNGKHVLVVYDDLSKQAAAYRELSLLLRRPPGREAFPGDVFYLHSRLLERAAKLSDAKGAGSITALPFVETQAGDISAYIPTNVISITDGQIFLQSDL (249-348)

atpa_mm: FYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKL (400-499)
         |  | ||||| ||||||||  ||  ||| | ||  | || |||  |||||||||| |||  | || |  | |||    |   | |||  ||   ||||
atpa_bs: FFSGVRPAINAGLSVSRVGGSAQIKAMKKVSGTLRLDLASYRELEAFAQFGSDLDQATQAKLNRGARTVEVLKQDLNKPLPVEKQVAILYALTKGYLDDI (349-448)

atpa_mm: EPSKITKFENAFLSHVISQHQSLLGNIRSDGKISEQSDAKLKEIVTNFLAGFEP--                                             (500-553)
             |  ||          |  ||  |   |      |   |     |   | |
atpa_bs: PVADIRRFEEEYYMYLDQNHKDLLDGIAKTGNLPADED--FKAAIEGFKRTFAPSN                                             (449-502)

The bottom most alignment is
atpa_mm: MLSVRVAAAVARALPRRAGLVSKNALGSSFVGARNLHASNTRLQKTGTAEMSSILEERILGADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSS (1-100)
         | |   |            |  |           |        |       | |  |     |  |     | |   |||||||||| |  | | ||||
atpa_bs: M-SIK-AEEI--S----T-LI-K----QQ-I--QN-Y------Q-------SDI--E-V--QD--V-----GTVIQVGDGIARVHGLDNCMAGELVEFSN (1-57)

atpa_mm: GLKGMSLNLEPDNVGVVVFGNDKLIKEGDVVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPI-GSKTRRRVGLKAPGIIPRISVREPMQTGIKAVDSL (101-199)
         |  ||  |||  ||| |  |    | ||| ||||| |  ||||||| || |  ||   || |||  ||| |     |||   | || || |||||| | |
atpa_bs: GVLGMAQNLEESNVGIVILGPFSEIREGDEVKRTGRIMEVPVGEELIGRIVNPLGQPVDGLGPILTSKT-RPIESPAPGVMDRKSVHEPLQTGIKAIDAL (58-156)

atpa_mm: VPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEY (200-299)
          |||||||||||||||||||| ||| | |||   |  |      | ||||||| |||   |  |    |  ||||| | ||  ||| ||||| |  | |
atpa_bs: IPIGRGQRELIIGDRQTGKTSVAIDAILNQK---D-QD----MICVYVAIGQKESTVRGVVETLRKHGALDYTIVVTASASQPAPLLYLAPYAGVTMAEE (157-248)

atpa_mm: FRDNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDSFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETEL (300-399)
         |  |||| |  |||||||| |||  |||||||||||| |||||||||||||||||  |  | || ||||  |||||| ||||||||||||||||||   |
atpa_bs: FMYNGKHVLVVYDDLSKQAAAYRELSLLLRRPPGREAFPGDVFYLHSRLLERAAKLSDAKGAGSITALPFVETQAGDISAYIPTNVISITDGQIFLQSDL (249-348)

atpa_mm: FYKGIRPAINVGLSVSRVGSAAQTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKL (400-499)
         |  | ||||| ||||||||  ||  ||| | ||  | || |||  |||||||||| |||  | || |  | |||    |   | |||  ||   ||||
atpa_bs: FFSGVRPAINAGLSVSRVGGSAQIKAMKKVSGTLRLDLASYRELEAFAQFGSDLDQATQAKLNRGARTVEVLKQDLNKPLPVEKQVAILYALTKGYLDDI (349-448)

atpa_mm: EPSKITKFENAFLSHVISQHQSLLGNIRSDGKISEQSDAKLKEIVTNFLAGFEP--                                             (500-553)
             |  ||          |  ||  |   |      |   |     |   | |
atpa_bs: PVADIRRFEEEYYMYLDQNHKDLLDGIAKTGNL--PADEDFKAAIEGFKRTFAPSN                                             (449-502)

g) The optimal score for all the alignments are around the same as the alignment between atpa_hs and atpa_ec which
makes sense because they are all have similar functions. However, atpa_mm and atpa_hs create an outlying alignment with
a score of 2689, and there are actually only 13 mismatches and no gaps. Looking at the fasta file, I see that atpa_mm
is a mouse ATP synthase unit, and it is almost identical to the human ATP synthase. It is also the only one with a
unique optimal alignment. The optimal score of alignments between atpa_mm & atpa_bs, atpa_mm & atpa_ec, and atpa_hs &
atpa_bs are very similar to the optimal score of the alignment between atpa_hs & atpa_ec, which makes sense because E.
coli and B. subtilis are both bacteria which may have a similar level of divergence from human ATP synthase. Since the
mouse ATP synthase sequence is very similar to the human one, it is also a similarly different from the bacterial ATP
synthase sequences. Also, the optimal score of the alignment between the two bacterial sequences is a little higher than
the alignments between the bacteria and mouse or human, but it is much less than the alignment between mouse and human,
indicating the bacterial ATP synthases are more similar to each other than to the others, but less similar than atpa_mm
is to atpa_hs. This may be because bacterial lifespans are much shorter and bacteria exist in many different
environments with different evolutionary pressures, and they have a much higher level of reproduction than mammals which
 can lead to more mutations.

h) If we are just computing the score, we do not need to store the entire table. To calculate the value of any given
cell, we look at the max value considering the cells above, to the left, and diagonally above and to the left and their
respective calculations. To find the optimal score, we only need to look at the bottom right corner of the dp table, so
combining these two facts, we see that we can compute the optimal score by just storing two rows at a time until we
complete the sequence.

In the modified algorithm, we will store a table that is the length of the shorter sequence + 1 in one dimension (min
(m,n) + 1) and 2 in the other dimension. We start by initializing the base cases as before in the first row using the
gap penalty considering the fact that we are comparing each subsequence of sequence 2 to an empty sequence (type 2
column). Then, we start at the first element of the next row, which is also a base case with the gap penalty (the first
element in each row is a type 3 column comparing a subsequence of sequence 1 to an empty sequence). Then, we  proceed to
the right and continue calculating the values for each cell as we did in our original algorithm. Then, we can transpose
the values from the second row to the first row and repeat the process by starting with the initialization of the first
column as a base case and filling in the second row with the correct values. In this approach, the actual computation is
exactly the same, and the number of rows we consider in total is still the length of the other sequence + 1, however, we
just do not store all the past values anymore. Once we complete the row corresponding to the last row of the longer
sequence, we can find the optimal value by taking the bottom right value of the table (corresponds to dp(m,n) in the
original algorithm).