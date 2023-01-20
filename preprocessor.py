"""
--------------------------------------------
Name: Aiden Teal
SID: 1724406
CCID: ateal
AnonID: 1000332190
CMPUT 274, Fall 2022
Assessment: Weekly Exercise #4: Text Preprocessor
--------------------------------------------
"""

import sys


# Global List
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
    ]


class Words:
    """ Class Words is used to define 4 functions not including __init__
    that can be used to preprocess the input coming into the program.
    By defining the functions here, they can be called, and reused
    throughout the program. The four functions revolve around making
    the text lowercase, removing punctuation/symbols,
    removing digits, and removing stop words. """

    def __init__(self, Words1, Stop_Words, mode):
        """ This function is used to initialize the objects and
        their given attributes. """
        self.Words1 = Words1
        self.Stop_Words = Stop_Words
        self.mode = mode

    def lowercase(self):
        """ This function converts all text to lowercase. """
        self.Words1 = self.Words1.lower()
        return self.Words1

    def remove_punctuation(self, punctuation="@!-$%&'()*+,./:;<=>?_[]^`{|}~"):
        """ This function, depending on the value of mode, will either
        remove all punctuation/symbols from the text or leave it. """
        if self.mode == '' or self.mode != "keep-symbols":
            for i in punctuation:
                while self.Words1.count(i) > 0:
                    self.Words1 = self.Words1.replace(i, "")
        return self.Words1

    def number_identifier(self, count=0, numbers="0123456789"):
        """ This function, depending on the value of mode, will either remove
        all digits from the text (unless the text it is preprocessing contains
        only digits) or leave it. """
        if self.mode == '' or self.mode != "keep-digits":
            for i in numbers:
                if self.Words1.count(i) > 0:
                    count += 1
                elif count == len(self.Words1):
                    self.Words1 = self.Words1
            for i in numbers:
                if self.Words1.count(i) > 0 and count != len(self.Words1):
                    self.Words1 = self.Words1.replace(i, "")
                    count -= 1
        return self.Words1

    def stop_words(self):
        """ This function, depending on the value of mode, will remove any text
        that matches the stop words listed at the top of the program. """
        if self.mode == '' or self.mode != "keep-stops":
            for i in self.Stop_Words:
                if self.Words1.count(i) > 0 and len(i) == len(self.Words1):
                    self.Words1 = self.Words1.replace(i, "")
        return self.Words1


def error_checking(Argument):
    """ This function takes in an argument, and depending on
    what the user inputs into the command-line, will either allow
    the program to function, or print an error message letting
    the user know that what they inputed is not allowed, while
    giving them a brief description of what is allowed. This function
    is created so that the code can run without issues. """
    error_count = 0
    if len(Argument) == 1:
        return Argument
    mode = Argument[1]
    if len(Argument) > 1 and mode == "keep-digits":
        error_count += 1
    elif len(Argument) > 1 and mode == "keep-symbols":
        error_count += 1
    elif len(Argument) > 1 and mode == "keep-stops":
        error_count += 1
    if error_count == 0:
        print("Mode defined is not accepted. " +
              "Usage: python3 preprocess.py <mode>:\n<mode>" +
              " should be keep-digits or " + "keep-stops or keep-symbols")
        sys.exit(1)


def string_manipulate(Argument):
    """ String manipulate takes in an argument(Argument)
    and depending on the value of Argument, will process
    the giving input using calls to the class Words. """
    words = str(input().strip())
    Words1 = list(words.split())
    list2 = []
    i = 1
    while i <= len(Words1):
        if len(Argument) == 1:
            # If no optional input mode is given, it will set mode = ''
            Words2 = Words(Words1[i-1], Stop_Words, mode='')
        else:
            # Else, defines mode as the optional command argument given.
            Words2 = Words(Words1[i-1], Stop_Words, mode=Argument[1])
        Words3 = Words2.lowercase()
        Words3 = Words2.remove_punctuation()
        Words3 = Words2.number_identifier()
        Words3 = Words2.stop_words()
        if Words3 == "":
            list2 = list2
        elif Words3 != "":
            list2.append(Words3)
        i += 1
    # After all text is processed from the input, it will output the
    # preprocessed text as a space-seperated string.
    print(*list2)


if __name__ == "__main__":
    error_checking(sys.argv)
    string_manipulate(sys.argv)
    pass
