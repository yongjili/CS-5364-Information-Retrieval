#!/usr/bin/python
"""
Reducer: 1st response time
"""

import sys
import csv
from datetime import datetime

def reducer():
    """
    Reducer after shuffle and sort, we calculate
    the shortest response time of the answers to its questoin 
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = \
        csv.writer(
            sys.stdout, delimiter='\t', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
    question_added_at = None
    1st_response_time = None
    current_id = None
    prefix_len = len('2016-03-08 10:16:12')
    date_format = '%Y-%m-%d %H:%M:%S'
    for line in reader:
        if len(line) == 4:
            node_id = line[0]
            if current_id is None or node_id != current_id:
                if not current_id is None:
                    write_record(current_id, 1st_response_time, writer)
                    1st_response_time = None
                current_id = node_id
            """
            node type is whether it is a question or an answer
            """
            node_type = line[2]
            added_at = line[3]
            if node_type == "question":
                question_added_at = \
                    datetime.strptime(added_at[:prefix_len], date_format)
            else:
                answer_added_at = \
                    datetime.strptime(added_at[:prefix_len], date_format)
                if not question_added_at is None:
                    delta = answer_added_at - question_added_at
                    response_time = delta.seconds / 60
                    if 1st_response_time is None or \
                        response_time < 1st_response_time:
                        1st_response_time = response_time
    write_record(current_id, 1st_response_time, writer)


def write_record(node_id, response_time, writer):
    """
    Output:
        Question Node ID | Response Time (in minutes)
    """
    if response_time is None:
        writer.writerow([node_id, "NA"])
    else:
        writer.writerow([node_id, response_time])

if __name__ == "__main__":
    reducer()
}
