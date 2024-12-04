import argparse
import os
import sys
import random
import copy

PATTERN_IDX = {
    2 : ['-ed', '-s'],
    3 : ['Det'],
    4 : ['Prep'],
}

PERMUTATION = {
    2: {'Vaff': ['-ed', '-s']},
    3: {'Det': ['an', 'a', 'the', 'my', 'one']},
    4: {'Prep': ['on', 'at', 'in', 'over', 'from']}
}


def flip_as_needed(sentence):
    to_flip = [2,3,4]
    s_split = sentence.split(" ")
    for j in range(len(s_split)):
        if s_split[j][0].isnumeric():
            if int(s_split[j][0]) in to_flip:
                reversed_end = reversed_children(s_split[j+1:],int(s_split[j][0]))

                s_split = s_split[:j+1] + reversed_end
                # print(s_split)
        else:
            continue
    return ' '.join(s_split).strip("\n")

def check_x(pattern_id, child):
    overlap = [x for x in PATTERN_IDX[pattern_id] if x in child]
    return overlap

def reversed_children(sentence_part, flip_id):
    children = []
    bracket_stack = []
    L_brack = '('
    R_brack = ')'
    children_end = -1
    for i in range(len(sentence_part)):
        s = sentence_part[i]
        if s == L_brack:
            bracket_stack.append((L_brack, i))
        elif s == R_brack:
            if len(bracket_stack) > 0:
                if bracket_stack[-1][0] == L_brack:
                    opening = bracket_stack.pop()
                    if len(bracket_stack) == 0:
                        children.append(sentence_part[opening[1]:i+1])
            else:
                children_end = i - 1
                break
        else:
            continue
    children_updated = []
    if len(children)!=1:
        for child in children[::-1]:
            children_updated += child

    else:
        for child in children:
            if check_x(flip_id, child):
                children_updated += child
            else:
                key = random.choice(list(PERMUTATION[flip_id].keys()))
                value = random.choice(PERMUTATION[flip_id][key])

                new_child = ['(', key, value, ')']
                children_updated += new_child
    return children_updated + sentence_part[children_end:]

def remove_bracketing(s):
    new_s = []
    split_s = s.split(" ")
    i = 0
    while i < len(split_s):
        if split_s[i] == ")":
            i += 1
        elif split_s[i] == "(":
            i += 2
        else:
            new_s.append(split_s[i])
            i += 1
    new_s.append(".")
    return ' '.join(new_s)

def generate_sentence_file(sentences, output_file):
    output_f = open(output_file, 'w')
    for s in sentences:
        output_f.write(remove_bracketing(flip_as_needed(s)) + "\n")
    output_f.close()

parser = argparse.ArgumentParser(description="Generate variants of sentences"
    " based on base grammar")

parser.add_argument("-s", "--sentence_file", type=str, required=True, 
    help="Path to base sentence file")

parser.add_argument("-o", "--output_path", type=str, required=True,
    help="Location of output folder")

args = parser.parse_args()

file = open(args.sentence_file, 'r')
sentences = file.readlines()

grammar_name = args.output_path
output_file = os.path.join(grammar_name)
generate_sentence_file(sentences, output_file)