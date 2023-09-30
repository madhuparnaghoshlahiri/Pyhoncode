from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://d4dipdas:anudip1234@anudip.az1cx5y.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db=client['Test']
table=db['user']
def add():
    id=int(input("Enter Your Id"))
    name=input("Enter Your Name")
    age=int(input("Enter Your Age"))
    add=input("Enter Your Address")
    data={"_id":id,"name":name,"age":age,"add":add}
    table.insert_one(data)
    print("Data Saved Success")
def display():
    for i in table.find({}):
        print(i)

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
