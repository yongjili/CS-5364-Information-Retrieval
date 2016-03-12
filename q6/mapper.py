#!/usr/bin/python
"""
The response time for the first answer to its question
"""

import sys
import csv

def mapper(stdin):
    """
    Mapper  Key is the question ID, values are 0/1, question/answer,
    and post time.
    """
    reader = csv.reader(stdin, delimiter='\t')
    reader.next()
    writer \
        = csv.writer(
            sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            question id = line[0]
            node_type = line[5]
            added_at = line[8]
            if node_type == "answer":
                parent_id = line[6]
                writer.writerow([parent_id, "1", "answer", added_at])
            elif node_type == "question":
                writer.writerow([question id, "0", "question", added_at])

if __name__ == "__main__":
    mapper(sys.stdin)
}
