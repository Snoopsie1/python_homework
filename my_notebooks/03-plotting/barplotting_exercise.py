import operator, matplotlib.pyplot as plt
some_people = {'Holger':25,'Helga':54,'Hasse':76,'Halvor':12,'Hassan':43,'Hulda':31,'Hansi':102}
print(some_people)
sorted_dict = dict(sorted(some_people.items(), key=operator.itemgetter(1)))
print(sorted_dict)

names = sorted_dict.keys()
ages = sorted_dict.values()
#Plotting time

plt.title("Age distribution between a handful of people")
plt.bar(names, ages, width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
plt.show()

