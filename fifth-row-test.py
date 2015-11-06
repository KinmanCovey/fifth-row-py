#!/usr/bin/env python
import unittest, fifthrow
from fifthrow.fifthrow import *

class FifthRowTest(unittest.TestCase):

    def test_url(self):
        '''
        FifthRow object's url should be the sandboxed url
        '''
        self.assertEqual(FifthRow(sandbox=True).url, 'sandbox.the5throw.com')

    def test_get_return(self):
        '''
        FifthRow.get() should return a list of Matchup objects
        '''
        data = FifthRow(sandbox=True).get('nba')
        self.assertIs(type(data), list)
        self.assertEqual(data[0].__class__, Matchup)

    def test_token_error(self):
        '''
        TokenError should be raised if token != an integer
        '''
        self.assertRaises(TokenError, FifthRow, sandbox=False, token=None)

if __name__ == '__main__':
    unittest.main()
