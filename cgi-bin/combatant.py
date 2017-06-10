#!/usr/bin/env python3

import mysql.connector
import getpass
import cgi

def getval():
    fields = cgi.FieldStorage()
    default = ""
    comb_id = fields.getvalue("id", default)
    print ("<h2>",type(comb_id),"</h2>")
    try:
        comb_id = int(comb_id)
        return comb_id
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

def populate(connection,comb_id):

    sql = "SELECT * FROM combatant WHERE id = " + str(comb_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()[0]

    base_stats = "SELECT base_atk, base_dfn, base_hp from species where id =" + str(data[0])
    cursor.execute(base_stats)
    bases = cursor.fetchall()[0]

    #Separate items:
    name = data[1]
    spc = data[2]
    atk = int(data[3]) + int(bases[0])
    dfn = int(data[4]) + int(bases[1])
    hp = int(data[5]) + int(bases[2])

    attacks = "SELECT name FROM attack WHERE id IN (SELECT attack_id FROM species_attack WHERE species_id =" + str(spc) + ");"
    cursor.execute(attacks)
    atk_list = [x[0] for x in cursor.fetchall()]

    spec = "SELECT name FROM species WHERE id = " + str(spc) + ";"
    cursor.execute(spec)
    species = cursor.fetchall()[0][0]

    print ("<table border='1'>")
    #Table header
    print("<tr>")
    print("<th>ID</th> <th>Name</th> <th>Species</th> <th>Attacks</th> <th>Attack</th> <th>Defense</th> <th>HP</th>")
    print("</tr>")
    print("<tr>")

    #for index, record in enumerate(cursor.fetchall()):
    print ("<td>", data[0], "</td>", "\n", end = " ")
    print ("<td>", name, "</td>", "\n", end = " ")
    print ("<td>", species, "</td>", "\n", end = " ")
    print ("<td>", atk_list, "</td>", "\n", end = " ")
    print ("<td>", str(atk), "</td>", "\n", end = " ")
    print ("<td>", str(dfn), "</td>", "\n", end = " ")
    print ("<td>", str(hp), "</td>", "\n", end = " ")
    print("</tr>")
    return connection



#connection = getcon(True)
print("Content-type: text/html\n")
#This begins the Body of hte HTTP Response
print("<html><head><title>Combatant Details</title></head>")
print("<body>")
print("<h1>Combatant Details</h1>")
connection = getcon()
val = getval()
con = populate(connection, val)
con.close()
print("</body></html>")
