"""Problem
This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

Solution
In general, arranging objects of different weight into several containers optimally is known as a bin packing problem, and is NP-hard. This example is a special case, however.

A full rescue is impossible if there is a person who cannot fit in any boat, in which case we can return -1. Otherwise, we can solve this using a two pointer approach.

First, we sort each person by weight. If we look at each person in descending order, either that person must go alone, or it is possible for another passenger to join him or her. It might seem that we need to find an optimal partner, but in fact we can simply use the lightest remaining person. This is because anyone who can fit in a boat with the heaviest person will also be able to fit in a boat with any other person.

Suppose that we track the indices of the lightest and heaviest un-rescued people with the variables first and last respectively. For each boat used, then, one of two things will happen:

We increment first and decrement last, if the two can go together.
We only decrement last, if he or she must go alone.
Once the two indices cross, we will have transported all the people, at which point we can return the number of boats used."""
def boats(people, limit):
    people.sort()
    if people[-1] > limit:
        return -1

    num_boats = 0
    first, last = 0, len(people) - 1

    while first <= last:
        if people[first] + people[last] <= limit:
            first += 1; last -= 1; num_boats += 1
        else:
            last -= 1; num_boats += 1

    return num_boats

"""The running time of this algorithm is bounded by the time it takes to sort N people, which will be O(N log N)."""
