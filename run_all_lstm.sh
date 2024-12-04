#!/bin/bash

mkdir -p data-bin
mkdir -p checkpoints
mkdir -p lstm-results
fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/${SPLIT}-dataset" --workers 20
fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/incorrect_${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/incorrect_${SPLIT}-dataset" --workers 20
fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/correct_${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/correct_${SPLIT}-dataset" --workers 20

for num in {0,9}; do
    bash train_lm_lstm.sh grammar42 $num
    bash train_lm_lstm.sh grammar42_permutation $num
done