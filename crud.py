import mysql.connector as mysql
x = mysql.connect(host="localhost", user="root", password="", database="students")
cur = x.cursor()
ans = "y"
while True:
    ch = int(input("CRUD Operation: \n1. C-Insert Data \n2. R-Display Data \n3. U-Update Data \n4. Delete Data \n"))
    if ch == 1:
        more = "y"
        while more == "y" or more == "Y":
            id = int(input("Enter the Employee ID: \n"))
            Ename =input("Enter the Employee Name: \n")
            cur.execute("insert into school values({}, '{}')".format(id, Ename))
            x.commit()
            print("Data successfully inserted")
    # if ch == 2:
    #     cur.execute("Select * from school")
    #     data = cur.fetchall()
    #     for i in data:
    #         print(i)
    
    if ch == 2:
        id = int(input("Enter the Employee ID: \n"))
        cur.execute("Select Ename from school where id = '104'")
        data = cur.fetchone()
        print(data)
    if ch == 3:
        update_ch = input("What do you want to Update: \nA. Employee Id \nB. Employee Name \n")
        if update_ch == "A" or update_ch == "a":
            id_old = int(input("Enter the existing Employee ID: \n"))
            id_new = int(input("Enter the new Employee ID: \n"))
            cur.execute("UPDATE user SET id={}, WHERE id='{}'".format(id_old, id_new))
            x.commit()
            print("Data updated Successfully")
        if update_ch == "B" or update_ch == "b":
            id = input("Enter the Employee id to be updated: \n")
            Ename = input("Enter the Employee new name: \n")
            cur.execute("UPDATE user SET Ename={}, WHERE id={} ".format(Ename, id))
            x.commit()
            print("Data updated Successfully")
        if ch == 4:
            delete_ch = input("press \nA. Delete entire Data \nB. Delete selected Data")
            if delete_ch == "A" or delete_ch == "a":
                cur.execute("DELETE FROM student")
                x.commit()
                print("The entire Data has been deleted")
            if delete_ch == "B" or delete_ch == "b":
                id = int(input("Enter the id of the Employee you want to delete: \n"))
                cur.execute("DELETE FROM student WHERE id={}".format(id))
                x.commit()
                print("User Deleted Successfully")
        ans = input("Run Again? (Y/N)")
        
            
        
            
                
    