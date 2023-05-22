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
        disc = {"""https://www.nykaa.com/rsvp-by-nykaa-fashion-beige-the-power-of-coord-set/p/5216375?productId=5216375&pps=1&skuId=5216351""":"""Product Details: This co-ord set features a crop top with square neckline, thick shoulder straps, centre front mock button placket and a smocked back for ease. It has a pair of flared pants with an elasticated back.

        Product Color: Beige.

        Fabric: Polyester Crepe with Polyester Knit Lining.

        Style Note: Feminine and stylish, this coord set is your go to for any ocassion! Style it with a strappy heels, a pendant necklace and a handbag for party or even vacation! - says Akshita Singh our inhouse stylist.

        Additional Information: Top length ranges from 11.3-13.18 inches; Palazzo length ranges from 40.25-42 inches.

        Fit: Comfort.

        Closure: Concealed side zipper and hook.""", """https://www.nykaa.com/twenty-dresses-by-nykaa-fashion-basics-navy-blue-slogan-printed-crop-tshirt/p/6583572?productId=6583572&pps=2&skuId=6583557""" : """This basic navy blue t-shirt from Twenty Dresses by Nykaa Fashion is a must-have. It gives your wardrobe a versatility of style and a breathable fit. Style with denim skirt, a pair of sneakers, and sunglasses to go on a long drive with your group of friends."""}

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
