a = ["apple", "banana", "cherry"]

print(a.index("dog"))


# import typing
# import numpy as np
#
#
#
# num_courses:int = int(input("how many course?"))
# course_roster_numpy = np.empty((num_courses), dtype=np.ndarray)
#
# print(course_roster_numpy)
#
# for k in range(num_courses):
#     num_students:int = int(input(f"how many students in course {k}?"))
#     course_roster_numpy[k] = np.array(num_students * ["(undefined)"], dtype=object)
#
# for row in range(course_roster_numpy.shape[0]):
#     for col in range(course_roster_numpy[row].size):
#         print(f"course {row}, student {col} is {course_roster_numpy[row, col]}")
#
# print(course_roster_numpy)