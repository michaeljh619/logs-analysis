This program is designed to run a set of queries using psycopg2.
These queries will help answer the following set of questions:

	1.) What are the three most popular articles?
	2.) Who are the most popular authors?
	3.) Which days did 1% or more of requests lead to errors?


- Running the program:
	Simply run the 'main.py' as an executable with './Main.py'. The
results of the queries will be neatly printed to the console. If you wish
to have the results printed to a file instead, simply run the program with
the '--file' (or '-f') option; this will have the results written to a
file called "results.txt" instead.


- Design of the program:
	Main.py executes the program, it uses the ReadQuery file to read
queries from text files. It then performs the queries using psycopg2 on the
"news" database using the QueryHandler file. The results are then printed to
the screen, unless the '--file' option is set, in which case the results are
printed to a file instead.
	The queries that are performed are in the files "query1.txt",
"query2.txt", and "query3.txt" for each respective answer to the questions.
