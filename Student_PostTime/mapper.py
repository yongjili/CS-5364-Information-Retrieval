#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

#regular expression
timePattern = re.compile(r"\s+(\d+):\d+:\d+")
#compile html case
lineStart = re.compile(r'''^"''')
lineEnd = re.compile(r'''"$''')
html = False
html_author_id = ""

#f = open("student_test_posts.csv",'r')

for line in sys.stdin:
#for line in f:
    data = line.strip().split("\t")
    if not html:
        if len(data) == 19:
            author_id = data[3]
            added_at = data[8]
        
            result =timePattern.search(added_at)
            if result:
                hour = result.group(1)
                print "{0}\t{1}".format(author_id, hour)

        elif len(data) > 4 and lineStart.match(data[4]):
            #body = data[4]
            html = True
            html_author_id = data[3]

    elif len(data) == 15 and lineEnd.search(data[0]):
        #body = data[0]
        #reEnd = lineEnd.search(body)
        html = False

        author_id = html_author_id
        added_at = data[4]
  
        result =timePattern.search(added_at)
        if result:
            hour = result.group(1)
            print "{0}\t{1}".format(author_id, hour)

           









