import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torch.optim as optim
import numpy as np

class networkConf:
    def __init__(self, inputD = 5, hiddenD = 20, latentD = 10):
        self.inputDim = inputD
        self.hiddenDim = hiddenD
        self.latentDim = latentD

class Encoder(nn.Module):
    def __init__(self, inputDim, hiddenDim, latentDim):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(inputDim, hiddenDim)
        self.fc2 = nn.Linear(hiddenDim, latentDim)
        self.relu = nn.ReLU()

    def forward(self, x):
        r = self.relu(self.fc1(x))
        r = self.fc2(r)
        return r

class Decoder(nn.Module):
    def __init__(self, inputDim, hiddenDim, latentDim):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latentDim, hiddenDim)
        self.fc2 = nn.Linear(hiddenDim, inputDim)
        self.relu = nn.ReLU()

    def forward(self, x):
        r = self.fc1(x)
        r = self.fc2(r)
        return r

class EncDec(nn.Module):
    def __init__(self, inputDim, hiddenDim, latentDim):
        super(EncDec, self).__init__()
        self.enc = Encoder(inputDim, hiddenDim, latentDim)
        self.dec = Decoder(inputDim, hiddenDim, latentDim)

    def forward(self, x):
        o = self.enc(x)
        o = self.dec(o)
        return o

def genData():
    return np.arange(0,50000,5).reshape(2000,5)

def lossFunc(x, y):
    return torch.sum(x-y)/x.shape[-1]

def trainModel(model, dataTensor, lossFunction, optimizer, epochs = 50):
    dataLoader = DataLoader(dataTensor)
    model.train()
    for epoch in range(epochs):
        totalLoss = 0
        for data in dataLoader:
            optimizer.zero_grad()
            x = model(data)
            loss = lossFunc(data, x)
            totalLoss += loss
            loss.backward()
            optimizer.step()
        print(f"{epoch} complete   total_loss:{totalLoss}")

    v = torch.tensor([3000, 3005, 3010, 3015, 3020], dtype = torch.float)
    res = model(v)
    print(res)



def main():
    conf = networkConf()
    # print(f"{conf.inputDim} {conf.hiddenDim} {conf.latentDim}")
    model = EncDec(conf.inputDim, conf.hiddenDim, conf.latentDim)
    d = genData()
    dataTensor = torch.tensor(d, dtype = torch.float)
    trainModel(model, dataTensor, lossFunc, optim.Adam(model.parameters(), lr=0.01))


if __name__ == "__main__":
    main()