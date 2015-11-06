#!/usr/bin/env python
import unittest, fifthrow
from fifthrow.fifthrow import *

class FifthRowTest(unittest.TestCase):

    def test_sandboxed_url(self):
        '''
        FifthRow object's url should be the sandboxed url.
        '''
        self.assertEqual(FifthRow(sandbox=True).url, 'sandbox.the5throw.com')

    def test_sandboxed_token(self):
        '''
        A sandboxed FifthRow should have a token of 'sandbox'
        regardless of token parameter.
        '''
        self.assertEqual(FifthRow(sandbox=True, token=5555).token, 'sandbox')

    def test_none_token(self):
        '''
        TokenError should be raised if token != an integer.
        '''
        self.assertRaises(TokenError, FifthRow, sandbox=False, token=None)

if __name__ == '__main__':
    unittest.main()
