#!/usr/bin/env python

'''
A script with SQL queries to answer questions about the
newsdata database.

1.) What are the 3 most popular articles of all time?
2.) Who are the most popular article authors of all time?
3.) On which days did more than 1% of requests lead to errors?
'''

# imports
from PrintResults import print_results, clear_results
from ReadQuery import read_query_file
from QueryHandler import query
from optparse import OptionParser

# authorship
__author__ = "Michael J. Hart"
__email__ = "MichaelJHart760@gmail.com"

# command line options
parser = OptionParser()
parser.add_option("-f", "--file", action="store_true",
                  help="write results to results.txt", default=False)
(options, args) = parser.parse_args()

# query files
QUERY_FILE_1 = "query1.txt"
QUERY_FILE_2 = "query2.txt"
QUERY_FILE_3 = "query3.txt"

# get queries
query_str_1 = read_query_file(QUERY_FILE_1)
query_str_2 = read_query_file(QUERY_FILE_2)
query_str_3 = read_query_file(QUERY_FILE_3)

# perform queries
results1 = query(query_str_1)
results2 = query(query_str_2)
results3 = query(query_str_3)

# turn query lists to strings
results_str_1 = '\n'.join(str(x) for x in results1)
results_str_2 = '\n'.join(str(x) for x in results2)
results_str_3 = '\n'.join(str(x) for x in results3)

# print the results, may be to a file depending on CL options
if options.file:
    clear_results()
print_results(1, results_str_1, options.file)
print_results(2, results_str_2, options.file)
print_results(3, results_str_3, options.file)
