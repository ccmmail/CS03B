"""Program to test class definitions for CS03B Discussion 1."""

from discussion1_CMC import Books

a = Books()
print(a)
b = Books()
print(b)
c = Books("ABIN12345", "The Great Gatsby", 180)
print(c)
a.set_ID("123")
print(a)
b.set_ID("123")

