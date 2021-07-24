import streamlit as st
import pandas as pd
import time

def oligocounter(oligo):
    atgc_counter = 0
    a_counter = 0
    t_counter = 0
    g_counter = 0
    c_counter = 0
    u_counter = 0
    counter = len(oligo)
    gc_counter = g_counter + c_counter
    gc_content = 0

    for i in oligo.lower():
        if i == 'a':
            a_counter += 1
        elif i == 't':
            t_counter += 1
        elif i == 'u':
            u_counter += 1
        elif i == 'g':
            g_counter += 1
        elif i == 'c':
            c_counter += 1
        else:
            atgc_counter += 0

    gc_counter = g_counter + c_counter
    
    if gc_counter > 0:
        gc_content = "{:.2f}".format(gc_counter/counter * 100)

    non_atgc = counter - atgc_counter

    return a_counter, t_counter, g_counter, c_counter, u_counter, counter,  gc_counter, gc_content

def reverse_complement(template):
    reverse =''
    for i in template.lower():
        if i == 'a':
            reverse += 't'
        elif i == 't':
            reverse += 'a'
        elif i == 'g':
            reverse += 'c'
        elif i == 'c':
            reverse += 'g'
        elif i == 'u':
            reverse += 'a'   

    return reverse[::-1]

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

#Function for sequence comparison
def seq_compare(seq_a, seq_b):
    first_seq = seq_a.lower()
    second_seq = seq_b.lower()
    compare =[]

    for i,j in zip(first_seq, second_seq):
        if i == ' ' or j == ' ':
            compare.append('*')
        elif i == j:
            compare.append('+')
        elif i != j:
            compare.append('~')


    len_diff = abs(len(first_seq) - len(second_seq))
    compare.append(len_diff * '_')

                  
    return first_seq, ''.join(compare), second_seq, compare.count('+'), compare.count('~'), compare.count('*'), len_diff


#Title
st.title("Kian's Bioinformatics Tools")
st.image("./img/composites-lab-header.jpg")

#Sidebar for selection of tools
st.sidebar.write("Tools Selection")
tool_select = st.sidebar.selectbox('Select Your Tool', ["Reverse Complement and Oligo Information", "Codon Amino Acid Translator", "Sequence Comparison"])


#Reverse Complement and Oligo Information
if tool_select =="Reverse Complement and Oligo Information":
    st.header("Reverse Complement and Oligo Information")
    user_input = st.text_area("Paste sequence (5' ---> 3') in text box below: ")

    if st.button("Process"):

        if not user_input:
            st.error("Please input a sequence")
            
        else:
            rev_seq = reverse_complement(user_input)
            oligo_content = list(oligocounter(user_input))
            st.header("Reverse Complement(5' ---> 3')")
            st.header(rev_seq)
            #st.dataframe(pd.DataFrame({"Reverse Complement(5' ---> 3')":[rev_seq]}))
            oligo_df = pd.DataFrame({'Content':['A', 'T', 'G', 'C', 'U', 'Total Length'],
                                     'Count':[oligo_content[0], oligo_content[1], oligo_content[2], oligo_content[3],
                                              oligo_content[4], oligo_content[5]]})
            gc_df = pd.DataFrame({'Content':['GC', 'GC%'], 'Count':[oligo_content[6], oligo_content[7]]})
            st.header("Oligo Content")
            st.dataframe(oligo_df)
            st.header("GC Content")
            st.dataframe(gc_df)
      
        
#Codon Amino Acid Translator

if tool_select == "Codon Amino Acid Translator":
    st.header("Codon Amino Acid Translator")
    codon_user_input = st.text_area("Paste sequence (5' --> 3') in text box below: ")

    if st.button("Translate"):
        if not codon_user_input:
            st.error("Please input a sequence")
        else:
            bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                bar.progress(percent_complete + 1)
            bar.empty()
            st.success("Translation Done!")
            if codon_user_input:
                amino_acid = codon_translate(codon_user_input)
                codon_pos = amino_acid[1]
                am_a = amino_acid[0]
                am_full = amino_acid[3]
                d = {'Codon Position': codon_pos, 'Amino Acid Shortform': am_a, 'Amino Acid Fullname': am_full}
                codon_df = pd.DataFrame(d)
                st.header("Amino Acid Results Table")
                st.dataframe(codon_df)
                st.header("Sequence length")
                st.header(amino_acid[2])

#Sequence Comparison
if tool_select == "Sequence Comparison":
    st.header("Sequence Comparison")
    st.header("First Sequence")
    first_sequence = st.text_area("Paste your First Sequence (5' --> 3') in text box below: ")
    st.header("Second Sequence")
    second_sequence = st.text_area("Paste your Second Sequence (5' --> 3') in text box below: ")
    
    if st.button("Compare"):
        if not first_sequence:
            st.error('Please input a sequence in "First Sequence"')
        elif not second_sequence:
            st.error('Please input a sequence in "Second Sequence"')
        else:
            bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                bar.progress(percent_complete + 1)
            bar.empty()
            st.success("Comparison Done!")
            
            if first_sequence and second_sequence:
                sequence_compare = seq_compare(first_sequence, second_sequence)
                st.header("Comparison Results")
                st.text(sequence_compare[0])
                st.text(sequence_compare[1])
                st.text(sequence_compare[2])
                st.text('\nMatch = +, Mismatch =~, Blank(in between) = *, Trailing Blanks = _') 
                
