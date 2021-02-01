import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim
from tqdm import trange


X = np.random.randint(1,9,(1000,2))
y = np.prod(X,axis=1).reshape(1000,1)

X,y = torch.from_numpy(X)*.1, torch.from_numpy(y)*1.

class mul(nn.Module):
    def __init__(self):
        super(mul,self).__init__()
        self.l1 = nn.Linear(2,4)
        self.act = nn.ReLU()
        self.l2 = nn.Linear(4,1)

    def forward(self, x):
        x = self.l1(x)
        x = self.act(x)
        x = self.l2(x)
        return x

net = mul().to('cuda')

optimizer = optim.Adam(net.parameters())
loss_function = nn.BCELoss()

net.train()

for epoch in (n:=trange(100)):
    X = X.to('cuda')
    y = y.to('cuda')
    output = net(X)
    loss = loss_function(output, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    n.set_description(f'{epoch}, loss = {loss.item()}')


with torch.no_grad():
    X = torch.tensor([2.,2.]).to('cuda')
    output = net(X)
    print(output)
