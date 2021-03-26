fn = input("Filename? ")
try:
    infile = open(fn, "r")
    s = infile.read()
    print("File size =", len(s))
    infile.close()
except FileNotFoundError as e: #errors and exceptions
    print("The file", fn, "does not exist.")

def listFiles():
    from os import listdir
    dirList = listdir(".") #返回指定文件夾包含的文件或文件夾的名字的列表(一般不包含 "." 和 ".." , 這裡剛好是指定 ".")
    return dirList
def main():
    for fn in listFiles():
        print(fn)
main()