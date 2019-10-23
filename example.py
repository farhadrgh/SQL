#!/usr/bin/env python

import sqlite3
import csv

con = sqlite3.connect("survey.db")
cur = con.cursor()
cur.execute("SELECT max(reading), min(reading), sum(reading), avg(reading) from Survey;")
results = cur.fetchall()

k = ['max', 'min', 'sum', 'avg']
for i in results:
    for j in range(len(i)):
        print(k[j], '=', i[j])

#cur = con.cursor()
cur.execute("SELECT * from Site;")
results2 = cur.fetchall()
out = csv.writer(open('data.csv', 'w'))
for d in results2:
    out.writerow(d)

cur.close()
con.close()
