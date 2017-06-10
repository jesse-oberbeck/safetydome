#!/usr/bin/env python3

import mysql.connector
import getpass


def getcon(verbose=False):
    # Connects to the database.
    try:
        login_name = getpass.getuser()
        config = {"user": login_name, "database": login_name}
        connection = mysql.connector.connect(**config)
        if verbose:
            print("Connecting with configuration:", config, sep='\n')
            print("Using", type(connection))
        return connection
    except:
        print("Connection Error.")


def populate():
    # Fills in the html portion sourced from the database.
    connection = getcon()
    sql = "SELECT * FROM fight"
    cursor = connection.cursor()
    cursor.execute(sql)
    print("<table border='1'>")
    for record in cursor.fetchall():
        print("<tr>", "<td>", "<a href='fightdetail.py?vs=" + str(record[0]) +
              "v" + str(record[1]), "'>", str(record[0]) + " VS " +
              str(record[1]), "</a>", "</td>", "</tr>", "\n", end = " ")
    return connection
    return connection


print("Content-type: text/html\n")
print("<html><head><title>Combatant List</title></head>")
print("<body>")
print("<a href='../index.html'>Home</a>")
print("<h1>Battle List</h1>")

con = populate()
con.close()
print("</body></html>")
