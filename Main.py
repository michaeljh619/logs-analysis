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
Q1_1 = "select articles.title, count(*) as num"
Q1_2 = " from articles, log"
Q1_3 = " where path != '/' and SUBSTR(path, 10) = slug"
Q1_4 = " group by articles.title"
Q1_5 = " order by num desc limit 3;"
QUERY1 = Q1_1 + Q1_2 + Q1_3 + Q1_4 + Q1_5
Q2_1 = "select authors.name, count(*) as num"
Q2_2 = " from articles, authors, log"
Q2_3 = " where path != '/' and SUBSTR(path, 10) = slug"
Q2_4 = " and authors.id = articles.author group by authors.name"
Q2_5 = " order by num desc;"
QUERY2 = Q2_1 + Q2_2 + Q2_3 + Q2_4 + Q2_5

# perform queries
results1 = query(QUERY1)
results1_str = '\n'.join(str(x) for x in results1)
full_answer1 = Q1_1+"\n"+Q1_2+"\n"+Q1_3+"\n"+Q1_4+"\n"+Q1_5+"\n\n"+ results1_str

results2 = query(QUERY2)
results2_str = '\n'.join(str(x) for x in results2)
full_answer2 = Q2_1+"\n"+Q2_2+"\n"+Q2_3+"\n"+Q2_4+"\n"+Q2_5+"\n\n"+ results2_str

# write the results to a file
clear_results()
write_results(1, full_answer1)
write_results(2, full_answer2)
#write_results(3, "Eating!")
