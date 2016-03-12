import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    if len(line) == 19:
	node_id = line[0]
	author_id = line[3]
	node_type = line[5]
	abs_parent_id = line[7]
	if node_type == "question":
		print "{0}\t{1}".format(node_id, author_id)
	else:
		print "{0}\t{1}".format(abs_parent_id, author_id)
