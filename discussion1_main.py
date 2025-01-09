"""Program to test class definitions for CS03B Discussion 1."""

from discussion1_CMC import Books

a = Books()
print(a)
b = Books()
print(b)
b.set_title("SpiderMan")
b.set_pages(28)
print(b)
c = Books("ABIN12345", "The Great Gatsby", 180)
print(c)
a.set_ID("ABIN12345")

print("test ID collision upon instantiation")
d = Books("ABIN12345", "Spider-Man", 180)

