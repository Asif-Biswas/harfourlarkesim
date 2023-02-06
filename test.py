import pytest
from main import create_mapping_list

def test_create_mapping_list_valid_input():
    strings = ['string1', 'string2', 'string3']
    regexes = ['regex1', 'regex2', 'regex3']
    result = create_mapping_list(strings, regexes)
    expected_result = [('regex1', ('string1', 'string2', 'string3')),
                       ('regex2', ('string1', 'string2', 'string3')),
                       ('regex3', ('string1', 'string2', 'string3'))]
    assert result == expected_result

def test_create_mapping_list_invalid_input():
    strings = 'string1'
    regexes = ['regex1', 'regex2', 'regex3']
    with pytest.raises(ValueError, match='Input must be a list of strings.'):
        create_mapping_list(strings, regexes)

def test_create_mapping_list_empty_input():
    strings = []
    regexes = []
    result = create_mapping_list(strings, regexes)
    expected_result = []
    assert result == expected_result

def test_create_mapping_list_invalid_input_type():
    strings = ['string1', 'string2', 'string3']
    regexes = 'regex1'
    with pytest.raises(ValueError, match='Input must be a list of strings.'):
        create_mapping_list(strings, regexes)

def test_create_mapping_list_empty_input_type():
    strings = ''
    regexes = ''
    with pytest.raises(ValueError, match='Input must be a list of strings.'):
        create_mapping_list(strings, regexes)


