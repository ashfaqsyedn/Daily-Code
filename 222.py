"""Problem
This problem was asked by Quora.

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

Solution
We can keep track of the segments of the path using a stack.

First, we split the path by slashes. Going through the segments, if we see ., we will ignore it. If the segment is .., and our stack already has part of the path, we will pop the last part off the stack. In all other cases, we will add the new segment to the stack.

Since we are given an absolute path, the first element of the split list will always be an empty string. For this reason, checking whether our stack has part of the path is equivalent to checking that its length is greater than one.

Once we have traversed all the segments, we will join them together and return the result.

This solution is O(N) in the length of our input."""
def standardize(path):
    stack = []
    path = path.split("/")

    for segment in path:
        if segment == ".":
            continue
        elif segment == "..":
            if len(stack) > 1:
                stack.pop()
        else:
            stack.append(segment)

    return "/".join(stack)
