#!/bin/python3

import argparse
import itertools
import csv
import sys

from lists import lists

def make_question_compts(file_obj):
    '''
    Take file object and return a list of lists, where each element in
    the overall list has a string (base question) followed by any number
    of lists, each containing strings.

    Example result:

    [['What is it like to be {}?', ['Mark Zuckerberg', 'Travis
    Kalanick', 'Jimmy Wales', 'Peter Thiel', 'Elon Musk', 'Noam
    Chomsky', 'Bryan Caplan']], ['How can {} be disrupted?', ['museums',
    'zoos']]]
    '''
    result = []
    reader = csv.reader(file_obj, delimiter='|')
    for row in reader:
        row_result = []
        try:
            row_result.append(row[0].strip())
            for i in row[1:]:
                row_result.append(lists.get(i.strip(), [j.strip() for j in i.split(",")]))
            result.append(row_result)
        except ValueError:
            pass
    return result

def generate_questions(question_compts):
    '''
    Produce a list of actual questions.
    '''
    if len(question_compts) <= 1:
        result = question_compts
    else:
        result = []
        if len(question_compts) == 3 and question_compts[1] == question_compts[2]:
            # So questions of the type "What do PERSON and PERSON think
            # of each other?", where we want to avoid asking "What do
            # Mark Zuckerberg and Mark Zuckerberg think of each other?"
            # and so on. Here questions are considered to be the same
            # even when they have a different order.  Note that we can't
            # tell the difference between questions where the order
            # matters and when it doesn't; we just assume the order
            # doesn't matter.
            for n, v in enumerate(question_compts[1]):
                for m, w in enumerate(question_compts[2][n + 1:]):
                    try:
                        result.append(question_compts[0].format(v, w))
                    except (ValueError, IndexError):
                        pass
        else:
            for i in itertools.product(*question_compts[1:]):
                if len(i) == len(set(i)):
                    # So we don't ask a question with overlapping parameters
                    try:
                        result.append(question_compts[0].format(*i))
                    except (ValueError, IndexError):
                        pass
    return result

if __name__ == "__main__":
    #compts = ["What is it like to play super smash brothers while on {}?", ["LSD", "marijuana", "MDMA", "psilocybin"]]
    ##print(generate_questions(compts))
    #print(generate_questions(["What is it like to {} at {}?", ["have sex", "become depressed"], unis]))
    #print(generate_questions([]))

    parser = argparse.ArgumentParser(description="Generate questions based on patterns and lists")
    parser.add_argument("input_file", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="input file; default to stdin")
    parser.add_argument("-n", "--number", action="store_true", help="report number of questions generated as final line")
    args = parser.parse_args()
    count = 0
    all_questions = []
    compts_list = make_question_compts(args.input_file)
    for i in compts_list:
        questions = generate_questions(i)
        count += len(questions)
        all_questions.extend(questions)
    for i in all_questions:
        print(i)
    if args.number:
        print("{} questions were generated".format(str(count)))
