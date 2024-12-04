#!/bin/bash

GRAMMAR=$1
SPLIT=$2



mkdir -p data-bin
mkdir -p checkpoints
mkdir -p lstm-results
fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/${SPLIT}-dataset" --workers 20
fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/incorrect_${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/incorrect_${SPLIT}-dataset" --workers 20
fairseq-preprocess --only-source --trainpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --validpref "data_gen/${GRAMMAR}/${GRAMMAR}/${SPLIT}.dev" --testpref "data_gen/${GRAMMAR}/${GRAMMAR}/correct_${SPLIT}.tst" --destdir "data-bin/${GRAMMAR}/correct_${SPLIT}-dataset" --workers 20
