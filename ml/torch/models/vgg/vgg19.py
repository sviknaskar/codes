import torch
import torch.nn as nn
from torchsummary import summary

img = torch.randn((1,3,224,224), dtype = torch.float32)

def getConvBlock(numFilters, inChannels = 3, numConvLayer = 3):
    convBlock = nn.Sequential()
    convBlock.append(nn.Conv2d(in_channels = inChannels, out_channels = numFilters, kernel_size=3, padding=1, stride=1, bias=False))
    convBlock.append(nn.ReLU())
    for i in range(numConvLayer - 1):
        convBlock.append(nn.Conv2d(in_channels = numFilters, out_channels = numFilters, kernel_size = 3, padding = 1, stride = 1, bias = False))
        convBlock.append(nn.ReLU())
    convBlock.append(nn.MaxPool2d(stride=2,kernel_size=2))

    return convBlock


class vgg19(nn.Module):
    def __init__(self):
        super(vgg19, self).__init__()
        self.allConvLayers = nn.Sequential()
        conf = [64, 128, 256, 512, 512]
        for i in range(len(conf)):
            if i == 0:
                self.allConvLayers.append(getConvBlock(inChannels = 3, numFilters = conf[i]))
            else:
                self.allConvLayers.append(getConvBlock(inChannels = conf[i - 1], numFilters=conf[i]))

        self.dense1 = nn.Linear(in_features = 512 * 7 * 7, out_features = 4096)
        self.dense2 = nn.Linear(in_features = 4096, out_features = 4096)
        self.dense3 = nn.Linear(in_features = 4096, out_features = 100)
        self.dropout = nn.Dropout(0.5)

    def forward(self, inImg):
        res = self.allConvLayers(inImg)
        # res2 = nn.Flatten(res)
        # print(res2.shape)
        print(res.shape)
        res = res.reshape(512 * 7 * 7)
        print(res.shape)
        res = self.dense1(res)
        res = self.dropout(res)
        res = self.dense2(res)
        res = self.dropout(res)
        res = self.dense3(res)
        return res

model = vgg19()
# model = getConvBlock(64)
res = model(img)
# summary(model, input_size=(3,256,256), batch_size=1)
print(res.shape)

# model1 = getConvBlock(64)
# model2 = getConvBlock(inChannels= 64, numFilters = 128)
# res = model1(img)
# print(res.shape)
# res2 = model2(res)
# print(res2.shape)

# model = nn.Sequential(model1, model2)
# summary(model, input_size=(3,256,256), batch_size=1)
