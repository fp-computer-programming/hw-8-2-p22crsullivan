# Author: CRS 12/09/21
def count_odds(lst):
 num_odds = 0
 for x in lst:
    if x % 2 != 0:
        num_odds += x
 return num_odds


print(count_odds([1, 2, 3, 4, 5, 6]) == 9)
print(count_odds([1, 3, 5, 7, 9]) == 25)
print(count_odds([2, 4, 6, 8, 10]) == 0)