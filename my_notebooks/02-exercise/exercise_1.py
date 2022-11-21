#1)
#Create a python file with 3 functions:
import csv
import argparse
#2)
#def print_file_content(file) that can print content of a csv file to the console
filename = "random.csv"

def print_file_content(file):
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
    

#3)
#def write_list_to_file(output_file, lst) that can take a list or tuple of strings and write each element to a new line in file 1. rewrite the function so that it gets an arbitrary number of strings instead of a list

output_filename = "file 1.csv"
myTuple = ("apple", "banana", "orange", "cookie", "rum")

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as csv_file:
        output_writer = csv.writer(csv_file)
        
        for element in lst:
            output_writer.writerow(element)
        
                
    
#4)
#def read_csv(input_file) that take a csv file and read each row into a list. Print the list.
myList = []
def read_csv(input_file):
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            myList.append(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that saves a name')
    parser.add_argument('ftools', type=str, help="enter a name/string/whatever", default="Arne")
    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True
    
    #subparser for print_file_content
    parser_print = subparsers.add_parser("print")
    #Add a required argument
    parser_print.add_argument('filename', help="write a csv filename to print!")
    
    #subparser for write_list_tofile
    parser_write = subparsers.add_parser("write")
    #Add a required argument
    parser_write.add_argument('output_filename', help="write where the csv file should be written")
    parser_write.add_argument('tuple', type=tuple, help="write a tuple here, t = (?,?,? etc)")
    
    #subparser for read_csv
    parser_read = subparsers.add_parser("read")
    #Add a required argument
    parser_read.add_argument("read_filename", help="write the csv file u want me to read")
    
    args = parser.parse_args()
    print(args)
    if args.subcommand == 'print':
        print("- - - - - -")
        print("exercise 1")
        print (f"I will now print this file: {args.filename}")
        print_file_content(args.filename)
    if args.subcommand == 'write':
        print("- - - - - -")    
        print("exercise 2")
        print(f"I will now write this tuple: {args.tuple} to this file: {args.output_filename}")
        write_list_to_file(args.output_filename, args.tuple)
    if args.subcommand == 'read':
        print("- - - - - -")
        print("exercise 3")
        print(f"I will now read this csv file to you: {args.read_filename}")
        read_csv(args.read_filename)
        print(myList)
    
    
    