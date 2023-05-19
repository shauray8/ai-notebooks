import torch
import numpy as np
from model import ModelM3

model = ModelM3()
model.load_state_dict(torch.load("./pretrained/E_1000_B_256.pth"))
model.eval()
def fetch(url):
    import requests, gzip, os, hashlib, numpy
    fp = os.path.join("./tmp", hashlib.md5(url.encode('utf-8')).hexdigest())
    if os.path.isfile(fp):
        with open(fp, "rb") as f:
            dat = f.read()
    else:
        with open(fp, "wb") as f:
            dat = requests.get(url).content
            f.write(dat)
    return numpy.frombuffer(gzip.decompress(dat), dtype=np.uint8).copy()
X_test = fetch("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")[0x10:].reshape((-1, 28, 28))
Y_test = fetch("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")[8:]

pred = model(torch.tensor(X_test[1].reshape(-1,1,28,28)).float())
print(torch.argmax(pred), Y_test[1])
