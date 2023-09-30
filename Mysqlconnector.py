import mysql.connector as  mc
def add():
    try:
        con=mc.connect(host="localhost",\
                       username="root",database="boot",password="")
        name=input("Enter Your Name")
        age=int(input("Enter Your Age"))
        add=input("Enter Your Address")
        query="insert into user(name,age,addres)\
        values('{0}',{1},'{2}')".format(name,age,add)
        c=con.cursor()
        c.execute(query)
        con.commit()
        print("Data Saved Success")
        con.close()
    except:
        con.rollback()
        print("Error Found")
def display():
    con=mc.connect(host="localhost",\

                       username="root",database="boot",password="")
    query="select * from user"
    c=con.cursor()
    c.execute(query)
    for i in c.fetchall():
        print(i)
    con.close()

def main():
    print("1. For Insert record")
    print("2. For Display All Record")
    print("3. For Quit")
    op=int(input("Select Any Option"))
    if op==1:
        add()
    elif op==2:
        display()
    elif op==3:
        exit()
    else:
        print("Invalid Options")

while True:
    main()
