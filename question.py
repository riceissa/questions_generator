#!/bin/python3

import itertools
import csv

#"What is it like to play super smash brothers while on {}?|LSD, marijuana, MDMA, psilocybin"
# ["What is it like to play super smash brothers while on {}?", ["LSD", "marijuana", "MDMA", "psilocybin"]]
# -> ["What is it like to play super smash brothers while on LSD?", "What is it like to play super smash brothers while on marijuana?", "What is it like to play super smash brothers while on MDMA?",  "What is it like to play super smash brothers while on psilocybin?"]

# Some commonly-used lists
lists = {
    "DRUGS": ["marijuana", "MDAM", "ketamine", "LSD", "psilocybin"],
    "UNIS": ["University of Washington", "MIT", "Caltech", "Yale", "Harvard", "Harvey Mudd College", "Princeton", "Brown University", "Stanford", "University of Chicago", "UC Berkeley", "UCLA"],
    "PEOPLE": ["Mark Zuckerberg", "Travis Kalanick", "Jimmy Wales", "Peter Thiel", "Elon Musk", "Noam Chomsky", "Bryan Caplan"]
    "QUORA_USERS": ["Brian Farley", "Brian Bi", "Alex K. Chen", "Vipul Naik", "Marc Srour", "Michael O. Church"],
    "PROCONS": ["pros", "cons"],
    "ANIMALS": ["kakapo", "parrot"],
    "ANIMALP": ["kakapo", "parrots"],
}
def prod(A, B):
    A = set(A)
    B = set(B)
    B = B.difference(A)
    result = []
    for i in itertools.product(A, B):
        if len(i) == len(set(i)):
            result.append(i)
    return result

def make_question_compts(file_obj):
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
        print("sane")
        if len(question_compts) == 3 and question_compts[1] == question_compts[2]:
            for i in question_compts[1]:
                for j in question_compts[2]
                FIXME
        else:
            for i in itertools.product(*question_compts[1:]):
                try:
                    if len(i) == len(set(i)):
                        # So we don't ask a question with overlapping parameters
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
        compts_list = make_question_compts(f)
        print(compts_list)
        for i in compts_list:
            print(generate_questions(i))
