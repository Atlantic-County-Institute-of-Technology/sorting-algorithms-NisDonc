# Nisdalie doncell 10/1/25
# import random


def bubble_sort(values):
    sort_act = 0
    sort_loop = 0
    # perform the bubblesort
    for i in range(len(values) - 1):
        sort_loop += 1
        # assume the final value in each pass is sorted
        for j in range(len(values) - i - 1):
            sort_loop += 1
            # perform the swap using a temp variable
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                sort_act += 1
    return values, sort_act, sort_loop
