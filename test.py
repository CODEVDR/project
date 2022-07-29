import pickle
import csv


def readf(filename):
    m = filename[:-4]
    try:
        if m.isalnum():
            if filename[-4:] == ".bat":
                mode = "rb"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = pickle.load(f)
                    print(k)
                    f.close()
                except:
                    print("File Not Found")
            elif filename[-4:] == ".txt":
                mode = "r"
                try:
                    f = open(f"{filename}", f"{mode}")
                    k = f.read()
                    print(k)
                    f.close()
                except:
                    print("File Not Found")
            elif filename[-4:] == ".csv":
                mode = "r"
                f = open(f"{filename}", f"{mode}")
                k = csv.reader(f)
                for i in k:
                    print(i)
            else:
                print("Invalid Extension !!!")
    except:
        print("Please Enter Filename in form of string with a Valid Extension.")


readf("test.csv")
"""f=open(f"test.bat",f"wb")
l=["hii i am a programmer"]
k=pickle.dump(l,f)
f.close()"""
