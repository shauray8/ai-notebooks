import numpy as np
import argparse
from embedd import create_embeddings
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
        print(most_sim)
        most_similar_embedding = index.reconstruct(most_sim)
        print(most_similar_embedding)
    else:
        #parse_data(args.site, args.prompt)
        disc = {"""https://www.nykaa.com/rsvp-by-nykaa-fashion-beige-the-power-of-coord-set/p/5216375?productId=5216375&pps=1&skuId=5216351""":"""Product Details: This co-ord set features a crop top with square neckline, thick shoulder straps, centre front mock button placket and a smocked back for ease. It has a pair of flared pants with an elasticated back.

        Product Color: Beige.

        Fabric: Polyester Crepe with Polyester Knit Lining.

        Style Note: Feminine and stylish, this coord set is your go to for any ocassion! Style it with a strappy heels, a pendant necklace and a handbag for party or even vacation! - says Akshita Singh our inhouse stylist.

        Additional Information: Top length ranges from 11.3-13.18 inches; Palazzo length ranges from 40.25-42 inches.

        Fit: Comfort.

        Closure: Concealed side zipper and hook.""", }

        data = {}
        for i in disc.items():
            embedding = create_embeddings(i[1])
            data[f"item1"] = {'URL' : i[0], 'embedding' : embedding,}
            embedding = embedding.reshape(1,-1)
            index = faiss.IndexFlatL2(embedding.shape[1])
            index.add(embedding)
            faiss.write_index(index, "my_index.index")
        print(data)



    pass
