import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that saves a name')
    parser.add_argument('name', type=str, help="enter a name/string/whatever", default="Arne")
    args = parser.parse_args()
    print(args.name)
    