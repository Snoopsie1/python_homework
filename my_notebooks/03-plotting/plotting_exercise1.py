import matplotlib.pyplot as plt

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}
days = list(student_attendance.keys())
attendance = list(student_attendance.values())

print(attendance)
plt.figure()
plt.plot(attendance, linewidth=5)
# Set chart title and label axes.
plt.title("Student Attendance", fontsize=24)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Attendance", fontsize=7)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
print("Hvor er min graf lol")
plt.show()
print("Der var den:>")
