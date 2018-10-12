#!/usr/bin/env python

'''
A script with SQL queries to answer questions about the
newsdata database.

1.) What are the 3 most popular articles of all time?
2.) Who are the most popular article authors of all time?
3.) On which days did more than 1% of requests lead to errors?
'''

# imports
from WriteFile import write_results, clear_results
from ReadQuery import read_query_file
from QueryHandler import query

# authorship
__author__ = "Michael J. Hart"
__email__ = "MichaelJHart760@gmail.com" 

# query files
QUERY_FILE_1 = "query1.txt"
QUERY_FILE_2 = "query2.txt"
QUERY_FILE_3 = "query3.txt"

# get queries
query_str_1 = read_query_file(QUERY_FILE_1)
query_str_2 = read_query_file(QUERY_FILE_2)
query_str_3 = read_query_file(QUERY_FILE_3)

print(query_str_1)

# perform queries
results1 = query(query_str_1)
results2 = query(query_str_2)
results3 = query(query_str_3)

# turn query lists to strings
results_str_1 = '\n'.join(str(x) for x in results1)
results_str_2 = '\n'.join(str(x) for x in results2)
results_str_3 = '\n'.join(str(x) for x in results3)

# write the results to a file
clear_results()
write_results(1, results_str_1)
write_results(2, results_str_2)
write_results(3, results_str_3)
