from Bio import SeqIO
from Bio.Restriction import EcoRI, BamHI, HindIII

def digest_local_sequence(file_path):
    # Read the downloaded FASTA file
    record = SeqIO.read(file_path, "fasta")
    dna_sequence = record.seq
    
    print(f"Sequence ID: {record.id}")
    print(f"Sequence Length: {len(dna_sequence)} nucleotides\n")
    
   
    enzymes = [EcoRI, BamHI, HindIII]
    
    print("--- Restriction Digest Results ---")
    for enzyme in enzymes:
        
        cut_sites = enzyme.search(dna_sequence)
        
        
        print(f"Enzyme: {enzyme.__name__}")
        print(f"Recognition Site: 5'-{enzyme.site}-3'")
        
        if cut_sites:
            print(f"Number of cuts: {len(cut_sites)}")
            print(f"Cleavage positions (1-based index): {cut_sites}\n")
        else:
            print("No cut sites found in this sequence.\n")

if __name__ == "__main__":
    digest_local_sequence("sequence.fasta")