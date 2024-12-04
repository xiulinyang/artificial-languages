from pathlib import Path
import argparse

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
    new_s.append(".\n")
    return ' '.join(new_s)

parser = argparse.ArgumentParser(description="postprocess sentences with bracket")

parser.add_argument("-i", "--input_file", type=str, default='',
    help="Path to input file")
parser.add_argument("-o", "--output_file", type=str, default='',
    help="Path to output file")

args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file

input_f = Path(input_file).read_text().strip().split('\n')
with open(output_file, 'w') as o:
    for s in input_f:
        post_s = remove_bracketing(s)
        o.write(post_s)
