/* This is a comment */

import mysql.connector as mdb

con = mdb.connect(
        host="localhost",
        user="root",
        passwd="Wiki@123",
        database="employees")
import os


###############################################################################################################################################################


def fetch_details():
    #con = mdb.connect( 'localhost', 'root', 'Wiki@123', 'mydatabase' )
    cur = con.cursor()
    cur.execute("SELECT emp_no, first_name, gender from employees_10")
    rows = cur.fetchall()
    emp_no = []
    first_name = []
    gender = []
    for row in rows:
        emp_no.append(row[0])
        first_name.append(row[1])
        gender.append(row[2])
        print emp_no
        print first_name
        print gender



    details =[x for x in zip(emp_no,first_name,gender)]
    return details
    
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)



###############################################################################################################################################################

def insert_details_into_table(details):

    query = "INSERT INTO employees10_duplicate(emp_no, first_name, gender) VALUES(%s,%s,%s)" 
    
    try:
        con = mdb.connect(
        host="localhost",
        user="root",
        passwd="Wiki@123",
        database="employees")
        
        cur = con.cursor()
        cur.executemany(query, details)
        con.commit()
        print "table_details inserted"
		
    except Error as error:
        print(error)

    finally:
        cur.close()
        con.close()

###############################################################################################################################################################


			
def main():
    details = fetch_details()                        	
    print details

    insert_details_into_table(details)


if __name__ == '__main__':
    main()

###############################################################################################################################################################
