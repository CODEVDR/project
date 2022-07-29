import pickle
import csv


def readf(filename):
    m = filename[:-4]
    try:
        if m.isalnum():#FILE NAME SHOULB IN STRING FORMAT
            if filename[-4:] == ".bat":#FOR BINARY FILE READING
                mode = "rb"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = pickle.load(f)
                    for i in k:print(i)
                    f.close()
                except:
                    print("File Not Found")#IF FILE NOT PRESENT IT SHOWAS AN ERROR
            elif filename[-4:] == ".txt":#FOR TEXT FILE READING
                mode = "r"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = f.read()
                    print(k)
                    f.close()
                except:
                    print("File Not Found")#IF FILE NOT PRESENT IT SHOWAS AN ERROR
            elif filename[-4:] == ".csv":#FOR CSV FILE READING
                try:   
                    mode = "r"
                    f = open(f"{filename}", f"{mode}")
                    k = csv.reader(f)
                    j = 0
                    print("Srno\tName\t rollno\t Marks")
                    for i in k:
                        j += 1
                        print(j, "\t", i[0], "\t", i[1], "\t", i[2])
                    f.close()
                except:
                    print("File Not Found")#IF FILE NOT PRESENT IT SHOWAS AN ERROR
            else:
                print("Invalid Extension !!!")#IF OTHER EXTENSION ENTERED IT SHOWS INVALID EXTENSION
    except:
        print("Please Enter Filename in form of string with a Valid Extension.")#IF ANYTHING IS ENTERED IT SHOWS AN ERROR...
print("OUTPUT FOR CSV FILE :")
readf("test.csv")# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory)
print("OUTPUT FOR TXT FILE :")
readf("test.txt")# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory)
print("OUTPUT FOR BINARY FILE :")
readf("test.bat")# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory)

