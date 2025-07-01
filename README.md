# Circos plot for genomic prediction
This code is used for "Circos Plots for Genome Level Interpretation of Genomic Prediction Models" (https://www.biorxiv.org/content/10.1101/2025.05.25.656055v1).

This code aims to visualise the effect of each genomic marker region and the interactions of these genomic marker regions for a target trait in crop breeding programs.
With a circos plot view, we can visually compare the inferred trait genetic architecture of each genomic prediction model to deepen the understanding of the predictive behaviour of each genomic prediction model at the genome level.
The comparison of the inferred genomic marker effects with known key genome regions also enables the discovery of potential new genome regions that have not been well-investigated in the previous studies.


## Description
- "Code" contains the source code that can generate a circos plot in the paper
- "Data" includes example files required to generate a circos plot
  - "Chromosome": the length of chromosomes. The folder contains the length of each chromosome across populations and each population (five populations in total) as example
  - "Interactions": the estimated pairwise interactions between genome regions. Interactions were inferred using Shapley scores (SHAP) from Random Forest in this paper. The folder contains example interactions across populations and within each population
  - "Key markers": the known genome regions that regulate flowering time in maize. For QTL, the information was extracted from Chen et al. (2019). For the leaf and shoot apical meristem (SAM), the gene information from Dong et al. (2012) was used. The folder contains the example location of each key genomic marker region across populations and within each population.
  - "Marker effect": the inferred genomic marker effects from each genomic prediction model. The genomic marker effects were inferred from the interpretable methods used in Tomura et al. (2025b). The folder contains example genomic marker effects across populations and within each population

## References
Chen Q, Yang CJ, York AM, Xue W, Daskalska LL, DeValk CA, Krueger KW, Lawton SB, Spiegelberg BG, Schnell JM et al. 2019. Teonam: A nested association mapping population for domestication and agronomic trait analysis in maize. Genetics. 213:1065–1078. 

Dong Z, Danilevskaya O, Abadie T, Messina C, Coles N, Cooper M. 2012. A gene regulatory network model for floral transition of the shoot apex in maize and its dynamic modeling. PLoS ONE. 

Lundberg SM, Lee SI. 2017. A unified approach to interpreting model predictions. Advances in neural information processing systems. 30.

Tomura S, Powell O, Wilkinson MJ, Cooper M. 2025a. Circos plots for genome level interpretation of genomic prediction models. BioRxiv.

Tomura S, Wilkinson MJ, Cooper M, Powell O. 2025b. Improved genomic prediction performance with ensembles of diverse models. G3: Genes, Genomes, Genetics. p. jkaf048. 
