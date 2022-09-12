import streamlit as st
import pandas as pd
import time
from collections import Counter
from codon_translate import codon_translate
from frequent_kmer import freq_kmer
from reverse_complement import reverse_complement
from seq_compare import seq_compare
from oligocounter import oligocounter


#Title
st.title("Kian's Bioinformatics Tools")
st.image("./img/composites-lab-header.jpg")

#Sidebar for selection of tools
st.sidebar.write("Tools Selection")
tool_select = st.sidebar.selectbox('Select Your Tool', ["Reverse Complement and Oligo Information", "Codon Amino Acid Translator", "Sequence Comparison", "Frequent K-mer"])


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
                time.sleep(0.05)
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
    st.title("Sequence Comparison")
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
                st.text('Match = + , Mismatch = - , Blank(in between) = * , Trailing Blanks = _ ')
                st.write('Matches: ', sequence_compare[3])
                st.write('Mismatches: ', sequence_compare[4])
                st.write('Blank(in between): ', sequence_compare[5])
                st.write('First Sequence Length: ', sequence_compare[6])
                st.write('Second Sequence Length: ', sequence_compare[7])
                st.write('Sequences Length Difference: ', sequence_compare[8])

#Frequent K-mer
if tool_select == "Frequent K-mer":
    st.header("Frequent K-mer")
    seq_input = st.text_area("Paste sequence (5' --> 3') in text box below: ")
    k_num = st.selectbox('Select K length', [1,2,3,4,5,6,7,8,9,10])
                         
    if st.button("Search"):
        if not seq_input:
            st.error("Please input a sequence")
        else:
            bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.05)
                bar.progress(percent_complete + 1)
            bar.empty()
            st.success("Search Done!")
            if seq_input:
                kmer = freq_kmer(seq_input, k_num)
                kmer_table = pd.DataFrame.from_dict(kmer[0], orient='index', columns=["Count"])
                st.header("Frequent K-mer Chart")
                st.bar_chart(kmer_table)
                st.header("Frequent K-mer Table")
                st.text('Table is scrollable. Click on "Count" to sort.')
                st.write(kmer_table)
                st.write("Input Sequence Length: ", kmer[3])
