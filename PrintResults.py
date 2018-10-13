#!/usr/bin/env python

'''
A file dedicated to easily writing out answers to the questions asked
for this project. When write_results is called, it will automatically
write out to a file called 'results.txt'.
'''

# imports
import datetime

# result headers
RH1 = "1.) What are the three most popular articles?\n"
RH2 = "2.) Who are the most popular authors?\n"
RH3 = "3.) Which days did 1% or more of requests lead to errors?\n"

# string formats
q1_beg_str = "The article "
q1_mid_str = " has a total of "
q1_end_str = " views."
q2_beg_str = "The author "
q2_mid_str = " has a total of "
q2_end_str = " views to their articles."
q3_beg_str = "On "
q3_mid_str = " there was a total of "
q3_end_str = " percent of requests that led to errors."

# file
RESULTS_FILE_NAME = "results.txt"


# clear file
def clear_results():
    results_file = open(RESULTS_FILE_NAME, "w")
    results_file.close()


# prints results
# result_num: numbered question you are answering
# query_results: the results of the query in a string
# write_to_file: whether results will be written to a file or printed
def print_results(result_num, query_results, write_to_file=False):
    # get header
    header = ""
    if result_num == 1:
        header = RH1
    elif result_num == 2:
        header = RH2
    else:
        header = RH3
    # string to write
    query_results_str = results_to_str(result_num, query_results)
    results_str = header + "\n" + query_results_str + "\n"
    # if write to file
    if write_to_file:
        # open file, write header
        results_file = open(RESULTS_FILE_NAME, "a")
        # write results and close
        results_file.write(results_str)
        results_file.close()
    else:
        print(results_str)


# formats the list of results into a neat string
# result_num: numbered question you are answering
# query_results: the results of the query in a string
def results_to_str(result_num, query_results):
    # strings for formatting
    beg_str = ""
    mid_str = ""
    end_str = ""
    final_str = ""
    # query results list of strings
    query_list_str = []

    # build surrounding strings
    if result_num == 1:
        beg_str = q1_beg_str
        mid_str = q1_mid_str
        end_str = q1_end_str
    elif result_num == 2:
        beg_str = q2_beg_str
        mid_str = q2_mid_str
        end_str = q2_end_str
    else:
        beg_str = q3_beg_str
        mid_str = q3_mid_str
        end_str = q3_end_str

    # turn queries into list of 2-tuple strings
    if result_num == 1 or result_num == 2:
        for (name, count) in query_results:
            query_list_str.append(("'%s'" % name, str(count)))
    else:
        for (date, perc) in query_results:
            query_list_str.append((date.strftime('%m/%d/%y'),
                                   str(perc*100.0)))

    # create readable queries
    index = 1
    for (r1, r2) in query_list_str:
        final_str += str(index) + "- "
        final_str += beg_str + r1 + mid_str + r2 + end_str
        final_str += "\n"
        index += 1
    # return final string
    return final_str
