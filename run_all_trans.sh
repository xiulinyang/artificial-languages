#!/bin/bash

for num in {0,9}; do
  bash train_ls_transformer.sh grammar42 $num
  bash train_ls_transformer.sh grammar42_permutation $num
done