#!/usr/bin/env python3

import mysql.connector
import getpass

def getcon(verbose=False):
    #Connects to the database.
    login_name = getpass.getuser()
    config = {"user": login_name, "database": login_name}
    connection = mysql.connector.connect(**config)
    if verbose:
        print("Connecting with configuration:", config, sep='\n')
        print("Using", type(connection))
    return connection

def populate():
    #Fills in the html portion sourced from the database.
    connection = getcon()
    sql = "select winner_id, c.name, count(*) as wins from fight, combatant c where c.id = winner_id group by winner_id order by wins desc, winner_id;"
    data = connection.cursor()
    data.execute(sql)

#replace ids with names

    print ("<table border='1'>")
    print("<tr><th>Combatant</th> <th>Wins/Rank</th> </tr>")
    for record in data.fetchall():
        print ("<tr>", "<td>", "<a href='combatant.py?id=" + str(record[0]), "'>", record[1],"</a>", "</td>", "<td>", record[2], "</td>""</tr>", "\n", end = " ")
    return connection



#connection = getcon(True)
print("Content-type: text/html\n")
#This begins the Body of hte HTTP Response
print("<html><head><title>Ranking</title></head>")
print("<body>")
print("<h1>Ranking</h1>")


con = populate()
con.close()
print("</body></html>")
