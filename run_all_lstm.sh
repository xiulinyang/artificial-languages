#!/bin/bash


for num in {1..8}; do
  bash train_lm_lstm.sh grammar42 $num
  bash train_lm_lstm.sh grammar42_permutation $num
done
