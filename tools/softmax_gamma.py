import torch
import torch.nn as nn

def param_softmax(scores_list, gamma):

    # [INFO] scores_list is one_sentence_scores_list
    # shape : [tokens_num, vocab_size] example : [41, 1000]
    tokens_num = len(scores_list)
    vocab_size = len(scores_list[0])
    ps_list = []
    for i, ps in enumerate(scores_list):
        # [INFO] ps : one word's decoder output log_softmaxed posterior distribution
        ps = torch.tensor(ps)
        mole = torch.exp(ps) ** gamma
        denom = torch.sum(torch.exp(torch.tensor(ps)) ** gamma)
        param_softmax_scores_list = mole/denom
        # [INFO] print(torch.sum(mole/denom)) : 1
        ps_list.append(param_softmax_scores_list)
    return ps_list        

if __name__ == "__main__":
    scores_list = [[0.1, 0.2, 0.5, 0.2], [0.1, 0.2, 0.3, 0.4], [10.0, 10.0, 10.0, 10.0]]
    gamma = 150
    print(param_softmax(scores_list, gamma))
