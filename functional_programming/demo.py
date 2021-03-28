"""
Advantages of Functional programming:
- Modularity: Writing functionally forces a certain degree of separation in solving your problems
  and eases reuse in other contexts.

- Brevity: Functional programming is often less verbose than other paradigms.

- Concurrency: Purely functional functions are thread-safe and can run concurrently.
  While it is not yet the case in Python, some functional languages do this automatically,
  which can be a big help if you ever need to scale your application.

- Testability: It is a simple matter to test a functional program, in that, all you need is
  a set of inputs and an expected set of outputs. They are idempotent.

See https://github.com/Joseph-H/some-py/blob/master/functional_demo.py and
https://github.com/Joseph-H/some-py/blob/master/itertools_demo.py
"""


def butlast(mylist):
    """Like butlast in Lisp; returns the list without the last element."""
    return mylist[:-1]  # This returns a copy of mylist


def remove_last_item(mylist):
    """Removes the last item from a list"""
    mylist.pop(-1)  # This modifies mylist


list = ['A', 'B', 'C']

# This function returns the modified copy of the list
new_list = butlast(list)

# Printing the modified copy returned by the function
print(new_list)
print(list)  # The original list is not modified

# This function modifies the list passed to it
remove_last_item(list)

# Printing the list after it is modified
print(list)
