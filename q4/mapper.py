#!/usr/bin/python

## mapper func top10 tag list

import sys
import csv

#with open('student_test_posts.csv', 'r') as csvfile:
reader = csv.reader(sys.stdin, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
reader.next()

for row in reader:
    if len(row) == 19:
        id = row[0]
        tagname = row[2]
        nodetype = row[5]
        if nodetype == "question":
            for tag in tagname.split(' '):
                print "{0}\t{1}".format(tag,id)
