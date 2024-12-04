#!/bin/bash

for num in {0..9}; do
    echo "We are running on split ${num}"
    bash train_lm_lstm.sh grammar42 $num
    bash train_lm_lstm.sh grammar42_permutation $num
done
