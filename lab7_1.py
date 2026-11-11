import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.Restriction import EcoRI, BamHI, HindIII

def perform_rflp_local(file_path, enzymes):
    print(f"Reading {file_path}...")
    record = SeqIO.read(file_path, "fasta")
    seq_length = len(record.seq)
    fragment_data = {}
    
    for enzyme in enzymes:
        cut_sites = enzyme.search(record.seq)
        boundaries = [0] + cut_sites + [seq_length]
        fragments = [boundaries[i+1] - boundaries[i] for i in range(len(boundaries)-1)]
        fragment_data[enzyme.__name__] = sorted(fragments, reverse=True)
        
    return record.id, fragment_data

def draw_electroforest_gel(id1, frag_dict1, id2, frag_dict2, enzymes):
    print("\nDrawing simulated gel...")
    fig, ax = plt.subplots(figsize=(10, 7))
    
    ax.set_facecolor('#111111')
    fig.patch.set_facecolor('#2b2b2b')
    
    lanes = len(enzymes) * 2
    lane_positions = range(1, lanes + 1)
    lane_labels = []
    
    current_lane = 1
    for enzyme in enzymes:
        y_vals1 = frag_dict1[enzyme.__name__]
        ax.scatter([current_lane]*len(y_vals1), y_vals1, color='cyan', marker='_', s=800, linewidth=2.5)
        lane_labels.append(f"{id1}\n{enzyme.__name__}")
        current_lane += 1
        
        y_vals2 = frag_dict2[enzyme.__name__]
        ax.scatter([current_lane]*len(y_vals2), y_vals2, color='lime', marker='_', s=800, linewidth=2.5)
        lane_labels.append(f"{id2}\n{enzyme.__name__}")
        current_lane += 1

    ax.set_yscale('log')
    ax.set_xticks(lane_positions)
    ax.set_xticklabels(lane_labels, color='white', fontsize=10)
    ax.set_ylabel('Fragment Size (Base Pairs)', color='white', fontsize=12)
    ax.set_title('Simulated RFLP Agarose Gel Comparison', color='white', fontsize=14, pad=20)
    
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='x', colors='white')
    ax.grid(axis='y', color='#333333', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_1 = "virus1.fasta" 
    file_2 = "virus2.fasta" 
    
    enzymes = [EcoRI, BamHI, HindIII]
    
    id1, fragments1 = perform_rflp_local(file_1, enzymes)
    id2, fragments2 = perform_rflp_local(file_2, enzymes)
    
    draw_electroforest_gel(id1, fragments1, id2, fragments2, enzymes)