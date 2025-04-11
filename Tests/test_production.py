'''
A file for tests for the production code.
'''
import unittest
from production import reverse_word
from production import reverse_all_words
import sys

#honestly pretty confused on where this is supposed to go or what it does--- come back 
sys.argv = ['production.py', 'this is a test'] #setting the command-line argument "this is a test"

from io import StringIO
sys.stdout = StringIO() #make a StringIO object and have sys.stdout point to it instead of the usual spot

printed_output = sys.stdout.getvalue() #I can get what is printed as a normal string!

class TestReverseWord(unittest.TestCase):

    def test_reverse_word(self):
        #test normal word 
        self.assertEqual(reverse_word("toby"), "ybot")
        #test empty 
        self.assertEqual(reverse_word(""), "")
        #test palindome
        self.assertEqual(reverse_word("mom"), "mom")
        # test single letter
        self.assertEqual(reverse_word("a"), "a")
        #test speacial char
        self.assertEqual(reverse_word("!@#$"), "$#@!")

    def test_reverse_all_words(self):
        #test normal phrase
        self.assertEqual(reverse_all_words("hello world"), "olleh dlrow")
        #test empty phrase
        self.assertEqual(reverse_all_words(""), "")
        #test single word
        self.assertEqual(reverse_all_words("hello"), "olleh")
        #test single letter 
        self.assertEqual(reverse_all_words("a"), "a")
        #test phrase with special char
        #self.assertEqual(reverse_all_words("hello! world!"), "olleh !dlrow")
        #test phrase with numbers
        self.assertEqual(reverse_all_words("123 456"), "321 654")

