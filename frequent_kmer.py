

from collections import Counter


def freq_kmer(seq, k):
    kmer = []
    seq = seq.upper()
    for i in range(k):
        for j in range(len(seq)):
            k_interval = seq[i+j:i+j+k]
            if len(k_interval) == k:
                kmer.append(seq[i+j:i+j+k])

    freq_dict = dict(Counter(kmer))
    freq_kmer = max(freq_dict, key= freq_dict.get)
    freq_kmer_count = freq_dict.get(freq_kmer)

    return freq_dict, freq_kmer, freq_kmer_count, len(seq)


