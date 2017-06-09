#!/usr/bin/env python3

import mysql.connector
import getpass

def getcon(verbose=False):
    login_name = getpass.getuser()
    config = {"user": login_name, "database": login_name}
    connection = mysql.connector.connect(**config)
    if verbose:
        print("Connecting with configuration:", config, sep='\n')
        print("Using", type(connection))
    return connection

def select():
    connection = getcon()
    sql = "SELECT * FROM players"
    cursor = connection.cursor()
    cursor.execute(sql)
    for index, record in enumerate(cursor.fetchall()):
        print ("<h4>", record,  "</h4>", end = " ")
    return connection



#connection = getcon(True)

#This begins the Body of hte HTTP Response
print("<html><head><title>A Basic Response</title></head>")
print("<body>")
print("<h1>Welcome</h1>")


con = select()
con.close()
print("</body></html>")
