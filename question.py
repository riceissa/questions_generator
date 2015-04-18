#!/bin/python3

import itertools
import csv

from lists import lists

#"What is it like to play super smash brothers while on {}?|LSD, marijuana, MDMA, psilocybin"
# ["What is it like to play super smash brothers while on {}?", ["LSD", "marijuana", "MDMA", "psilocybin"]]
# -> ["What is it like to play super smash brothers while on LSD?", "What is it like to play super smash brothers while on marijuana?", "What is it like to play super smash brothers while on MDMA?",  "What is it like to play super smash brothers while on psilocybin?"]

def make_question_compts(file_obj):
    '''
    Take file object and return a list of lists, where each element in
    the overall list has a string (base question) followed by any number
    of lists, each containing strings.
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
    if len(question_compts) <= 1:
        result = question_compts
    else:
        result = []
        if len(question_compts) == 3 and question_compts[1] == question_compts[2]:
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

    with open("data.txt", "r") as f:
        count = 0
        all_questions = []
        compts_list = make_question_compts(f)
        #print(compts_list)
        for i in compts_list:
            questions = generate_questions(i)
            count += len(questions)
            all_questions.extend(questions)
            #print(questions)
        for i in all_questions:
            print(i)
        print("{} questions were generated".format(str(count)))
