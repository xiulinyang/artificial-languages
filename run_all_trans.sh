#!/bin/bash

mkdir -p trans-results

for num in {0..9}; do
  bash train_lm_transformer.sh grammar42 $num
  bash train_lm_transformer.sh grammar42_permutation $num
done
