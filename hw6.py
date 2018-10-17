import re
import unittest

#BEFORE WRITING CODE, DO PSEUOCODE FIRST!!!

#WEDNESDAY sumNums COMPLETE ^-^'
#THURSDAY countWord
#FRIDAY-SUNDAY: listURLs

def sumNums(fileName):
    #open fileName
    """This function takes in a filename as input and returns a sum of

    the counted integers in the file. 
    """
    f = open(fileName, "r")
    txt = f.read()

    #create an emp list of numbers, in the form of a str
    list_sum = re.findall(r'\d+', txt)

    #convert to int
    list_s = [int(val) for val in list_sum]

    #Don't forget to close file, otherwise, u get a weird message
    f.close()
    return(sum(list_s))


def countWord(fileName, word):
    pass

def listURLs(fileName):
    pass


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),15)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
