#!/bin/bash

# Array of 10 random seeds
seed=$1
exp=$2
mkdir -p data_gen/grammar${seed}${exp}
mkdir -p data_gen/permute${seed}${exp}
python data_gen/sample_sentences.py -g data_gen/base-grammar.gr -n 100000 -O data_gen/grammar${seed}${exp}/grammar${seed}_b.txt -s ${seed} -b True
python data_gen/permute_sentences.py -s data_gen/grammar${seed}${exp}/grammar${seed}_b.txt -o data_gen/permute${seed}${exp}/grammar${seed}_permutation.txt -e ${exp}
python postprocess.py -i data_gen/grammar${seed}${exp}/grammar${seed}_b.txt -o data_gen/grammar${seed}${exp}/grammar${seed}.txt

echo "All scripts have been run with all seeds."

python data_gen/make_splits.py -S data_gen/permute${seed}${exp}/ -O .
python data_gen/make_splits.py -S data_gen/grammar${seed}${exp}/ -O .

python test_generator.py
