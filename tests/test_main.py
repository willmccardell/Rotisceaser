#!/usr/bin/env python3

# import pytest
import rotisceaser.main as rot

def test_pizza_13():
    rot_input = 'jr ner beqrevat cvmmn gbavtug'
    expected_output = 'ROT-13: Probability: 100.0% : we are ordering pizza tonight'
    assert rot.main(rot_input, False) == expected_output

def test_pizza_7():
    rot_input = 'px tkx hkwxkbgz ibsst mhgbzam'
    expected_output = 'ROT-7: Probability: 100.0% : we are ordering pizza tonight'
    assert rot.main(rot_input, False) == expected_output

def test_strip_punc():
    rot_input = 'zxq, ald! yxq'
    expected_output = 'ROT-3: Probability: 100.0% : cat dog bat'
    assert rot.main(rot_input, False) == expected_output

def test_strip_punc_compared():
    rot1_input = 'zxq, ald! yxq'
    rot2_input = 'zxq ald yxq'
    assert rot.main(rot1_input, False) == rot.main(rot2_input, False)

def test_full_output():
    rot_input = 'no i am the brave computer'
    expected_output = ('The original cypher was \"no i am the brave computer\".\n' +
                        'Determining most likely rotation factor.\n' +
                        'ROT-0: Probability: 100.0% : no i am the brave computer\n' +
                        'ROT-5: Probability: 50.0% : st n fr ymj gwfaj htruzyjw\n')
    assert rot.main(rot_input, True) == expected_output