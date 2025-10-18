s=set()
s.add("14")
s.add(14)
s.add(14.0)
print(s)
print(14==14.0)
print(14=="14")
# # Because Python compares numeric types by value: an
# int and a float are considered equal if their
# numeric values are the same, so 14 == 14.0 is True.