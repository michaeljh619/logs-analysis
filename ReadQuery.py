#!/usr/bin/env python

'''
A file dedicated to reading text files containing queries.
The one function in this file will return the query as a string
so it can be used in the QueryHandler.
'''

# read file, return query in a string
def read_query_file(file_name):
    # return string set up
    file_contents = ""

    # open to read
    try:
        query_file = open(file_name, "r")
        for line in query_file:
            file_contents += line + " "

    # close file
    finally:
        query_file.close()
    
    # return string
    return file_contents
