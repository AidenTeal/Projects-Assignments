"""
Name: Aiden Teal
SID: 1724406
CCID: ateal
AnonID: 1000332190
CMPUT 274, Fall 2022

Assessment: Weekly Exercise #3: Word_Frequency

"""

import sys
from collections import OrderedDict

file_check = sys.argv
dict_of_words = {}
total_word_count = 0


def error_checking(file_check):

    """ This piece of code serves as an error check in the chance
    a user inputs two command-line inputs as that would cause
    issues for the program """

    if len(sys.argv) > 2:
        print("Too many arguments. Usage: python3 freq.py <input file name>")
        exit()


if file_check[0] is not None:

    """ Using the open function, if a command line input is given after
    the file name, it will rearragne the text file given and organize
    all the words within the file into a dictionary. Also serves as
    an error check incase no command-line input is given with the file. """

    try:
        with open(sys.argv[1]) as i:
            while True:
                line = i.readline()
                if not line:
                    break
                for w in line.split():
                    if w not in dict_of_words:
                        dict_of_words[w] = 1
                        total_word_count += 1
                    elif w in dict_of_words:
                        dict_of_words[w] += 1
                        total_word_count += 1
                dict1_of_words = OrderedDict(sorted(dict_of_words.items()))
    except IndexError:
        print("Too few arguments. Usage: python3 freq.py <input file name>")
        exit()


with open(sys.argv[1] + ".out", 'w') as o:

    """ Creates an output file with writing properties (using the open
    function), and writes a histogram of all the words from the input file
    into it, including the count and frequency of each word. After every key
    in the dictionary, it produces a new line so that each key
    is written on its own line. """

    for words in dict1_of_words:
        o.write(words + " " + str(dict1_of_words[words]) + " " +
                str(round(dict1_of_words[words] / total_word_count, 3)))
        o.write('\n')
    o.close()


if __name__ == "__main__":
    error_checking(sys.argv)
    pass