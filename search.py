import pickle
import csv


def searchf(filename):
    m = filename[:-4]
    try:
        if m.isalnum():  # FILE NAME SHOULB IN STRING FORMAT
            if filename[-4:] == ".bat":  # FOR BINARY FILE SEARCHING
                mode = "rb"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = pickle.load(f)
                    n = input("Enter RollNo : ")+" "
                    s = []
                    for i in k:
                        if i[1] == n:
                            v = 1
                            s.append(i)
                            break
                        else:
                            v = 0
                    if v == 1:
                        print(s)
                    else:
                        print("Data Not Found..")
                    f.close()
                except:
                    # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                    print("File Not Found")
            elif filename[-4:] == ".txt":  # FOR TEXT FILE READING
                mode = "r"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = f.readlines()
                    n = input("Enter Roll Number : ")
                    s = []
                    for i in k:
                        t = i.split(" ")
                        if t[1] == n:
                            s.append(i)
                            v = 1
                            break
                        else:
                            v = 0
                    if v == 1:
                        print(s)
                    else:
                        print("Data Not Found...")
                    f.close()
                except:
                    # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                    print("File Not Found")
            elif filename[-4:] == ".csv":  # FOR CSV FILE READING
                try:
                    mode = "r"
                    f = open(f"{filename}", f"{mode}")
                    k = csv.reader(f)
                    n = input("Enter Roll no : ")+" "
                    s = []
                    j = 0
                    print("Srno\tName\t rollno\t Marks")
                    for i in k:
                        j += 1
                        if i[1] == n:
                            s.append(i)
                            v = 1
                            break
                        else:
                            v = 0
                    if v == 1:
                        print(j, "\t", s[0][0], "\t", s[0][1], "\t", s[0][2])
                    else:
                        print("Data Not Found")
                    f.close()
                except:
                    # IF FILE NOT PRESENT IT SHOWAS AN ERROR
                    print("File Not Found")
            else:
                # IF OTHER EXTENSION ENTERED IT SHOWS INVALID EXTENSION
                print("Invalid Extension !!!")
    except:
        # IF ANYTHING IS ENTERED IT SHOWS AN ERROR...
        print("Please Enter Filename in form of string with a Valid Extension.")


print("OUTPUT FOR CSV FILE :")
# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory)
searchf("test.csv")
print("OUTPUT FOR TXT FILE :")
# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory)
searchf("test.txt")
print("OUTPUT FOR BINARY FILE :")
# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory)
searchf("test.bat")
