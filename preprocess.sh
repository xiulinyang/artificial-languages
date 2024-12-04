#!/bin/bash

GRAMMAR=$1

mkdir -p data-bin
mkdir -p checkpoints
mkdir -p lstm-results
mkdir -p data-bin/${GRAMMAR}/correct_${SPLIT}-dataset
mkdir -p data-bin/${GRAMMAR}/
for SPLIT in {0..9}; do
  #fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/${SPLIT}-dataset" --workers 20
  #fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/incorrect_${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/incorrect_${SPLIT}-dataset" --workers 20
  fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/correct_${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/correct_${SPLIT}-dataset" --workers 20
done
