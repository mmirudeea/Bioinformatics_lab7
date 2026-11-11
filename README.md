# Bioinformatics Lab: Restriction Enzyme Analysis & RFLP Simulation

## Exercise 1: Single Sequence Digestion
**Prompt:** 
1. Take an arbitrary DNA sequence from NCBI between 1000-3000 nucleotides (letters). 
2. Use 3 restriction enzymes (name, recognition sequence, cleavage site).

*Implementation Details:*
* **Target Sequence:** pUC19 cloning vector (NCBI Accession: M77789.2, 2686 bp).
* **Enzymes Used:** 
  * EcoRI (5'-G|AATTC-3')
  * BamHI (5'-G|GATCC-3')
  * HindIII (5'-A|AGCTT-3')
* **Objective:** Parse the sequence from a local FASTA file and output the exact 1-based cleavage positions for each enzyme.

## Exercise 2: Viral Genome RFLP Comparison
**Prompt:** 
Download two viral genomes of the same virus species. Apply the previous list of restriction enzymes and compare the resulting fragments in a simulated electrophoresis gel to visualize the genetic differences between the two versions.

*Implementation Details:*
* **Target Sequences:** Two strains of *Human mastadenovirus C*:
  * Strain 1: Human adenovirus 2 (NCBI Accession: NC_001405.1)
  * Strain 2: Human adenovirus 5 (NCBI Accession: AC_000008.1)
* **Objective:** Digest both viral genomes locally using EcoRI, BamHI, and HindIII. Calculate the resulting fragment sizes and plot them on a logarithmic scale using `matplotlib` to simulate an agarose gel, allowing for direct visual comparison of restriction site polymorphisms.
