#!/usr/bin/env python

'''
A file dedicated to easily writing out answers to the questions asked
for this project. When write_results is called, it will automatically
write out to a file called 'results.txt'.
'''

# result headers
RESULT_HEADER_1 = "1.) What are the three most popular articles?\n"
RESULT_HEADER_2 = "2.) Who are the most popular authors?\n"
RESULT_HEADER_3 = "3.) On which days did more than 1% of requests lead to errors?\n"

# file
RESULTS_FILE_NAME = "results.txt"

# clear file
def clear_results():
    results_file = open(RESULTS_FILE_NAME, "w")
    results_file.close()

# write to file
# result_num: numbered question you are answering
def write_results(result_num, query_results):
    # open file
    results_file = open(RESULTS_FILE_NAME, "a")
    # write header
    if result_num == 1:
        results_file.write(RESULT_HEADER_1)
    elif result_num == 2:
        results_file.write(RESULT_HEADER_2)
    else:
        results_file.write(RESULT_HEADER_3)
    # write results and close
    results_file.write("\n")
    results_file.write(query_results + "\n\n")
    results_file.close()
