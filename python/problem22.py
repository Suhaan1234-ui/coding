s = {8, 7, 12, "Harry", [1,2]}
print(s)
# using list instead of tuple This will raise a TypeError
#  because lists are unhashable and cannot be added to a set.
#sets only accept hashable (immutable) items like numbers, strings, and tuples.