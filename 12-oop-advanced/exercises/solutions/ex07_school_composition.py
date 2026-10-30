"""School that contains Student and Teacher objects, with len(), iteration, counts and the oldest person."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"{super().__str__()}, grade {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()}, teaches {self.subject}"


class School:
    def __init__(self, name):
        self.name = name
        self.people = []                        # the School has-a list of people

    def add_person(self, person):
        self.people.append(person)

    def __len__(self):
        return len(self.people)

    def __iter__(self):
        return iter(self.people)

    def count(self, kind):
        return sum(1 for person in self.people if isinstance(person, kind))

    def oldest(self):
        return max(self.people, key=lambda person: person.age)


school = School("Sunrise School")
school.add_person(Student("Sita", 16, 10))
school.add_person(Teacher("Ramesh", 45, "Maths"))
school.add_person(Student("Aarav", 17, 11))
school.add_person(Teacher("Gita", 38, "Science"))
school.add_person(Student("Priya", 15, 9))

print(f"{school.name} has {len(school)} people:")
for person in school:
    print(" -", person)

print("Students:", school.count(Student))
print("Teachers:", school.count(Teacher))
print("Oldest:  ", school.oldest())
