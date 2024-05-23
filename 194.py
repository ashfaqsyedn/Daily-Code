"""Problem
This problem was asked by Facebook.

Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

Solution
We can try each possible line segment with each other, and keep track of which ones intersect. Two line segments intersect if their first x-values are on different sides than their second ones:"""


def intersects(l1, l2):
    # these lines intersect iff l1[0] > l2[0] and l1[1] > l2[1] or vice versa
    return (l1[0] < l2[0] and l1[1] > l2[1]) or \
           (l1[0] > l2[0] and l1[1] < l2[1])


def num_intersections(lst1, lst2):
    line_segments = list(zip(lst1, lst2))
    count = 0
    for i, l1 in enumerate(line_segments):
        for l2 in line_segments[i + 1:]:
            if intersects(l1, l2):
                count += 1
    return count

"""This runs in O(n2) time and constant space.

"""
