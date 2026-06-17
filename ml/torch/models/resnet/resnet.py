import torch
from torch import nn
from torchviz import make_dot
# from torchview import draw_graph

class Bottleneck(nn.Module):
    def __init__(self, inChannels, middleChannels, expansionFactor, stride, isBottleneck):
        super(Bottleneck, self).__init__()
        self.inChannels = inChannels
        self.middleChannels = middleChannels
        self.expansionFactor = expansionFactor
        self.outChannels = self.middleChannels * self.expansionFactor
        self.stride = stride
        self.isBottleneck = isBottleneck
        self.isIdentity = False
        if self.inChannels == self.outChannels:
            isIdentity = True
        else:
            #1x1 conv layer
            projection = [nn.Conv2d(in_channels = self.inChannels,
                                    out_channels = self.outChannels,
                                    kernel_size = 1,
                                    stride = stride,
                                    padding = 0,
                                    bias = False
                                    )
                          ]
            #batchnorm layer
            projection.append(nn.BatchNorm2d(self.outChannels))
            self.projection = nn.Sequential(*projection)

        self.relu = nn.ReLU()
        if self.isBottleneck:
            self.conv1_1x1 = nn.Conv2d(in_channels=self.inChannels,
                                       out_channels=self.middleChannels,
                                       kernel_size=1,
                                       padding = 0,
                                       stride = 1,
                                       bias = False)
            self.batchNorm1 = nn.BatchNorm2d(self.middleChannels)
            self.conv2_3x3 = nn.Conv2d(in_channels=self.middleChannels,
                                       out_channels=self.middleChannels,
                                       kernel_size=3,
                                       padding = 1,
                                       stride = stride,
                                       bias = False)
            self.batchNorm2 = nn.BatchNorm2d(self.middleChannels)
            self.conv3_1x1 = nn.Conv2d(in_channels=self.middleChannels,
                                       out_channels=self.outChannels,
                                       kernel_size=1,
                                       padding=0,
                                       stride=1,
                                       bias=False)
            self.batchNorm3 = nn.BatchNorm2d(self.outChannels)

        else:
            self.conv1_3x3 = nn.Conv2d(in_channels=self.inChannels,
                                       out_channels=self.middleChannels,
                                       kernel_size=3,
                                       padding=1,
                                       stride=stride,
                                       bias=False)
            self.batchNorm1 = nn.BatchNorm2d(self.middleChannels)
            self.conv2_3x3 = nn.Conv2d(in_channels=self.middleChannels,
                                       out_channels=self.middleChannels,
                                       kernel_size=3,
                                       padding=1,
                                       stride=1,
                                       bias=False)
            self.batchNorm2 = nn.BatchNorm2d(self.middleChannels)

    def forward(self, x):
        xOrig = x
        if self.isBottleneck:
            x = self.relu(self.batchNorm1(self.conv1_1x1(x)))
            x = self.relu(self.batchNorm2(self.conv2_3x3(x)))
            x = self.batchNorm3(self.conv3_1x1(x))
        else:
            x = self.relu(self.batchNorm1(self.conv1_3x3(x)))
            x = self.batchNorm2(self.conv2_3x3(x))


        if self.isIdentity:
            x += xOrig
        else:
            x += self.projection(xOrig)
            # t = self.projection(xOrig)
            # print(f"{x.shape}    {t.shape}")


        x = self.relu(x)
        return x



# def TestBottleneck():
#     x = torch.randn(1,64,112,112)
#     model = Bottleneck(inChannels=64, middleChannels=64, expansionFactor=4, stride=4, isBottleneck=True)
#     out = model(x)
#     # dot = make_dot(out, params = dict(model.named_parameters()))
#     # dot.format = 'png'
#     # dot.render('./bottleneck')
#     # graph = draw_graph(model, x.shape, expand_nested=True)
#     # graph.visual_graph
#     # del model
#
# TestBottleneck()


class ResNet(nn.Module):
    def __init__(self, params, inChannels, numClasses):
        super(ResNet, self).__init__()
        self.layerSize = params[0]
        self.rep = params[1]
        self.expansion = params[2]
        self.isBottleneck = params[3]
        # print(f"{self.layerSize}  {self.rep}")

        initOutChannels = 64
        self.conv1 = nn.Conv2d(in_channels = inChannels, out_channels = initOutChannels, kernel_size = 7, padding = 3, stride = 2, bias = False)
        self.bn1 = nn.BatchNorm2d(initOutChannels)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d(kernel_size = 3, stride = 2, padding = 1)
        self.averagepool = nn.AdaptiveAvgPool2d(1)
        self.fc1 = nn.Linear(self.layerSize[-1]*self.expansion, numClasses)
        self.block1 = self.GenerateBlock(initOutChannels, self.layerSize[0], self.rep[0], self.expansion, self.isBottleneck, 1)
        self.block2 = self.GenerateBlock(self.layerSize[0]*self.expansion, self.layerSize[1], self.rep[1],
                                         self.expansion,self.isBottleneck, 2)
        self.block3 = self.GenerateBlock(self.layerSize[1] * self.expansion, self.layerSize[2], self.rep[2],
                                         self.expansion, self.isBottleneck, 2)
        self.block4 = self.GenerateBlock(self.layerSize[2] * self.expansion, self.layerSize[3], self.rep[3],
                                         self.expansion, self.isBottleneck, 2)

        # for i in range(len(self.block1)):
        #     print(self.block1[i].named_parameters)


    def GenerateBlock(self, inChannels, midChannels, rep, expansion, isBottleNeck, stride):
        block = [Bottleneck(inChannels=inChannels, middleChannels=midChannels,
                            expansionFactor= expansion, isBottleneck=True, stride=stride)]
        for i in range(1, rep):
            block.append(Bottleneck(inChannels=midChannels*expansion, middleChannels=midChannels,
                                    expansionFactor= expansion, isBottleneck=True, stride=1))
        return nn.Sequential(*block)

    def forward(self, x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.maxpool(x)

        x = self.block1(x)

        x = self.block2(x)

        x = self.block3(x)

        x = self.block4(x)

        x = self.average_pool(x)

        x = torch.flatten(x, start_dim=1)
        x = self.fc1(x)

        return x




modelParam = {'resnet50':[[64, 128, 256, 512],[3, 4, 6, 3],4,True]}
# print(modelParam['resnet50'])
model = ResNet(modelParam['resnet50'],3,1000)
x = torch.randn(1, 3, 224, 224)
output = model(x)
print(model.parameters)