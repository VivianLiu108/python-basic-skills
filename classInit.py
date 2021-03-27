class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def bmi(self):
        return self.weight / (self.height * self.height)
def main():
    aList = [ Person("Alice", 1.65, 48),
              Person("Bob", 1.9, 140),
              Person("Charlie", 1.75, 65)
            ]
    for p in aList:
        print(p.name, p.bmi())
main()





class Student:
    height = 190
    weight = 140

    def __init__(self, id=1, name="Daniel", sex="boy"):
        self.id = id
        self.name = name
        self.sex = sex

if __name__ == "__main__":
    s = Student(1, "Alice")
    s2 = Student(2, "Bob", "girl")
    s3 = Student(3)

    s.height = 165
    s.weight = 48

    print(s.id, s.name, s.sex, s.height, s.weight)
    print(s2.id, s2.name, s2.sex, s2.height, s2.weight)
    print(s3.id, s3.name, s3.sex, s3.height, s3.weight)

#1 Alice boy 165 48
#2 Bob girl 190 140
#3 Daniel boy 190 140
