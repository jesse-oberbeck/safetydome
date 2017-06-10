#!/usr/bin/env python3

import mysql.connector
import getpass
import cgi

def getvals():
    fields = cgi.FieldStorage()
    default = ""
    vs = fields.getvalue("vs", default)
    print ("<h2>",vs,"</h2>")
    one, two = vs.split('v')
    try:
        one = int(one)
        two = int(two)
        return one, two
    except:
        print("<h3>", "Nice try, Dave.","</h3>")

def getcon(verbose=False):
    login_name = getpass.getuser()
    config = {"user": login_name, "database": login_name}
    connection = mysql.connector.connect(**config)
    if verbose:
        print("Connecting with configuration:", config, sep='\n')
        print("Using", type(connection))
    return connection

def populate(connection, one, two):

    sql = "SELECT * FROM fight WHERE combatant_one = '" + str(one) + "' AND combatant_two = '" + str(two) + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()[0]

    comb1 = cursor.execute("SELECT name FROM combatant WHERE id = "+ str(data[0]))
    comb1 = cursor.fetchall()[0][0]
    comb2 = cursor.execute("SELECT name FROM combatant WHERE id = "+ str(data[1]))
    comb2 = cursor.fetchall()[0][0]
    winner =  cursor.execute("SELECT name FROM combatant WHERE id = "+ str(data[2]))
    winner = cursor.fetchall()[0][0]

    print ("<table border='1'>")
    #Table header
    print("<tr>")
    print("<th>Combatant 1</th> <th>Combatant 2</th> <th>Winner</th> <th>Start</th> <th>Finish</th>")
    print("</tr>")
    print("<tr>")

    #for index, record in enumerate(cursor.fetchall()):
    print ("<td>", comb1, "</td>", "\n", end = " ")
    print ("<td>", comb2, "</td>", "\n", end = " ")
    print ("<td>", winner, "</td>", "\n", end = " ")
    print ("<td>", data[3], "</td>", "\n", end = " ")
    print ("<td>", data[4], "</td>", "\n", end = " ")
    print("</tr>")
    return connection



#connection = getcon(True)
print("Content-type: text/html\n")
#This begins the Body of hte HTTP Response
print("<html><head><title>Combatant Details</title></head>")
print("<body>")
print("<h1>Battle Details</h1>")
connection = getcon()
val1, val2 = getvals()
con = populate(connection, val1, val2)
con.close()
print("</body></html>")
