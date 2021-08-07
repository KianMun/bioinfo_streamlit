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
            compare.append('-')


    len_diff = abs(len(first_seq) - len(second_seq))
    compare.append(len_diff * '_')

                  
    return first_seq, ''.join(compare), second_seq, compare.count('+'), compare.count('-'), compare.count('*'), len(first_seq), len(second_seq), len_diff
