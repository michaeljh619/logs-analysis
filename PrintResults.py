#!/usr/bin/env python

'''
A file dedicated to easily writing out answers to the questions asked
for this project. When write_results is called, it will automatically
write out to a file called 'results.txt'.
'''

# result headers
RH1 = "1.) What are the three most popular articles?\n"
RH2 = "2.) Who are the most popular authors?\n"
RH3 = "3.) Which days did 1% or more of requests lead to errors?\n"

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
    results_str = header + "\n" + query_results + "\n\n"
    # if write to file
    if write_to_file:
        # open file, write header
        results_file = open(RESULTS_FILE_NAME, "a")
        # write results and close
        results_file.write(results_str)
        results_file.close()
    else:
        print(results_str)
