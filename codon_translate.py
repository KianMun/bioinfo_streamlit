#Codon dictionary
codon = {'GCT' : 'Ala','GCC' : 'Ala','GCA': 'Ala', 'GCG': 'Ala', 'TTT' :'Phe','TTC' :'Phe',
         'TTA' : 'Leu', 'TTG': 'Leu', 'CTT': 'Leu','CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
         'ATT' : 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG' : 'Met',
         'GTT' : 'Val', 'GTC' : 'Val', 'GTA' : 'Val', 'GTG' : 'Val', 'TCT' : 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser', 'AGT': 'Ser', 'AGC': 'Ser',
         'CCT' : 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'ACT' : 'Thr', 'ACC' : 'Thr', 'ACA' : 'Thr', 'ACG' : 'Thr',
         'TAT' : 'Tyr', 'TAC' : 'Tyr', 'TAA' : 'Ter', 'TAG' : 'Ter', 'TGA' : 'Ter', 'CAT' : 'His', 'CAC': 'His',
         'CAA' : 'Gln', 'CAG' : 'Gln', 'AAT' : 'Asn', 'AAC' : 'Asn', 'AAA' : 'Lys', 'AAG' : 'Lys',
         'GAT' : 'Asp', 'GAC' : 'Asp', 'GAA' : 'Glu', 'GAG' : 'Glu', 'TGT' : 'Cys', 'TGC' : 'Cys', 'TGG' : 'Trp',
         'CGT' : 'Arg', 'CGC' : 'Arg', 'CGA' : 'Arg', 'CGG' : 'Arg', 'AGA' : 'Arg', 'AGG' : 'Arg', 'GGT' : 'Gly', 'GGC' : 'Gly', 'GGA' : 'Gly', 'GGG' : 'Gly'}

#Amino acid full name
amino_acid_full = {'Ala': 'Alanine', 'A':'Alanine', 'Phe':'Phenylalanine', 'F':'Phenylalanine', 'Leu':'Leucine', 'L':'Leucine',
              'Ile': 'Isoleucine', 'I':'Isoleucine', 'Met': 'Methionine', 'M':'Methionine', 'Val': 'Valine', 'V':'Valine','Ser': 'Serine', 'S':'Serine',
              'Pro':'Proline', 'P':'Proline', 'Thr': 'Threonine', 'T':'Threonine', 'Tyr': 'Tyrosine', 'Y':'Tyrosine',
              'Ter': 'Termination', '*': 'Termination', 'His' : 'Histidine', 'H' :'Histidine',
              'Gln' : 'Glutamine', 'Q' :'Glutamine', 'Asn': 'Asparagine', 'N':'Asparagine', 'Lys': 'Lysine', 'K':'Lysine',
              'Asp': 'Aspartate' , 'D':'Aspartate', 'Glu': 'Glutamate', 'E':'Glutamate', 'Cys' : 'Cysteine', 'C' :'Cysteine',
              'Trp': 'Tryptophan', 'W':'Tryptophan', 'Arg': 'Arginine', 'R':'Arginine', 'Gly': 'Glycine', 'G':'Glycine'}


#Function to translate codon to amino acid
def codon_translate(sequence):
    seq = sequence.upper()
    seq = seq.replace('U', 'T')
    seq_threes = []
    aa_match = []
    indx = []
    length = len(sequence)
    
    for i in range(0, len(seq),3):
        seq_threes.append(seq[i:i+3])
    for amino, code in codon.items():
        for j in range(len(seq_threes)):
            if amino == seq_threes[j]:
                aa_match.append(code)
                indx.append(j)
                
    position = [k +(k*2 + 1) if k>0 else k + 1  for k in indx]
    aa_match = [x for _, x in sorted(zip(indx, aa_match))]

    aa_fullname = []
    fullname_indx = []
    
    for k, v in amino_acid_full.items():
        for l in range(len(aa_match)):
            if k  == aa_match[l]:
                aa_fullname.append(v)
                fullname_indx.append(l)

    aa_fullname = [y for _, y in sorted(zip(fullname_indx, aa_fullname))]
    
    return aa_match, sorted(position), length, aa_fullname
