import pickle
import csv

def writef(filename,list):
    m = filename[:-4]
    try:
        if m.isalnum():#FILE NAME SHOULB IN STRING FORMAT
            if filename[-4:] == ".bat":#FOR BINARY FILE READING
                mode = "wb"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = pickle.dump(list,f)
                    f.close()
                    print("Sucessfully Written Data in bindary file")
                except:
                    print("File Not Found")#IF FILE NOT PRESENT IT SHOWAS AN ERROR
            elif filename[-4:] == ".txt":#FOR TEXT FILE READING
                mode = "w"
                try:
                    f = open(f"{filename}", f"{mode}")
                    for i in list:
                        f.writelines(i)
                    f.close()
                    print("Sucessfully Written Data in text file")
                except:
                    print("File Not Found")#IF FILE NOT PRESENT IT SHOWAS AN ERROR
            elif filename[-4:] == ".csv":#FOR CSV FILE READING
                try:   
                    mode = "w"
                    f = open(f"{filename}", f"{mode}", newline='')
                    k = csv.writer(f)
                    k.writerows(list)
                    f.close()
                    print("Sucessfully Written Data in csv file")
                except:
                    print("File Not Found")#IF FILE NOT PRESENT IT SHOWAS AN ERROR
            else:
                print("Invalid Extension !!!")#IF OTHER EXTENSION ENTERED IT SHOWS INVALID EXTENSION
    except:
        print("Please Enter Filename in form of string with a Valid Extension.")#IF ANYTHING IS ENTERED IT SHOWS AN ERROR...
l=[["mita ","1 ","99 "],["gita ","2 ","90 "]]
writef("test.csv",l)# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory if not present the files automatically created.)
writef("test.txt",l)# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory if not present the files automatically created.)
writef("test.bat",l)# FUNCTION CALL (test.csv,test.txt,test.bat already created in directory if not present the files automatically created.)