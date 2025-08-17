COMPSCI 260 - Problem Set 3, Problem 2
Due: Fri 23 Feb 2024, 5pm

Name: Cindy Su
NetID: cs699

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9668099/
2. https://my.clevelandclinic.org/health/drugs/22650-acidophilus
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3570796/
4. https://www.nature.com/articles/s41598-022-12721-4
5. https://www.tandfonline.com/doi/full/10.1080/19490976.2023.2249152
6. https://www.nature.com/articles/ismej20124
7. https://en.wikipedia.org/wiki/Vibrio_cholerae
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8244777/
9. https://www.cdc.gov/cholera/treatment/antibiotic-treatment.html#:~:text=Oral%20or%20intravenous%20hydration%20is,
of%20stool%20during%20rehydration%20treatment.
10. https://en.wikipedia.org/wiki/Peptoniphilus


My solutions and comments for this problem are below.
-----------------------------------------------------
a) Lactobacillus acidophilus is a mutualistic bacterium that is an important probiotic in the GI tract. It is thought to
 have good resistance against acid and bile salts, making it able to grow where other lactic acid bacteria cannot. Also,
 at a threshold level, L. acidophilus has positive nutritional effects, regulatory roles in intestinal microbiota
 balance, and helps immunity and cholesterol reduction. It also produces lactic acid that can inhibit the growth of
 pathogenic bacteria. L. acidophilus is naturally prevalent in the human gut and in other parts of the body due to
 its helpful role in the immune and digestive system. Some also take probiotics to raise the levels of the microbe in
 their body and potentially gain more benefits. [1][2]

Peptoniphilus timonensis is part of the Peptoniphilus genus, which has species that are butyrate-producing and use
peptones and oligopeptide as a major energy source. P. timonesis is susceptible to many antibiotics. As mentioned in the
description of Eubacterium rectale, butyrate is an important energy source for cells in the colonic epithelium. This
appears to be a less studied bacterium and does not have much information about the prevalence or function, but the fact
that this bacteria has only been described a few times and most seem to reference a single article may indicate that it
is not prevalent in the human gut because barely anyone has isolated it. Other strains of Peptoniphilus have been
isolated in other body systems and linked to impaired healing or disease.
[3][10]

Prevotella copri is abundant (~40% prevalence of the Provetella species) in the human gut, and it has been detected in
many profiling studies because it is vastly distributed, and some sources claim it is beneficial while others believe it
is harmful to human health. It is believed to be an enterotype with Bacteroids because their prevalences are inversely
correlated, perhaps suggesting that they fight for the same nutrients. There have also been variations in prevalence of
P. copri notes based on different diets. P. copri is thought to decrease inflammation by detoxifying certain reactive
oxygen species and protecting the mucosal barrier. However, some studies report on P. copris detrimental effects:
insulin resistance, hypertension, and gut inflammation. [4][5]

Ruminococcus bromii is important for fermentation of resistant starches (RS) and can break down certain RS that E.
rectale and B. thetaoitaomicron cannot, and its degradation products can be used by other bacteria. Fermentation of RS
is thought to have beneficial health impacts like reducing insulin resistance, reversing infectious diarrhea, and
prevent colorectal cancer. It is abundant like E. rectale and the Bacteroides genus especially because it is a keystone
species, meaning that it has a very important function (degradation products used by other bacteria). The
Ruminococccaeae cluster of bacteria make up about 10-40% of total bacterial 16S rRNA sequences. [6]

Some strains of Vibrio cholerae are pathogenic to humans and cause cholera which is fatal and can be caused by eating
undercooked seafood or drinking contaminated water. It attacks the intestinal mucosa killing native gut
microbiota and causing dehydration through diarrhea and vomiting, and it must also maintain its virulence in the
environment of the human gut. Millions of people get cholera every year. However, there are also strains of V. cholerae
that are non-pathogenic (in fact, it is around 75% of the cases). Nevertheless, in a healthy human gut, the prevalence
of V. cholerae is extremely low, and most people only have elevated levels from consuming contaminated food. [7][8]

c) find the reverse complement of the reads because it makes it much simpler to find the start position of the matched
reads because it will be exactly what the function outputs. Even though reverse complementing the genomes may take less
time because it is much less nucloetides than the 100,000 reads, it would require work to adjust the index for each
match, and I did not want to change it in the find function because that would make it not work with the general case of
non reverse-complemented inputs.
The total number of matches is 299964, meaning that 36 reads either do not match to any genome or match to multiple.

d)
The prevalence of Bacteroides_ovatus in patient1 is 0.1951.
The prevalence of Bacteroides_thetaiotaomicron in patient1 is 0.1641.
The prevalence of Bifidobacterium_longum in patient1 is 0.0475.
The prevalence of Eubacterium_rectale in patient1 is 0.03.
The prevalence of Lactobacillus_acidophilus in patient1 is 0.0665.
The prevalence of Peptoniphilus_timonensis in patient1 is 0.1315.
The prevalence of Prevotella_copri in patient1 is 0.0875.
The prevalence of Roseburia_intestinalis in patient1 is 0.1446.
The prevalence of Ruminococcus_bromii in patient1 is 0.0815.
The prevalence of Vibrio_cholerae in patient1 is 0.0517.

The prevalence of Bacteroides_ovatus in patient2 is 0.065.
The prevalence of Bacteroides_thetaiotaomicron in patient2 is 0.0375.
The prevalence of Bifidobacterium_longum in patient2 is 0.0515.
The prevalence of Eubacterium_rectale in patient2 is 0.0405.
The prevalence of Lactobacillus_acidophilus in patient2 is 0.013.
The prevalence of Peptoniphilus_timonensis in patient2 is 0.0765.
The prevalence of Prevotella_copri in patient2 is 0.1295.
The prevalence of Roseburia_intestinalis in patient2 is 0.0435.
The prevalence of Ruminococcus_bromii in patient2 is 0.0465.
The prevalence of Vibrio_cholerae in patient2 is 0.4965.

The prevalence of Bacteroides_ovatus in patient3 is 0.2145.
The prevalence of Bacteroides_thetaiotaomicron in patient3 is 0.1545.
The prevalence of Bifidobacterium_longum in patient3 is 0.061.
The prevalence of Eubacterium_rectale in patient3 is 0.0435.
The prevalence of Lactobacillus_acidophilus in patient3 is 0.0585.
The prevalence of Peptoniphilus_timonensis in patient3 is 0.161.
The prevalence of Prevotella_copri in patient3 is 0.0985.
The prevalence of Roseburia_intestinalis in patient3 is 0.13.
The prevalence of Ruminococcus_bromii in patient3 is 0.078.
The prevalence of Vibrio_cholerae in patient3 is 0.0005.

e) Patient 1 and 3 have very similar prevalences for all 10 microbes except the prevalence of Vibrio cholerae is about
10x more in patient 1 than patient 3. Patient 2 has very different prevalences for all the microbes, but this seems to
be due to the drastically increased prevalence of Vibrio Cholerae, as it makes up almost 50% of the reads. Some
individual microbes still have similar prevalences, like Bifidobacterium longum, and Eubacterium rectale, while most
others are decreased compared to 1 and 2. However, Prevotella copri is also elevated in Patient 2, which a prevalence of
about 0.1295 whereas in Patients 1 and 3, it is under 0.1. Considering the added scaling due to the high V. cholerae
prevalence, this actually indicates a signficant elevation of P. copri in Patient 2. As mentioned before, P. copri has a
lot of debate surrounding its role in the body, and some say it reduces inflammation while others say it causes it. In
this case, it is possible that it is more abundant because it is reducing inflammation caused by pathogenic V.
cholerae, or alternatively, it may be contributing to the patient's symptoms. It is also interesting to  note that some
of the bacteria we identified as mutualistic have higher prevalences, like B. ovatus, B. thetaiotaomicron, R.
intestinalis. Interestingly, P. timonensis is also quite abundant, but I did not find very much information about its
function. V. cholerae, which seems to be the most dangerous microbe, has a significantly lower prevalence than any of
the other bacteria in a healthy patient like patient 3.

g) The start and stop positions of the longest stretch of zeros for patient 1 are 5016 and 5080 (1-indexed)
respectively.
There are no stretches of zeros for patient 2.

h) The sequence in the segment with no reads mapped to it in patient 1 is
TACCGGCCAGGTGCAACTTTTCAAGTAGAAGTACCAGGTAGTCAACATATAGATTCACAACCTT. When I looked up this sequence on BLAST, it matched to
Vibrio cholerae, but many strains matched with 100% identity, so I could not tell exactly what strain it was exactly,
but all the matches have enterotoxin in their name, indicating that they contain the toxin gene from a bacteriophage.
As described from my research, there are both pathogenic and non-pathogenic strains of V. cholerae, which aligns with
our observations of one symptomatic and one asymptomatic patient both with elevanted V. cholerae levels. We can
hypothesize that patient 1 has a strain without the toxin gene while patient 2 has the one with the toxin gene, and it
makes sense that there was an unsequenced region with the reads from patient 1 since we used a reference genome with the
toxin gene.
Knowing this, I would definitely tell patient 2 that they had the pathogenic strain of V. cholerae which explains all
their symptoms, and it can be treated with oral or IV hydration, and if the symptoms persist or worsen, a course of
antibiotic treatment. [9] As for patient 1, they have elevated levels of V. cholerae, but it seems to not have the toxic
gene and not be pathogenic, so it may not be of much concern. However, even non-pathogenic strains of V. cholerae can
cause mild illness or be dangerous if a patient becomes immunocompromised, so since we are aware of the elevated levels,
it may be beneficial to treat it or tell the patient about the elevated levels but not to be too concerned.