import unittest
from aoc_validate_passphrase import validate_passphrase

results = [{'input':"aa bb cc dd ee",
            'output':True},
           {'input':"aa bb cc dd aa",
            'output':False},
           {'input':"aa bb cc dd aaa",
            'output':True},
          ]

class PassphraseTest(unittest.TestCase):
    def test_results(self):
        print('results are {}'.format(results))
        for r in results:
            print('Checking \n[{}]\n is a valid phrase is {}'.format(r['input'], r['output']))
            self.assertEqual(r['output'], validate_passphrase(r['input'])) 

if __name__ == '__main__':
    print('hello world')
    unittest.main()
