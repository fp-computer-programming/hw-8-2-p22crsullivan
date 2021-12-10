# Author: CRS 12/09/21
def letter_in_word(word, letter):
    amount = 0
    for x in word:
        if x == letter:
            amount += 1
    return amount


print(letter_in_word("cat", "t") == 1)
print(letter_in_word("apple", "p") == 2)
print(letter_in_word("supercalifragilisticexpialidocious", "i") == 7)