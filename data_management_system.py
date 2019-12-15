import os
import sys
import logo
import logo1
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="123456",
    database="mydatabase"
    )

mycursor = mydb.cursor()
print(logo.logo)
choice = 1
while choice != 5:
    try:
        choice = int(input("Enter your Choice. ").strip())
        if choice in range(1,5):
            if choice == 1:
                choice = input("Choose table that you want to upload data to: ").strip().lower()
                if choice == "customer":
                   c_name  = input("Enter Customer's name. ").strip().lower()
                   c_bal   = int(input("Enter Customer's balance. ").strip())
                   c_stat  = input("Enter Customer's status. ").strip().lower()
                   c_add   = input("Enter Customer's address. ").strip().lower()
                   c_email = input("Enter Customer's email address. ").strip().lower()
                   sql = "insert into customer(cust_name,cust_balance,cust_status,cust_address,cust_email)\
                          values(%s,%s,%s,%s,%s)"
                   val = (c_name,c_bal,c_stat,c_add,c_email)
                   mycursor.execute(sql,val)
                   mydb.commit()
                   if mycursor.rowcount == 1:
                       print("Record inserted, TABLE UPDATED SUCCESSFULLY.")
                   else:
                       print("Record not inserted, PLEASE CONTACT SUPPORT")
                else:
                    print("This database does not exist")
                    print("Exiting application")
                    break
            elif choice == 2:
                choice = input("Enter value by which you want to search records.\n\
Enter I to search by customer id \n\
Enter N to search by customer name\n\
Enter B to search by customer balance\n\
Enter A to search by customer address \n\
Enter E to search by customer email  \n\
").strip().lower()
                if choice == "i":
                    choice = int(input("Enter Customer's Id. ").strip())
                    sql = ("select * from customer where cust_id = %s")
                    val = (choice,)
                    mycursor.execute(sql,val)
                    if mycursor.rowcount == True:
                        print("No customer exists with Customer Id = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "n":
                    choice = input("Enter Customer's Name. ").strip().lower()
                    sql = ("select * from customer where cust_name = %s")
                    val = (choice,)
                    mycursor.execute(sql,val)
                    if mycursor.rowcount == True:
                        print("No Customer exists with Name = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "b":
                    choice = int(input("Enter Customer's Balance. ").strip())
                    sql = ("select * from customer where cust_balance = %s")
                    val = (choice,)
                    mycursor.execute(sql,val)
                    if mycursor.rowcount == True:
                        print("No Customer exists with balance = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "a":
                    choice = input("Enter Customer's Address. ").strip()
                    sql = ("select * from customer where cust_address = %s")
                    val = (choice,)
                    mycursor.execute(sql,val)
                    if mycursor.rowcount == True:
                        print("No Customer exists with address = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "e":
                    choice = input("Enter Customer's email. ").strip()
                    sql = ("select * from customer where cust_email = %s")
                    val = (choice,)
                    mycursor.execute(sql,val)
                    if mycursor.rowcount == True:
                        print("No Customer exists with email = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                else:
                    print("Incorrect choice")
            elif choice == 3:
                choice = input("Enter value by which you want to search records.\n\
Enter N to search by customer name\n\
Enter B to search by customer balance\n\
Enter A to search by customer address \n\
Enter E to search by customer email  \n\
").strip().lower()
                if choice == "n":
                    choice = input("Enter Customer's Name. ").strip().lower()
                    sql = ("select * from customer where cust_name like \'%"+ choice + "%\' ")
                    mycursor.execute(sql)
                    if mycursor.rowcount == True:
                        print("No Customer exists with Name = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "b":
                    choice = input("Enter Customer's Balance. ").strip()
                    sql = ("select * from customer where cust_balance like \'%"+ choice + "%\' ")
                    mycursor.execute(sql)
                    if mycursor.rowcount == True:
                        print("No Customer exists with balance = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "a":
                    choice = input("Enter Customer's Address. ").strip()
                    sql = ("select * from customer where cust_address like \'%"+ choice + "%\' ")
                    mycursor.execute(sql)
                    if mycursor.rowcount == True:
                        print("No Customer exists with address = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                elif choice == "e":
                    choice = input("Enter Customer's email. ").strip()
                    sql = ("select * from customer where cust_email like \'%"+ choice + "%\' ")
                    mycursor.execute(sql)
                    if mycursor.rowcount == True:
                        print("No Customer exists with email = {}".format(choice))
                    else:
                        result = mycursor.fetchall()
                        for r in result:
                            print(r)
                else:
                    print("Incorrect choice")
            elif choice == 4:
                sql = ("select * from customer")
                mycursor.execute(sql)
                result = mycursor.fetchall()
                with open ('customer.txt','w') as wf:
                    wf.write("-----------------------------------------------------------------------------------------------------------------------------------\n")
                    wf.write("| Cust_Id |     Cust_name        | Cust_balance  | Cust_status  |        Cust_address            |        Cust_email              |\n")
                    wf.write("-----------------------------------------------------------------------------------------------------------------------------------")
                    for item in result:
                        wf.write("\n")
                        count = 0
                        for i in item:
                            if count == 0:
                                j = "        "+str(i)
                                if len(j) > 8:
                                    k = j[-7:]
                                    k = "|"+k+"  |"
                                    count = count+1
                                    wf.write(k)
                            elif count == 1:
                                j = "                    "+str(i)
                                if len(j) > 20:
                                    k = j[-20:]
                                    k = k+"  |"
                                    count = count+1
                                    wf.write(k)
                            elif count == 2:
                                j = "             "+str(i)
                                if len(j) > 13:
                                    k = j[-13:]
                                    k = k+"  |"
                                    count = count+1
                                    wf.write(k)
                            elif count == 3:
                                j = "            "+str(i)
                                if len(j) > 12:
                                    k = j[-12:]
                                    k = k+"  |"
                                    count = count+1
                                    wf.write(k)
                            elif count == 4:
                                j = "                              "+str(i)
                                if len(j) > 30:
                                    k = j[-30:]
                                    k = k+"  |"
                                    count = count+1
                                    wf.write(k)
                            elif count == 5:
                                j = "                         "+str(i)
                                if len(j) > 30:
                                    k = j[-30:]
                                    k = k+"  |"
                                    count = count+1
                                    wf.write(k)
                    wf.write("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
                    print("File created")
            elif choice == 5:
                print("Thanks for using DataManSys, see you soon, GOODBYE")
                sys.exit()
                break
        else:
            print("Choice not valid !!! exiting program!!!")
    except ValueError:
        print("please enter a valid choice")

