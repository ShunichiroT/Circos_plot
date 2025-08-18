# Ensemble AnalySis with Interpretable Genomic Prediction (EasiGP): Computational Tool for Interpreting Ensembles of Genomic Prediction Models
This code is used for "Ensemble AnalySis with Interpretable Genomic Prediction (EasiGP): Computational Tool for Interpreting Ensembles of Genomic Prediction Models".

This code aims to analyse the ensemble of multiple diverse genomic prediction models at the genome level in crop breeding programs.
Circos plots are constructed for the analysis using the effect of each genomic marker region and the interactions of these genomic marker regions for a target trait.
With a circos plot view, we can visually compare the inferred trait genetic architecture of each genomic prediction model to deepen the understanding of the predictive behaviour of each genomic prediction model at the genome level.
The comparison of the inferred genomic marker effects with known key genome regions also enables the discovery of potential new genome regions that have not been well-investigated in previous studies.


## Description
- Model: the code for seven individual genomic prediction models (rrBLUP, BayesB, RKHS, RF, SVR, MLP and GAT) and the naive ensemble-average models is stored. These genomic prediction models are implemented through the "main" function.
   - ridge regression best linear unbiased prediction (rrBLUP), BayesB and reproducing kernel Hilbert Space (RKHS): BGLR (Pérez and de Los Campos, 2014) in R
   - Random forest (RF) and support vector regression (SVR): Sklearn (Pedregosa et al., 2012) in Python
   - Multilayer perceptron (MLP): PyTorch (Paszke et al., 2019) in Python
   - Graph attention network (GAT): PyTorch Geometric (Fey et al., 2019) in Python 
  
- Data: example data files based on the TeoNAM dataset (Chen et al., 2019) to run this tool
  - Details are explained in "README.md" in the Data folder

- Result: folder used as storage for output files from this tool

- environment_windows.yml: a list of packages needed to implement this tool in Windows

- environment_linux.yml: a list of packages needed to implement this tool in Linux

- genomic_prediction.py: code that bundles the genomic prediction models. This function is implemented through the "main" function.

- circos_plot.py: code that generates a circos plot. This function is implemented through the "main" function.

- main.py: the top function that manages the implementation of this tool. Users can modify the settings and hyperparameters through this function to optimise this tool based on their requirements.

## Procedure
1. Download this tool
2. Develop an environment using the "environment.yml" file
   - It is recommended to use Anaconda for the environment development
3. Prepare the relevant data in the specified format
   - Check "README.md" in the Data folder for the format details
4. Adjust settings and hyperparameters in the "main" function
   - Check the explanations in the code for the details 
6. Implement the code
7. Check and analyse the generated output files in the Result folder 

## References
Chen Q, Yang CJ, York AM, Xue W, Daskalska LL, DeValk CA, Krueger KW, Lawton SB, Spiegelberg BG, Schnell JM et al. 2019. Teonam: A nested association mapping population for domestication and agronomic trait analysis in maize. Genetics. 213:1065–1078. 

Dominik G. Grimm, Damian Roqueiro, Patrice A. Salomé, Stefan Kleeberger, Bastian Greshake, Wangsheng Zhu, Chang Liu, Christoph Lippert, Oliver Stegle, Bernhard Schölkopf, Detlef Weigel, Karsten M. Borgwardt. 2017. easyGWAS: A Cloud-Based Platform for Comparing the Results of Genome-Wide Association Studies. The Plant Cell. 29. 5-19.

Dong Z, Danilevskaya O, Abadie T, Messina C, Coles N, Cooper M. 2012. A gene regulatory network model for floral transition of the shoot apex in maize and its dynamic modeling. PLoS ONE. 

Fey M, Lenssen JE. 2019. Fast graph representation learning with pytorch geometric. arXiv preprint arXiv:1903.02428.

Gibbs, Patrick M., Jefferson F. Paril, and Alexandre Fournier-Level. 2025. Trait genetic architecture and population structure determine model selection for genomic prediction in natural Arabidopsis thaliana populations. Genetics 229.3: iyaf003.

Lundberg SM, Lee SI. 2017. A unified approach to interpreting model predictions. Advances in neural information processing systems. 30.

Paszke A, Gross S, Massa F, Lerer A, Bradbury J, Chillemi G, Antiga L, Desmaison A, Tejani A, Chilamkurthy S et al . 2019. Pytorch: An imperative style, high-performance deep learning library. Advances in Neural Information Processing Systems. 32.

F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12:2825–2830, 2011.

The 1001 Genomes Consortium. 2016. 1,135 Genomes Reveal the Global Pattern of Polymorphism in Arabidopsis thaliana. Cell. 166(2). 481-491.

Tomura S, Wilkinson MJ, Cooper M, Powell O. 2025. Improved genomic prediction performance with ensembles of diverse models. G3: Genes, Genomes, Genetics. p. jkaf048. 
