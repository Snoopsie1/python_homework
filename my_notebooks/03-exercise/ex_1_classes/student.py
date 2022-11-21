import rand, random, data_sheet, course, csv
import matplotlib.pyplot as plt


class Student:
    """A student has a data sheet"""

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return f"Student({self.name}, {self.gender}, {self.data_sheet}, {self.image_url}"

    def __str__(self):
        return f"Student information: \n" \
               f"Name: {self.name} \n" \
               f"Gender: {self.gender} \n" \
               f"Data-Sheet: {self.data_sheet} \n" \
               f"Image: {self.image_url}"

    def get_average_grade(self):
        return sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())


def write_students_into_csv(student_list):
    header = ['name', 'gender', 'courses', 'avg grade', 'img_url']
    data = []

    for student in student_list:
        data.append([student.name, student.gender,
                     student.data_sheet.courses, student.get_average_grade(), student.image_url])

    # Writing to csv
    with open('randomStudents.csv', 'w', newline=None) as f:
        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerows(data)


def sort_students_by_avg_grade(students):
    return sorted(students, key=lambda x: float(x[3]))


def read_students_from_csv(filename="randomStudents.csv"):
    read_students = []

    with open(filename) as f:
        csv_reader = csv.reader(f)

        next(csv_reader)

        for line in csv_reader:
            read_students.append(line)

    return read_students


def generate_random_students(number_of_randoms):
    """Create a function that can generate n number of
    students with random: name, gender, courses (from a fixed list of course names), grades, img_url"""
    # Making students
    rand_students = []
    for i in range(number_of_randoms):
        students_courses = []
        # Gives student 5 courses
        for y in range(5):
            students_courses.append(
                course.Course(rand.courses[random.randint(0, len(rand.courses) - 1)].title(),
                              "ETC",
                              rand.grades[random.randint(0, len(rand.grades) - 1)])
            )

        students_datasheet = data_sheet.Data_Sheet(students_courses)

        rand_students.append(
            Student(rand.names[random.randint(0, len(rand.names) - 1)].title(),
                    rand.gender[random.randint(0, 1)],
                    students_datasheet,
                    rand.image_url)
        )

    return rand_students


def demo_generation():
    demo_courses = []
    for x in range(5):
        demo_courses.append(
            course.Course(rand.courses[random.randint(0, len(rand.courses) - 1)],
                          "ETC",
                          rand.grades[random.randint(0, len(rand.grades) - 1)])
        )

    demo_data_sheet = data_sheet.Data_Sheet(demo_courses)
    demo_student = Student(rand.names[random.randint(0, len(rand.names))].title(), "intet", demo_data_sheet,
                           rand.image_url)
    print(demo_student)


# For the first part of the exercise
# students = generate_random_students(8)
# write_students_into_csv(students)

# For the second part
read_students = read_students_from_csv()
grade_sorted_students = sort_students_by_avg_grade(read_students)
for student in grade_sorted_students:
    print(student[0])
    print(student[3])

# Graph part
bar_student_names = []
bar_student_avg_grade = []

for student in grade_sorted_students:
    bar_student_names.append(student[0])
    bar_student_avg_grade.append(student[3])

# Plotting time
plt.title("Average Grades Among Students")
plt.bar(bar_student_names, bar_student_avg_grade, width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
plt.show()
