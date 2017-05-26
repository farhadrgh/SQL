#! /Users/farhad/anaconda/bin/python

import sqlite3

con = sqlite3.connect("survey.db")
cur = con.cursor()
cur.execute("SELECT * from Person;")
results = cur.fetchall()
#print(results)

for i in results:
    print(i)

cur.close()
con.close()
