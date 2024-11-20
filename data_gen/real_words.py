from pathlib import Path
from random import sample
nn = Path('english-nouns.txt').read_text().strip().split('\n')
adj = Path('english-adjectives.txt').read_text().strip().split('\n')

sample_nn = sample(nn, 300)
sample_adj = sample(adj, 300)

with open('sample_ns.txt', 'w') as n:
    for w in sample_nn:
        to_write = f'1\tNoun_S\t{w}\n'
        n.write(to_write)


    for k in sample_nn:
        to_write2 =  f'1\tNoun_P\t{k}\n'
        n.write(to_write2)


with open('sample_adj.txt', 'w') as adj:
    for t in sample_adj:
        tw= f'1\tAdj\t{t}\n'
        adj.write(tw)


