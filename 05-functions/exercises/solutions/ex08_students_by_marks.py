"""Exercise 8: sort, map and filter a list of (name, marks) tuples with lambdas."""

students = [("Aarav", 85), ("Sita", 92), ("Bikash", 67), ("Priya", 78), ("Kiran", 95)]

by_marks = sorted(students, key=lambda student: student[1], reverse=True)
print("Top 3:", by_marks[:3])

names = list(map(lambda student: student[0], students))
print("Names:", names)

above_80 = list(map(lambda student: student[0], filter(lambda student: student[1] > 80, students)))
print("Above 80:", above_80)
