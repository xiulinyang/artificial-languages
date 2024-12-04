#!/bin/bash

bash train_lm_lstm.sh base-grammar 0
bash train_lm_lstm.sh flip-grammar 0

bash train_lm_transformer.sh flip-grammar 0
bash train_lm_transformer.sh base-grammar 0
