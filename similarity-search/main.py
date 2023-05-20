import numpy as np
import argparse
from embedd import create_embeddings
from gather import *

parser = argparse.ArgumentParser(description='PyTorch U square net training on comma 10k dataset',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--mode', default="test", type=str,
                    help='operations', choices=["train","test"])

parser.add_argument('--prompt', default=None, type=str,
                    help='define a prompt, different functionallity for both train and test')

parser.add_argument('--site', default=None, type=str,
                    help='Site to parse data from, diff functions for every website')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.mode == "test":
        print(create_embeddings(args.prompt))

    else:
        parse_data(args.site, args.prompt)
    pass
