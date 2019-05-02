"""
    Cocktail Sort
    -------------
    A bidirectional bubble sort. Walks the elements bidirectionally, swapping
    neighbors if one should come before/after the other.

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Cocktail_sort

"""


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    up = range(len(seq)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if seq[i] > seq[i+1]:
                    seq[i], seq[i+1] =  seq[i+1], seq[i]
                    swapped = True
            if not swapped:
                return


