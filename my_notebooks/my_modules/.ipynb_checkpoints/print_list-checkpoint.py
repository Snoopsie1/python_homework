# for use in exercise 1 in book 2-3 ( Modules )
# file 2.
import list_of_names as lon

names = lon.listOfNames();

def func():
    for name in names:
        print(name.title())

if __name__ == "__main__":
    func();