"""
    Gnome Sort
    ----------
    A sorting algorithm similar to insertion sort except that the element is
    moved to its proper place by a series of swaps.

    Time Complexity: O(n**2)

    Space Complexity: O(1) auxillary

    Stable: No

    Psuedo code: http://en.wikipedia.org/wiki/Gnome_sort

"""


def sort(a):
        i, j, size = 1, 2, len(a)
        while i < size:
            if a[i - 1] <= a[i]:
                i, j = j, j + 1
            else:
                a[i - 1], a[i] = a[i], a[i - 1]
                i -= 1
                if i == 0:
                    i, j = j, j + 1
        return a

