import seq_features as sf
import pytest

def test_number_negative_single_aa():
    """perform unit tests on number_negatives()"""
    assert sf.number_negative('E')==1
    assert sf.number_negative('EEEEAAA')==4
    
def test_number_negative_short_seqs():   
    assert sf.number_negative('D')==1
    
    
def test_number_negative_lowercases(): 
    assert sf.number_negative('adese')==3

# want the program to understand errors
def test_number_negative_invalid_amino_acid(): 
    with pytest.raises(RuntimeError) as excinfo:
        sf.number_negative('Z')
    excinfo.match('Z is not a valid amino acid.')
    
    
###

def test_number_posiive_single_aa():
    """perform unit tests on number_positives()"""
    assert sf.number_positive('E')==0
    assert sf.number_positive('D')==0
    assert sf.number_positive('R')==1
    assert sf.number_positive('K')==1
    assert sf.number_positive('H')==1
    
def test_number_positive_short_seqs():   
    assert sf.number_positive('EEEEAAA')==0
    assert sf.number_positive('KRAKRHAAA')==5
    
def test_number_positive_lowercases(): 
    assert sf.number_positive('adese')==0
    assert sf.number_positive('akrhdfseds')==3
    

# want the program to understand errors
def test_number_positive_invalid_amino_acid(): 
    with pytest.raises(RuntimeError) as excinfo:
        sf.number_positive('Z')
    excinfo.match('Z is not a valid amino acid.')

def test_is_valid_with_Z():
    """perform unit tests on is_valid()"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.is_valid('Z')
    excinfo.match('Z is not a valid amino acid.')
    
def test_is_valid_with_short_but_wrong_seq():
    """perform unit tests on is_valid()"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.is_valid('skd&&&')
    excinfo.match('& is not a valid amino acid.')