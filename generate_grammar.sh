#!/bin/bash

# Array of 10 random seeds
seed=42
mkdir -p data_gen/grammar${seed}
mkdir -p data_gen/permute${seed}
python data_gen/sample_sentences.py -g data_gen/base-grammar.gr -n 100000 -O grammar/grammar${seed}.txt -s ${seed} -b True
python data_gen/permute_sentences.py -s grammar/grammar${seed}.txt -o data_gen/permute${seed}/grammar${seed}_permutation.txt
python postprocess.py -i grammar/grammar${seed}.txt -o data_gen/grammar${seed}/grammar${seed}.txt

echo "All scripts have been run with all seeds."

python make_splits.py -S permute42/ -O .
python make_splits.py -S grammar42/ -O .

python test_generator.py
