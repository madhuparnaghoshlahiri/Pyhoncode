try:
    x=open("D:\Anudip\Data.txt",'a')
    print(x)
    x.write("Anudip Python Content")
    x.write(str(25))
    x.write("\n")
    x.write("ABC KOLKATA")
    print("File Created Successfully")
    x.close()
except FileNotFoundError:
    print("File not Present")
