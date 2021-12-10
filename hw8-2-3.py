# Author: CRS 12/09/21
def three_letter_words(lst):
    letter_words = 0
    for x in lst:
        if len(x) == 3:
            letter_words += 1
            return letter_words


three_letter_words(["cat", "bat", "apple"]) == 2
three_letter_words(["apple", "hippo", "mouse"]) == 0
three_letter_words(["hop", "pop", "bop"]) == 3