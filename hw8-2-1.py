# Author: CRS 12/09/21
def count_odds(lst):
 num_odds = 0
 for num in lst:
    if num % 2 != 0:
        num_odds += 1
 return num_odds


print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)