from pathlib import Path
from pprint import pprint

import os
import pickle

pickle_dir = '../../espnet/egs/fisher_callhome_spanish/st1/exp/train_sp.en_lc.rm_pytorch_softloss-epoch26/pre_decoding/dev'


def load_pickle(pickle_dir):
    p = Path()
    p_dir = p / pickle_dir
    # if not dir.exists():
    print(p_dir)
    cnt = 0
    # pprint(list(p_dir.iterdir()))
    for path in list(p_dir.iterdir()):
        if path.name == 'log':
            continue
        if path.suffix == '.json':
            continue
        if path.name == '20051009_182032_217_fsp-A-000070-000192':
            print(path.name)
            vector = pickle.load(f)
            continue
        p_path = p / path
        with p_path.open(mode='rb') as f:
            # print(path)
            vector = pickle.load(f)
            cnt += 1
    print(cnt)
        
if __name__ == '__main__':
    load_pickle(pickle_dir)        

