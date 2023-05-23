import numpy as np
import json
import argparse
from embedd import create_embeddings, decode_embeddings
from gather import *
import faiss

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
        prompt = create_embeddings(args.prompt)
        prompt = prompt.reshape(1,-1)
        index = faiss.read_index("my_index.index")
        D,I = index.search(prompt, 1)
        most_sim = I[0][0]
        most_similar_embedding = index.reconstruct(int(I[0][0]))
        with open('data.json') as file:
            data = json.load(file)

        for i in data.items():
            if np.array_equal(np.array(i[1]), most_similar_embedding):
                print(i[0])
    else:
        #parse_data(args.site, args.prompt)
        with open("raw_data.json") as file:
            disc = json.load(file)

        data = {}
        for i in disc.items():
            embedding = create_embeddings(i[1])
            data[i[0]] = embedding.tolist()
            embedding = embedding.reshape(1,-1)
            index = faiss.IndexFlatL2(embedding.shape[1])
            index.add(embedding)
            faiss.write_index(index, "my_index.index")

        json_data = json.dumps(data)
        with open('data.json', 'w') as file:
            file.write(json_data)
        print(data)



    pass
