from pathlib import Path
from random import sample
# nn = Path('english-nouns.txt').read_text().strip().split('\n')
# adj = Path('english-adjectives.txt').read_text().strip().split('\n')
verbs = Path('english/mostly-verbs-infinitive.txt').read_text().strip().split('\n')
# sample_nn = sample(nn, 300)
# sample_adj = sample(adj, 300)
sample_iverbs = sample(sorted(verbs, key=lambda x: len(x), reverse=True)[:1000],200)
tverbs = [x for x in verbs if x not in sample_iverbs ]
sample_tverbs = sample(sorted(tverbs, key=lambda x: len(x), reverse=True)[:1000],200)
with open('english/sample_ivbs.txt', 'w') as n:
    for w in sample_iverbs:
        w= w.split()[0]
        to_write = f'1\tIVerb_S\t{w}\n'
        n.write(to_write)


    for k in sample_iverbs:
        k = k.split()[0]
        to_write2 =  f'1\tIVerb_P\t{k}\n'
        n.write(to_write2)


with open('english/sample_tvbs.txt', 'w') as n:
    for w in sample_tverbs:
        w= w.split()[0]
        to_write = f'1\tTVerb_S\t{w}\n'
        n.write(to_write)


    for k in sample_tverbs:
        k = k.split()[0]
        to_write2 =  f'1\tTVerb_P\t{k}\n'
        n.write(to_write2)

# with open('sample_adj.txt', 'w') as adj:
#     for t in sample_adj:
#         tw= f'1\tAdj\t{t}\n'
#         adj.write(tw)


