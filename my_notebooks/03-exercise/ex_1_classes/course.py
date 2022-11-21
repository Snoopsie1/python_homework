class Course:
    """Each course has a name, ETCs and optional grade if course is taken"""

    def __init__(self, name, ETCs, grade=0):
        self.name = name
        self.ETCs = ETCs
        self.grade = grade

    def __repr__(self):
        return f"Course({self.name, self.ETCs, self.grade}"

    def __str__(self):
        return f"Course information: \n" \
               f"Name: {self.name} \n" \
               f"ETCs: {self.ETCs} \n" \
               f"Grade: {self.grade}"