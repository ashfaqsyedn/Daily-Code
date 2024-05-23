"""This problem was asked by Google.

What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?

Solution
The code will print out:

3
3
3
The issue here is that the variable i, used in print(i), is bound to the i outside of the function scope. Since it's a variable that gets updated in the for loop, it means that the last value the i takes on will get used in the print, which is 3.

To remedy this, we can capture the current state of i inside a closure, and pass the i in to that function:"""
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(var):
            def print_var():
                print(var)
            return print_var
        flist.append(print_i(i))

    return flist


functions = make_functions()
for f in functions:
    f()
