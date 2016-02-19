#!/usr/bin/python

import sys
import csv

def reducer():

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = \
        csv.writer(
            sys.stdout, delimiter='\t', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
    answer_num = 0
    answer_length = 0
    question_body_length = None
    current_id = None
    for line in reader:
        if len(line) == 4:
            data_id = line[0]
            if current_id is None or data_id != current_id:
                if not current_id is None:
                    write_record(
                        current_id, question_body_length, answer_num,
                        answer_length, writer)
                question_body_length = None
                answer_num = 0
                answer_length = 0               
                current_id = data_id

            node_type = line[2]
            body_length = int(line[3])
            if node_type == "question":
                question_body_length = body_length
            else:
                answer_num += 1
                answer_length += body_length
    write_record(
        current_id, question_body_length, answer_num, answer_length,
        writer)

def write_record(
    data_id, question_body_length, answer_num, answer_length, writer):
    writer.writerow(["   Outputs   Question Node ID |	Question Length |	Average Answer Length"])
    if answer == 0:
        writer.writerow([data_id, question_body_length, "0"])
    else:
        writer.writerow(
            [data_id, question_body_length,
             float(answer_length) / float(answer_num)])

if __name__ == "__main__":
    reducer()
