#!/usr/bin/python

import sys
import csv

def mapper(stdin):
    """
    the key,value pair includes the question ID,
    0/1 stands for question/answer, and body length.
    """
    reader = csv.reader(stdin, delimiter='\t')
    # Skip the header.
    reader.next()
    writer \
        = csv.writer(
            sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            #The dataset has 19 attributes,including id, body, node type and parent_id
            the_id = line[0]
            body = line[4]
            node_type = line[5]
            if node_type == "question":
                writer.writerow([the_id, "0", "question", len(body)])
            elif node_type == "answer":
                parent_id = line[6]
                writer.writerow([parent_id, "1", "answer", len(body)])

if __name__ == "__main__":
    mapper(sys.stdin)
