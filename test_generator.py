from pathlib import Path
from collections import Counter

VOCAB = [x for x in Path('Y_vocab.txt').read_text().strip().split('\n')]

CLOSEDCLASS = ['on', 'at', 'in', 'over', 'from', 'an', 'a', 'the', 'my', 'one', '-ed', '-s']


def get_bigrams(sents):
    bigrams = [b for l in sents for b in zip(l.split(" ")[1:-1], l.split(" ")[2:])]
    bigram_perm = ['_'.join(list(x)) for x in bigrams]

    return bigram_perm


def get_freq(bigrams, permute=False):
    '''
    word_x: the closed class item
    word_y: the open class item
    '''
    if permute:
        x_id =  '1'
    else:
        x_id = '0'
    target_freq = {}
    alternative_freq = {}
    freq = Counter(bigrams)
    for bigram, count in freq.items():
        word_x, word_y = (bigram.split('_')[1], bigram.split('_')[0]) if permute else bigram.split('_')
        def update_freq_dict(freq_dict, word, count, bigram, x_id):
            if x_id:

                if bigram.split('_')[int(x_id)] in CLOSEDCLASS:
                    if word not in freq_dict:
                        freq_dict[word] = {count: [bigram]}
                    else:
                        freq_dict[word].setdefault(count, []).append(bigram)

                else:
                    return
            else:

                if word not in freq_dict:
                    freq_dict[word] = {count: [bigram]}
                else:
                    freq_dict[word].setdefault(count, []).append(bigram)

        if word_x in VOCAB:
            update_freq_dict(target_freq, word_x, count, bigram, None)
        elif word_y in VOCAB:
            update_freq_dict(alternative_freq, word_y, count, bigram, x_id)
    return target_freq, alternative_freq

def get_all_pair(freq_dict):
    return [' '.join(j.split('_')) for y in freq_dict for _, z in y.items() for _, t in z.items() for j in t]

def write_test(freq_dict, output_name):
    with open(output_name, 'w') as o:
        to_write = '\n'.join(get_all_pair(freq_dict))
        o.write(f"{to_write}")

def check_vocab_size(file1,file2):
    tok_file1 = [y for x in file1 for y in x.split()]
    tok_file2 = [y for x in file2 for y in x.split()]
    overlap = len(set(tok_file1) & set(tok_file2))
    if len(set(tok_file1))==len(set(tok_file2))== overlap:
        print(f'the vocab size between is the same!!')
    else:
        print([x for x in tok_file2 if x not in tok_file1])
        print([x for x in tok_file1 if x not in tok_file2])
        print(f'the vocab size is different!!')
if __name__ == '__main__':
    for i in range(10):
        index = str(i)
        base_grammar_correct = f'data_gen/grammar42exp2/grammar42exp2/correct_{index}.tst'
        base_grammar_incorrect = f'data_gen/grammar42exp2/grammar42exp2/incorrect_{index}.tst'
        permute_grammar_correct = f'data_gen/grammar42exp2_permutation/grammar42exp2_permutation/correct_{index}.tst'
        permute_grammar_incorrect = f'data_gen/grammar42exp2_permutation/grammar42exp2_permutation/incorrect_{index}.tst'
        permutations = [x for x in Path(f'data_gen/grammar42exp2/grammar42exp2/{index}.trn').read_text().strip().split('\n')]
        original = [x for x in Path(f'data_gen/grammar42exp2_permutation/grammar42exp2_permutation/{index}.trn').read_text().strip().split('\n')]
        check_vocab_size(permutations, original)
        bigrams_permy, bigrams_permx = get_freq(get_bigrams(permutations), True)
        bigrams_origy, bigrams_origx = get_freq(get_bigrams(original), False)
        overlap_keys = set(bigrams_origx.keys()) & set(bigrams_permx.keys()) & set(bigrams_origy.keys()) & set(
            bigrams_permy.keys())

        test_orig_a = []
        test_orig_b = []
        test_perm_a = []
        test_perm_b = []

        for k, v in bigrams_origy.items():
            if k in overlap_keys:
                overlap_freq = set(bigrams_origy[k].keys()) & set(bigrams_permy[k].keys()) & set(
                    bigrams_origx[k].keys()) & set(bigrams_permx[k].keys())
                for freq in overlap_freq:
                    min_num = min(
                        [len(bigrams_origy[k][freq]), len(bigrams_origx[k][freq]), len(bigrams_permy[k][freq]),
                         len(bigrams_permx[k][freq])])
                    test_orig_a.append({k: {freq: bigrams_origy[k][freq][:min_num]}})
                    test_orig_b.append({k: {freq: bigrams_origx[k][freq][:min_num]}})
                    test_perm_a.append({k: {freq: bigrams_permy[k][freq][:min_num]}})
                    test_perm_b.append({k: {freq: bigrams_permx[k][freq][:min_num]}})

        write_test(test_orig_a,base_grammar_incorrect)
        write_test(test_orig_b,base_grammar_correct)
        write_test(test_perm_a,permute_grammar_incorrect)
        write_test(test_perm_b,permute_grammar_correct)


