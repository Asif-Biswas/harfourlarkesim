import unittest
from main import create_mapping_list

class TestCreateMappingList(unittest.TestCase):
    def test_create_mapping_list(self):
        strings = ['string1', 'string2', 'string3']
        regexes = ['regex1', 'regex2', 'regex3']
        expected_output = [('regex1', ('string1', 'string2', 'string3')), \
                           ('regex2', ('string1', 'string2', 'string3')), \
                            ('regex3', ('string1', 'string2', 'string3'))]
        
        result = create_mapping_list(strings, regexes)
        self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()
