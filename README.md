# Circos plots for genomic prediction
This code is used for "Circos Plots for Genome Level Interpretation of Genomic Prediction Models" (https://www.biorxiv.org/content/10.1101/2025.05.25.656055v1).

This code aims to analyse the ensemble of multiple diverse genomic prediction models at the genome level in crop breeding programs.
Circos plots are constructed for the analysis using the effect of each genomic marker region and the interactions of these genomic marker regions for a target trait.
With a circos plot view, we can visually compare the inferred trait genetic architecture of each genomic prediction model to deepen the understanding of the predictive behaviour of each genomic prediction model at the genome level.
The comparison of the inferred genomic marker effects with known key genome regions also enables the discovery of potential new genome regions that have not been well-investigated in previous studies.


## Description
- Model: the code for seven individual genomic prediction models (rrBLUP, BayesB, RKHS, RF, SVR, MLP and GAT) and the naive ensemble-average models is stored. These genomic prediction models are implemented through the "main" function.
   - ridge regression best linear unbiased prediction (rrBLUP), BayesB and reproducing kernel Hilbert Space (RKHS): BGLR (Pérez and de Los Campos, 2014) in R (v1.1.4)
   - Random forest (RF) and support vector regression (SVR): Sklearn (Pedregosa et al., 2012) (v1.2.2) in Python (v3.11.10) 
   - Multilayer perceptron (MLP): PyTorch (Paszke et al., 2019) (v2.5.1) in Python
   - Graph attention network (GAT): PyTorch Geometric (Fey et al., 2019) (v.2.4.0) in Python 
  
- Data: example data files to run this tool
  - Details are explained in "README.md" in the Data folder

- Result: folder used as storage for output files from this tool

- genomic_prediction.py: code that bundles the genomic prediction models

- circos_plot.py: code that generates a circos plot

- main.py: the top function that manages the implementation of this tool. Users can modify the settings and hyperparameters through this function to optimise this tool based on their requirements. 

## References
Chen Q, Yang CJ, York AM, Xue W, Daskalska LL, DeValk CA, Krueger KW, Lawton SB, Spiegelberg BG, Schnell JM et al. 2019. Teonam: A nested association mapping population for domestication and agronomic trait analysis in maize. Genetics. 213:1065–1078. 

Dong Z, Danilevskaya O, Abadie T, Messina C, Coles N, Cooper M. 2012. A gene regulatory network model for floral transition of the shoot apex in maize and its dynamic modeling. PLoS ONE. 

Fey M, Lenssen JE. 2019. Fast graph representation learning with pytorch geometric. arXiv preprint arXiv:1903.02428. https://doi.org/10.48550/arXiv.1903.02428.

Lundberg SM, Lee SI. 2017. A unified approach to interpreting model predictions. Advances in neural information processing systems. 30.

Paszke A, Gross S, Massa F, Lerer A, Bradbury J, Chillemi G, Antiga L, Desmaison A, Tejani A, Chilamkurthy S et al . 2019. Pytorch: An imperative style, high-performance deep learning library. Advances in Neural Information Processing Systems. 32.

F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12:2825–2830, 2011.

Tomura S, Powell O, Wilkinson MJ, Cooper M. 2025a. Circos plots for genome level interpretation of genomic prediction models. BioRxiv.

Tomura S, Wilkinson MJ, Cooper M, Powell O. 2025b. Improved genomic prediction performance with ensembles of diverse models. G3: Genes, Genomes, Genetics. p. jkaf048. 
