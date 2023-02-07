import pytest
from main import create_mapping_list


def test_create_mapping_list_input_not_list():
    strings = 'abcde'
    regexes = ['abc', 'hij', 'klmno', 'btgrc']
    with pytest.raises(ValueError, match="Input must be a list of strings."):
        create_mapping_list(strings, regexes)

    strings = ['abcde']
    regexes = 'abc'
    with pytest.raises(ValueError, match="Input must be a list of strings."):
        create_mapping_list(strings, regexes)


def test_create_mapping_list_input_not_string():
    strings = ['abcde', 'fghij', 9, 'abc', 'hij']
    regexes = ['abc', 'hij', 'klmno', 'btgrc']
    with pytest.raises(ValueError, match="Input must be a list of strings."):
        create_mapping_list(strings, regexes)

    strings = ['abcde', 'fghij', 'klmnoabc9', 'abc', 'hij']
    regexes = ['abc', 'hij', 'klmno', 9]
    with pytest.raises(ValueError, match="Input must be a list of strings."):
        create_mapping_list(strings, regexes)


def test_create_mapping_list_output():
    strings = ['abcde', 'fghij', 'klmnoabc9', 'abc', 'hij']
    regexes = ['abc', 'hij', 'klmno', 'bcdno']
    expected_output = [('abc', ('abcde', 'klmnoabc9', 'abc')),
                       ('hij', ('fghij', 'hij')),
                       ('klmno', ('klmnoabc9',)),
                       ('bcdno', ())]
    assert create_mapping_list(strings, regexes) == expected_output


def test_create_mapping_list_empty_input():
    strings = []
    regexes = []
    expected_output = []
    assert create_mapping_list(strings, regexes) == expected_output


def test_create_mapping_list_no_matches():
    strings = ['abcde', 'fghij', 'klmnoabc9', 'abc', 'hij']
    regexes = ['z', 'y', 'x']
    expected_output = [('z', ()),
                       ('y', ()),
                       ('x', ())]
    assert create_mapping_list(strings, regexes) == expected_output


def test_create_mapping_list_multiple_matches():
    strings = ['abcde', 'fghij', 'klmnoabc9', 'abc', 'hij']
    regexes = ['ab', 'hi', 'klmno']
    expected_output = [('ab', ('abcde', 'klmnoabc9', 'abc')),
                       ('hi', ('fghij', 'hij')),
                       ('klmno', ('klmnoabc9',))]
    assert create_mapping_list(strings, regexes) == expected_output
