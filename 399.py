"""Problem
This problem was asked by Facebook.

Given a list of strictly positive integers, partition the list into 3 contiguous partitions which each sum up to the same value. If not possible, return null.

For example, given the following list:

[3, 5, 8, 0, 8]
Return the following 3 partitions:

[[3, 5],
 [8, 0],
 [8]]
Which each add up to 8.

Solution
First off, notice that the sum of all the elements must be divisible by 3 for us to be able to partition it into 3 equal pieces. So we can immediately check whether the sum of the array is divisible by 3 and return null if it isn't, as a sanity check.

Next, to actually find the partition bounds, we can iterate over the array with a temporary sum variable, keeping track of whenever it reaches sum(arr) / 3. When it does, we can set our first or second bound to the current index we're on."""
def partition(arr):
    if sum(arr) % 3 != 0:
        return None

    j = None
    k = None
    current_sum = 0
    for i, num in enumerate(arr):
        if current_sum == sum(arr) / 3:
            current_sum = 0
            if j is None:
                j = i
            elif k is None:
                k = i
        current_sum += num

    if j is None or k is None:
        return None

    return [arr[:j], arr[j:k], arr[k:]]
"""This runs in O(N) time and O(1) space, since we just have a few temporary variables and we loop over the array once."""
