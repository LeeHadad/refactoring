
"""
    strand_sort.py

    Implementation of strand sort on a list and returns a sorted list.

    Strand Sort Overview:
    ------------------------
    Repeatedly pulls sorted sublists out of the unsorted list and merges them
    with a result array.

    Time Complexity: O(n**2) worst case

    Space Complexity: O(1) auxiliary

    Stable: Yes

    Psuedo Code: https://en.wikipedia.org/wiki/Strand_sort
"""


def sort(array):
    def strand(a):
        i, s = 0, [a.pop(0)]
        while i < len(a):
            if a[i] > s[-1]:
                s.append(a.pop(i))
            else:
                i += 1
        return s

    def merge(left, right):
        out = []
        while len(left) and len(right):
            if left[0] < right[0]:
                out.append(left.pop(0))
            else:
                out.append(right.pop(0))
        out += left
        out += right
        return out

    out = strand(array)
    while len(array):
        out = merge(out, strand(array))
    return out


