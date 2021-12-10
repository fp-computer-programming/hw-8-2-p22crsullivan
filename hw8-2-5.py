# Author: CRS 12/09/21
def sum_till_odd(lst):
    number = 0
    for x in lst:
        if x % 2 != 0:
            break
        else:
            number += x
    return number


print(sum_till_odd([2, 4, 6, 8, 9]) == 20)
print(sum_till_odd([13, 12, 10]) == 0)
print(sum_till_odd([14, 16, 32]) == 62)