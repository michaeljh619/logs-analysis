#!/usr/bin/env python

'''
File dedicated to making query calls as simple as possible.
Simply give the query() function the sql query you want performed
and it will return you the data you want.
'''

# imports
import psycopg2

# Constants
DBNAME = "news"


def query(query_string):
    """Queries the newsdata database with the specified query"""
    # connect
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # query
    c.execute(query_string)

    # close and return
    rows = c.fetchall()
    db.close()
    return rows
