import mysql.connector

#  GETTING THE CONNECTION TO CONNECT TO DATABASE :

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythondb")
mycursor = mydb.cursor()


# ********************************** MY PHTHON CRUD APLLICATION ***********************************
class Crud:

    def Create_Employee(self):
        name = input("ENter the Table Name To Create :  ")
        query = "create table %s (eid int(11) , ename varchar(255) , erole varchar(255))"
        query = query % (name)
        mycursor.execute(query)

        for tb in mycursor:
            print(tb)

    # *********************************** DELETION USING PALCEHOLDERS ****************************************

    def Delete_Employee(self):
        query = " delete from employee where eid = %s"
        eid = input("Enter The Employee - Id To Delete : ")
        query = query % (eid)
        mycursor.execute(query)
        mydb.commit()

    # *********************************** INSERTION USING PALCE HOLDERS ****************************************

    def Insert_Employee(self):

        query = "insert into employee (eid , ename , erole)  values (%s , %s , %s)"
        print(query)
        a = input("ENter The Employee - Id : ")
        b = input("ENter The Employee - Name : ")
        c = input("ENter The Employee - Role : ")
        lat = (a, b, c)
        mycursor.execute(query, lat)
        mydb.commit()

    # *********************************** SELECT QUERY   USING PALCE HOLDERS ***********************************
    def Select_By_Id(self):

        query = "select * from employee where eid = %s "
        eid = int(input("Enter The EMployee - Id : "))
        query = query % (eid)
        print(query)
        mycursor.execute(query)
        res = mycursor.fetchall()
        for i in res:
            print(i)

    # *********************************** SELECT QUERY   USING PALCE HOLDERS ***********************************

    def update_employee(self):
        query = "update employee set eid = %s , ename = '%s' , erole ='%s' where eid = %s"
        oldid = int(input("Enter Employee id  to edit :"))
        newid = int(input("Enter The NEw Emp - Id : "))
        newaname = input("Enter The NEw Emp - Name : ")
        newrole = input("Enter The NEw Emp - Role : ")
        query = query % (newid, newaname, newrole, oldid)
        print(query)
        mycursor.execute(query)
        mydb.commit()


obj = Crud()
print("===>Create A New Table In DB   ")
obj.Create_Employee()
print("\n===>Get Employee Details With Id Number  ")
obj.Select_By_Id()
print("\n===>Insert A New  Employee Into DB  ")
obj.Insert_Employee()
print("\n===>Update EMployee Details  ")
obj.update_employee()
print("\n===>Delete Employee Record  ")
obj.Delete_Employee()
