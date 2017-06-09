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

def populate():
    connection = getcon()
    sql = "SELECT * FROM combatant"
    cursor = connection.cursor()
    cursor.execute(sql)
    print ("<table border='1'>")
    for index, record in enumerate(cursor.fetchall()):
        print ("<tr>", "<td>", "<a href='combatant.py?id=" + str(record[0]), "'>", record[1],"</a>", "</td>", "</tr>", "\n", end = " ")
    return connection



#connection = getcon(True)
print("Content-type: text/html\n")
#This begins the Body of hte HTTP Response
print("<html><head><title>Combatant List</title></head>")
print("<body>")
print("<h1>Combatant List</h1>")


con = populate()
con.close()
print("</body></html>")
