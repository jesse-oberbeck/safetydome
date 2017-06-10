#!/usr/bin/env python3

import mysql.connector
import getpass


def getcon(verbose=False):
    try:
        # Connects to the database.
        login_name = getpass.getuser()
        config = {"user": login_name, "database": login_name}
        connection = mysql.connector.connect(**config)
        if verbose:
            print("Connecting with configuration:", config, sep='\n')
            print("Using", type(connection))
        return connection
    except:
        print("Connection error.")


def populate():
    # Fills in the html portion sourced from the database.
    connection = getcon()
    sql = "SELECT * FROM combatant"
    cursor = connection.cursor()
    cursor.execute(sql)
    print("<div style=float:left>")
    print("<table border='1'>")
    for index, record in enumerate(cursor.fetchall()):
        print("<tr>", "<td>", "<a href='combatant.py?id=" + str(record[0]),
              "'>", record[1], "</a>", "</td>", "</tr>", "\n", end = " ")
    print("</div>")
    return connection


print("Content-type: text/html\n")
print("<html><head><title>Combatant List</title></head>")
print("<body>")
print("<a href='../index.html'>Home</a>")
print("<h1>Combatant List</h1>")
print("<div style=float:right>")
print("<img src=\'/select-player.png\' style=\'width:600px;height:450px;\'>")
print("<!-- http://retrowaretv.com/wp-content/uploads/2016/01/\
      select-player.png -->")
print("<!-- From the game Golden Axe by Sega -->")
print("</div>")
con = populate()
print("</table")
con.close()
print("</body></html>")
