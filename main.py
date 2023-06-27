import os
import argparse

from torch.backends import cudnn
from utils.utils import *

from solver import Solver


def str2bool(v): 
    return v.lower() in ('true')


def main(config):
    cudnn.benchmark = True
    if (not os.path.exists(config.model_save_path)):
        mkdir(config.model_save_path) 
    solver = Solver(vars(config))

    if config.mode == 'train':
        solver.train()
        solver.test()
    elif config.mode == 'test':
        solver.test()

    return solver
#gtx 2080 ti

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--lr', type=float, default=1e-4)
<<<<<<< HEAD
    parser.add_argument('--num_epochs', type=int, default=50)
    parser.add_argument('--k', type=int, default=-3)
    parser.add_argument('--win_size', type=int, default=3)
    parser.add_argument('--input_c', type=int, default=2)
    parser.add_argument('--output_c', type=int, default=2)
    parser.add_argument('--batch_size', type=int, default=50)
=======
    parser.add_argument('--num_epochs', type=int, default=10)
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--win_size', type=int, default=100)
    parser.add_argument('--input_c', type=int, default=2)
    parser.add_argument('--output_c', type=int, default=2)
    parser.add_argument('--batch_size', type=int, default=512)
>>>>>>> 0d1bc5124d73620c1121117f6f4856970808314f
    parser.add_argument('--pretrained_model', type=str, default=None)
    parser.add_argument('--dataset', type=str, default='credit')
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'])
    parser.add_argument('--data_path', type=str, default='C:/Users/user/Desktop/SLOWLAB/anomaly_transformer_in_stock_market/data')
    parser.add_argument('--model_save_path', type=str, default='checkpoints')
    parser.add_argument('--anormly_ratio', type=float, default=10.00)

    config = parser.parse_args()

    args = vars(config)
    print('------------ Options -------------')
    for k, v in sorted(args.items()):
        print('%s: %s' % (str(k), str(v)))
    print('-------------- End ----------------')
    main(config)