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


# authorship
__author__ = "Michael J. Hart"
__email__ = "MichaelJHart@gmail.com"

# code
clear_results()
write_results(1, "Testing!")
write_results(2, "Poofing!")
write_results(3, "Eating!")
