#!/usr/bin/python

import sys

"""
Provide the Pyhton MapReduce encoding of the following SQL queries.
Q1. SELECT name FROM Customer WHERE month(startDate)=7

Customer(cid, startDate, name)

1,20/09/1985,PARKER LONG
2,03/07/1994,SAWYER NEWTON
3,31/12/1999,ROSE PARKER
4,16/08/1991,HAYES JACKSON
5,13/06/1980,MANN JACKSON
6,07/04/1980,SIMMONS FOX

"""


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line into words delim = ,
		# 1,20/09/1985,PARKER LONG => 1 / date / name
    words = line.split(",")

    # verif sur la date
    key = words[0]
    value = words[2]
    
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the 
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    print '%s\t%s' % (key, value)
