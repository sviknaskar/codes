import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

def tensor2Image(imageTensor):
    return imageTensor.detach().swapaxes(0,2).numpy()




def doubleConv(inDim,outDim, stride = 1, padding = 0):
    layers = nn.Sequential(
        nn.Conv2d(in_channels = inDim, out_channels = outDim, kernel_size = 3, padding = padding, stride = stride, bias = False),
        nn.Conv2d(in_channels = outDim, out_channels = outDim, kernel_size = 3, padding = padding, stride = stride, bias = False),
        nn.ReLU()
    )
    return layers

def upSample(inDim, outDim):
    layer = nn.ConvTranspose2d(inDim, outDim, stride = 2, kernel_size= 2)
    return layer


class UNet(nn.Module):
    def __init__(self):
        super(UNet,self).__init__()
        self.maxPool = nn.MaxPool2d(kernel_size = 2, stride = 2)

        self.prepLayer = doubleConv(3,64)
        self.convDown_1 = doubleConv(64, 128)
        self.convDown_2 = doubleConv(128, 256)
        self.convDown_3 = doubleConv(256, 512)
        self.convDown_4 = doubleConv(512, 1024)

        self.convUp_1 = doubleConv(1024, 512, padding=0)
        self.convUp_2 = doubleConv(512, 256)
        self.convUp_3 = doubleConv(256, 128)
        self.convUp_4 = doubleConv(128, 64)

    def forward(self,image):
        prep = self.prepLayer(image)
        outDown_1 = self.maxPool(prep)
        outDown_2 = self.convDown_1(outDown_1)
        outDown_3 = self.maxPool(outDown_2)
        outDown_3 = self.convDown_2(outDown_3)
        outDown_4 = self.maxPool(outDown_3)
        outDown_4 = self.convDown_3(outDown_4)
        outDown_5 = self.maxPool(outDown_4)
        outDown_5 = self.convDown_4(outDown_5)

        outUp_1 = upSample(1024,512)(outDown_5)
        outUp_1 = F.pad(outUp_1,[4,4,4,4])
        outUp_1 = torch.cat([outDown_4, outUp_1], dim = 1)
        outUp_1 = self.convUp_1(outUp_1)
        print(f"{outUp_1.shape}")
        return outUp_1


model = UNet()
torch.manual_seed(32)
image = torch.randn((1,3,572,572),dtype = torch.float32)
res = model(image)
print(res.shape)


# plt.imshow(tensor2Image(image[0]))
# plt.show()

# layer = nn.ConvTranspose2d(1024,512,kernel_size = 2, stride = 2)
# img = torch.randn((1,1024,28,28), dtype = torch.float)
# res = layer(img)
# print(res.shape)
# res = F.pad(res, [4,4,4,4])
# print(res.shape)