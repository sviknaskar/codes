import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from dataprep.testImgGen import randImgGen as imGen
from torchsummary import summary
import cv2



def doubleConv(inDim, outDim):
    layers = nn.Sequential(
        nn.Conv2d(in_channels = inDim, out_channels = outDim, kernel_size = 3, stride = 1, padding = 1, bias = False),
        nn.Conv2d(in_channels = outDim, out_channels = outDim, kernel_size = 3, stride = 1, padding = 1, bias = False)
    )
    return layers

class UNetSimple(nn.Module):
    def __init__(self):
        super(UNetSimple,self).__init__()
        self.doubleConvDown_1 = doubleConv(3,64)
        self.doubleConvDown_2 = doubleConv(64, 128)
        self.doubleConvDown_3 = doubleConv(128,256)
        self.doubleConvDown_4 = doubleConv(256, 512)
        self.doubleConvUp_1 = doubleConv(512, 256)
        self.doubleConvUp_2 = doubleConv(256, 128)
        self.doubleConvUp_3 = doubleConv(128, 64)

        self.upsample_1 = nn.ConvTranspose2d(in_channels=512, out_channels = 256, kernel_size=2, stride=2, padding = 0, bias = False)
        self.upsample_2 = nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=2, stride=2, padding=0, bias=False)
        self.upsample_3 = nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=2, stride=2, padding=0,
                                             bias=False)

        self.maxPool = nn.MaxPool2d(kernel_size = 2, stride = 2)
        self.relu = nn.ReLU()

    def forward(self, img):
        x_1d = self.doubleConvDown_1(img)
        x_1d = self.relu(x_1d)

        x_2d = self.maxPool(x_1d)
        x_2d = self.doubleConvDown_2(x_2d)
        x_2d = self.relu(x_2d)

        x_3d = self.maxPool(x_2d)
        x_3d = self.doubleConvDown_3(x_3d)
        x_3d = self.relu(x_3d)

        x_4d = self.maxPool(x_3d)
        x_4d = self.doubleConvDown_4(x_4d)
        x_4d = self.relu(x_4d)

        x_5u = self.upsample_1(x_4d)
        x_5u = torch.cat([x_5u, x_3d], dim = 1)
        x_5u = self.doubleConvUp_1(x_5u)

        x_6u = self.upsample_2(x_5u)
        x_6u = torch.cat([x_6u, x_2d], dim=1)
        x_6u = self.doubleConvUp_2(x_6u)

        x_7u = self.upsample_3(x_6u)
        x_7u = torch.cat([x_7u, x_1d], dim=1)
        x_7u = self.doubleConvUp_3(x_7u)

        reconstructionlayer = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False),
            nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1, bias=False),
            nn.ReLU()
        )


        recImg = reconstructionlayer(x_7u)

        return recImg

# img = imGen(width=256,height=256,channels=3,imgType=torch.float)
img = cv2.imread("leaf.png")

# cv2.imshow("test", img)
# cv2.waitKey(0)

# imgTensor = torch.tensor(img).swapaxes(1,3)

imgTensor = torch.tensor(img, dtype = torch.float).swapaxes(0,2).unsqueeze(dim=0)
print(imgTensor.shape)
#
#
model = UNetSimple()
# print(model.named_parameters)
# model = doubleConv(3,64)
# res = model(imgTensor)
# resImg = res.detach().swapaxes(1,3).numpy()
# # print(res.shape)
# plt.imshow(resImg[0])
# plt.show()
summary(model, input_size=(3,572,572), batch_size=1)