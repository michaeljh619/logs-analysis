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
from QueryHandler import query

# authorship
__author__ = "Michael J. Hart"
__email__ = "MichaelJHart760@gmail.com" 

# queries
Q1 = "select articles.title, count(*) as num"
Q2 = " from articles, log"
Q3 = " where path != '/' and SUBSTR(path, 10) = slug"
Q4 = " group by articles.title"
Q5 = " order by num desc limit 3;"
QUERY1 = Q1 + Q2 + Q3 + Q4 + Q5

# perform queries
results1 = query(QUERY1)
results1_str = '\n'.join(str(x) for x in results1)
full_answer1 = Q1+"\n"+Q2+"\n"+Q3+"\n"+Q4+"\n"+Q5+"\n\n"+ results1_str

# write the results to a file
clear_results()
write_results(1, full_answer1)
#write_results(2, "Poofing!")
#write_results(3, "Eating!")
