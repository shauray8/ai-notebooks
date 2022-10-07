from graphviz import Digraph
from tqdm import trange
import math
import numpy as np
import matplotlib.pyplot as plt
import random


## defining float as Value (it's actually the same just a different word)
class Value:
  def __init__(self,data,_children=(),_op="",label=""):
    self.data = data
    self._prev = set(_children)
    self._op = _op
    # represents the derivative of the output wrt to that perticular variable 
    self.grad = 0.0
    self.label = label
    self._backward = lambda: None
      
  ## python internlly uses this function to return the data
  def __repr__(self):
    return f"Value(data={self.data})"
  
  def __add__(self,other):
    other = other if isinstance(other, Value) else Value(other)
    out = Value(self.data + other.data, (self, other),"+")
    
    def _backward():
      self.grad += 1.0 * out.grad
      other.grad += 1.0 * out.grad

    out._backward = _backward
    return out

  def backward(self):
    topo = []
    visited = set()
    def build_topo(v):
      if v not in visited:
        visited.add(v)
        for child in v._prev:
          build_topo(child)
        topo.append(v)
    build_topo(self)

    self.grad = 1.0
    for node in reversed(topo):
      node._backward()
  
  def __mul__(self, other):
    other = other if isinstance(other, Value) else Value(other)
    out = Value(self.data * other.data, (self, other),"*")
    def _backward():
      self.grad += other.data * out.grad
      other.grad += self.data * out.grad
    out._backward = _backward
    return out

  def __rmul__(self, other):
    return self * other

  def __radd__(self, other):
    return self + other

  def tanh(self):
    x = self.data
    t = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
    out = Value(t, (self, ), 'tanh')

    def _backward():
      self.grad += (1 - t**2) * out.grad
    out._backward = _backward

    return out

  def __neg__(self):
    return self * -1

  def __sub__(self,other):
    return self + (-other)


  def exp(self):
    x = self.data
    out = Value(math.exp(x), (self, ), 'exp')

    def _backward():
      self.grad += out.data * out.grad
    out._backward = _backward

    return out

  def __truediv__(self, other):
    return self * other ** -1

  def __pow__(self, other):
    assert isinstance(other, (int, float)), "only supporting int/float powers for now"
    out = Value(self.data**other, (self,),f"**{other}")

    def _backward():
      self.grad += other * (self.data ** (other-1)) * out.grad
    out._backward = _backward

    return out

  ## add log sum exp maybe in the future for activation 
  # this is how it works
  # log(exp(x1)+....+exp(xn))

  ## add RELU 

      

## helper function for getting the tree and stuff
def trace(root):
    nodes, edges = set(),set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child,v))
                build(child)
    build(root)
    return nodes, edges
    

## draws the actuall tree 
def draw_dot(root):
    dot = Digraph(format="svg", graph_attr={'rankdir':"LR"})
    
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        dot.node(name=uid, label = "{ %s | data %.4f | grad %.4f }" % (n.label ,n.data, n.grad), shape='record')
        if n._op:
            dot.node(name= uid + n._op, label = n._op)
            dot.edge(uid + n._op, uid)
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    
    return dot


## viz function for a little change in some variable can effect the other 
def lol():
  h = 1e-7
  a = Value(2.0,label="a")
  b = Value(-3.0,label="b")
  c = Value(10.0,label="c")
  e = a*b; e.label="e"
  d = e+c; d.label="d"
  f = Value(-2.0, label="f")
  L = d*f 
  L.label="L"
  L1 = L.data

  a = Value(2.0 + h,label="a")
  b = Value(-3.0,label="b")
  c = Value(10.0,label="c")
  e = a*b; e.label="e"
  d = e+c; d.label="d"
  f = Value(-2.0, label="f")
  L = d*f 
  L.label="L"
  L2 = L.data

  print((L2-L1)/h)


## variables for the example
def first_example():
  a = Value(2.0,label="a")
  b = Value(-3.0,label="b")
  c = Value(10.0,label="c")
  e = a*b; e.label="e"
  d = e+c; d.label="d"
  f = Value(-2.0, label="f")
  L = d*f 
  L.label="L"
  print(L)

## gradients calculated 
  L.grad = 1
  d.grad = f.data
  f.grad = d.data
### dl/dc = dl/dd * dd/dc
  c.grad = d.grad * 1
  e.grad = d.grad * 1
### dl/da = dl/de * de/da
  a.grad = e.grad * b.data
  b.grad = e.grad * a.data



## rerunnning the forward pass
### we nudged the variables in the direction of gradient so we expect the output to go up 
## which means a less negative output 
def doing_what_the_comment_says():
  a.data += 0.01 * a.grad
  b.data += 0.01 * b.grad
  c.data += 0.01 * c.grad
  f.data += 0.01 * f.grad

  e = a*b; e.label="e"
  d = e+c; d.label="d"
  f = Value(-2.0, label="f")
  L = d*f 
  L.label="L"
  print("nudged output",L)

## neuron
### bias in the inert happiness 
### activation function is some kind of squishing function 

x1 = Value(2.0, label="x1")
x2 = Value(0.0, label="x2")
w1 = Value(-3.0, label="w1")
w2 = Value(1.0, label="w2")
b = Value(6.8813, label="b")
x1w1 = x1*w1; x1w1.label="x1*w1"
x2w2 = x2*w2; x2w2.label="x2*w2"
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label="x1*w1 + x2*w2"
n = x1w1x2w2 + b; n.label = "n"
## ----- changing the expression for tanh
#e = (2*n).exp()
#o = (e-1) / (e+1)
## ----- code ends here 

## sigmoid
e = (-n).exp()
o = Value(1.) / (e+1)

o.label = "o"

o.backward()

def still_a_lot_of_manual_labour():
  o.grad = 1.0
  o._backward()
  n._backward()
  x1w1x2w2._backward()
  x1w1._backward()
  x2w2._backward()


def no_more_calculating_the_grad():
## calculating the gradients for the above stuff
  o.grad = 1
  n.grad = 1 - (o.data)**2

## do/db = do/dn * dn/db = n.grad * 1
## do/dxw = do/dn * dn/dxw = n.grad * 1
  b.grad = n.grad
  x1w1x2w2.grad = n.grad

## do/x1w1 = do/dxw * dxw/dx1w1 = n.grad * 1
## do/x2w2 = do/dxw * dxw/dx2w2 = n.grad * 1
  x1w1.grad = n.grad
  x2w2.grad = n.grad

## do/dx1 = do/x1w1 * dx1w1/dx1 = n.grad * w1.data
## do/dw1 = do/x1w1 * dx1w1/dw1 = n.grad * x1.data
  x1.grad = n.grad * w1.data
  w1.grad = n.grad * x1.data
  x2.grad = n.grad * w2.data
  w2.grad = n.grad * x2.data


## defining a Neuron

class Module:
  def zero_grad(self):
    for p in n.parameters():
      p.grad = 0.0
      
    def parameters(self):
      return []
      
class Neuron(Module):

    def __init__(self, nin):
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(0)

    def __call__(self, x):
        act = sum((wi*xi for wi,xi in zip(self.w, x)), self.b)
        return act.tanh()

    def parameters(self):
        return self.w + [self.b]

class Layer(Module):

    def __init__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, x):
        out = [n(x) for n in self.neurons]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]


class MLP(Module):

    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
          x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]



x = [1.,2.,3.]
n = MLP(3 ,[4,4,1])


#print(n(x))

xs = [[2.,3.,-1.],
[3.,-1.,.5],
[.5,1.,1.],
[1.,1.,-1.],
]

ys = [1.,-1.,1.,1.]


for _ in (w := trange(1000)):
    
  ## forward pass

  ypred = [n(x) for x in xs]
  #print(ypred)
  ## mean squared error loss
  loss = sum([(yout - ygt)**2 for ygt, yout in zip(ys, ypred)])

  # zero the gradient 
  n.zero_grad()

  #print("loss",loss)
  loss.backward()
  #print("grad",n.layers[0].neurons[0].w[0].grad)
  #print("data",n.layers[0].neurons[0].w[0].data)

  #print(len(n.parameters()))

  # update

  # define optimizer (pytorch style) and then create a step function for this
  # write a legit LR decay 
  # https://medium.com/analytics-vidhya/learning-rate-decay-and-methods-in-deep-learning-2cee564f910b

  LR = .05
  for p in n.parameters():
    p.data -= LR * p.grad

  w.set_description(f"No. of steps : {_}; loss : {loss.data} ; LR : {LR}")


print(ypred)
print(n.parameters())
print(n.layers[0].neurons[0].w[0].grad)
print(n)

## prints to stdout 

#dot = draw_dot(n(xs))
#dot.render()
