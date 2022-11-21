import os


def get_file_names(folderpath,out="output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    with open(out, "w") as file_object:
        for file in os.listdir(folderpath):
            file_object.write(file + '\n') # '' > "" åbenbart. Ellers skriver den ikke newlines.
            print(file)

def get_all_file_names(folderpath,out="output.txt"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    #idk what or why i did this.
    #Bon apetit.
    
    # folder path
    dir_path = folderpath

    # list to store files name
    directories = []
    res = []
    for (dir_path, dir_names, file_names) in os.walk(dir_path):
        res.extend(file_names)
        directories.extend(dir_names)
    print(res)
    print(directories)
    
#    with open(out, "w") as file_object:
 #       for file in os.listdir(folderpath):
  #          file_object.write(file + '\n')
   #         print(file)
            
            

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in file_names:
        with open(file) as f:
            first_line = f.readline()
            print(first_line)

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file in file_names:
        with open(file) as file_object:
            for line in file_object:
                if '@' in line:
                    print(line)
                    
            

def write_headlines(md_files, out="output.txt"):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    headlines = []
    for md_file in md_files:
        with open(md_file, "r") as file_object:
            for line in file_object:
                if line.startswith("#"):
                    headlines.append(line)
                    
    with open(out, "w") as headwriters:
        for headline in headlines:
            headwriters.write(headline)
            
        
    
fileNames = ["filesToPrint/randomText1.txt", "filesToPrint/randomText2.txt", 
             "filesToPrint/randomText3.txt", "filesToPrint/randomText4.txt",
            "filesToPrint/randomText5.txt", "filesToPrint/randomText6.txt"]

md_files = ["filesToPrint/md_file1.md", "filesToPrint/md_file2.md",
            "filesToPrint/md_file3.md", "filesToPrint/md_file4.md"]
    
if __name__ == "__main__":
    #Task 1
    #get_file_names("../02-exercise")
    #Task 2
    #get_all_file_names("../02-exercise")
    #Task3
    #print_line_one(fileNames)
    #Task4
    #print_emails(fileNames)
    #Task5
    write_headlines(md_files)