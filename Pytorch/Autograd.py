import torch 
import math 

dtype = torch.float
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else torch.set_default_device(device)

x = torch.linspace(-1,1,200, dtype=dtype)
y = torch.exp(x)

a = torch.randn((), dtype=dtype, requires_grad=True)
b = torch.randn((), dtype=dtype, requires_grad=True)
c = torch.randn((), dtype=dtype, requires_grad=True)
d = torch.randn((), dtype=dtype, requires_grad=True)

initial_loss = 1
learning_rate = 1e-5 
for t in range(5000):
    y_pred = a + b*x +c*x **2 + d*x**3

    loss = (y_pred - y).pow(2).sum()
    if t==0:
        initial_loss = loss.item()
    
    if t % 100 == 99:
        print(f'Iteration t = {t:4d} loss(t)/loss(0) = {round(loss.item()/initial_loss, 6):10.6f} a = {a.item():10.6f} b = {b.item():10.6f} c = {c.item():10.6f} d = {d.item():10.6f}')
    loss.backward()

    with torch.no_grad():
        a -= learning_rate * a.grad
        b -= learning_rate * b.grad
        c -= learning_rate * c.grad
        d -= learning_rate * d.grad

        a.grad = None
        b.grad = None
        c.grad = None
        d.grad = None
print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')
