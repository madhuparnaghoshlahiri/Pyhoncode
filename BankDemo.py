import mysql.connector as  mc
def openAcc():
    try:
        con=mc.connect(host="localhost",\
                       username="root",database="bank",password="rkit2022")
        name=input("Enter Your Name")
        acno=input("Enter Accountno")
        dob=input("Enter Your D.O.B")
        phno=input("Enter Your Phoneno")
        address=input("Enter Your Address")
        ob=int(input("Enter Opening Balance"))
        query1="insert into account(name,acno,dob,ad,phn,ob)\
        values('{0}','{1}','{2}','{3}','{4}',{5})".format(name,acno,dob,address,phno,ob)
        query2="insert into amount(name,acno,balance)\
        values('{0}','{1}',{2})".format(name,acno,ob)
         
        c=con.cursor()
        c.execute(query1)
        c.execute(query2)
        con.commit()
        print("Data Saved Successfully")
        main()
       
    except:
        con.rollback()
        print("Error Found")
def deposit():
    con=mc.connect(host="localhost",\

                       username="root",database="bank",password="rkit2022")
    am=int(input("Enter Amount"))
    ac=input("Enter Accountno")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("Deposited amount Successfully")
    main()
def withdrawl():
    con=mc.connect(host="localhost",\
                       username="root",database="bank",password="rkit2022")    
    ac=input("Enter Accountno")
    am=int(input("Enter Amount"))
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("Withdrawled Successfully")
    main()
def balance():
    con=mc.connect(host="localhost",\
                       username="root",database="bank",password="rkit2022")
    ac=input("Enter Accountno")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("BALANCE of the account ::",ac," is ",myresult[0]) 
    main() 
    
def displayAc():
    con=mc.connect(host="localhost",\
                       username="root",database="bank",password="rkit2022")
    ac=input("Enter Accountno")
    a="select * from account where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("RECORD OF CUSTOMER")
    for i in myresult:
        print(i,end=" ")
    con.close()
    main()

def closeAc():
    con=mc.connect(host="localhost",\
                       username="root",database="bank",password="rkit2022")
    ac=input("Enter Accountno")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    print("Account deleted Successfully")
    main()  

def main():
    print("1. OPEN NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAWL AMOUNT")
    print("4. BALANCE ENQUIRY")
    print("5. DISPLAY CUSTOMER DETAILS")
    print("6. CLOSE ACCOUNT")
    
    op=int(input("Select Any Option"))
    if op==1:
        openAcc()
    elif op==2:
        deposit()
    elif op==3:
        withdrawl()
    elif op==4:
        balance()
    elif op==5:
       displayAc()
    elif op==6:
        closeAc()
    else:
        print("WRONG CHOICE")

while True:
    main()
