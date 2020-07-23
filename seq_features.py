import bootcamp_utils

def is_valid(seq):
    seq=seq.upper()
    for aa in seq:
        if aa not in bootcamp_utils.aa.keys():
            raise RuntimeError(aa+' is not a valid amino acid.')  

def prep_seq(seq):
    return seq.upper()

def number_negative(seq):
    """Number of negative res in a protein seq"""
    seq=prep_seq(seq)
    is_valid(seq)
    return seq.count('E')+ seq.count('D')
    #pass

def number_positive(seq):
    """Number of positive res in a protein seq"""    
    seq=prep_seq(seq)
    is_valid(seq)
    return seq.count('R')+ seq.count('K')+ seq.count('H')