class Data_Sheet:
    """A Data-Sheet has multiple courses in particular order"""

    def __init__(self, courses):
        self.courses = courses

    def __repr__(self):
        return f"Data_Sheet({self.courses}"

    def __str__(self):
        return f"Datasheet information: \n" \
               f"Courses : {self.courses}"

    def get_grades_as_list(self):
        # Wonder if this works...
        return [course.grade for course in self.courses]


