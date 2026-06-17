import torch
import torch.nn as nn

class Block(nn.Module):
    def __init__(self, inFeatures, outFeatures, downSample = None, stride = 1):
        super(Block, self).__init__()
        self.l1 = nn.Sequential(
            nn.Conv2d(in_channels = inFeatures, out_channels = outFeatures, kernel_size = 3, stride = 1, padding = 1),
            nn.BatchNorm2d(outFeatures),
            nn.ReLU()
        )
        self.l2 = nn.Sequential(
            nn.Conv2d(in_channels = outFeatures, out_channels = outFeatures, kernel_size=3, stride = 1, padding = 1),
            nn.BatchNorm2d(outFeatures),
        )
        self.downSample = downSample

    def forward(self, x):
        identity = x
        r = self.l1(x)
        r = self.l2(x)
        if self.identityDownSample is not None:
            identity = self.downSample(identity)
        r += identity
        r = nn.ReLU(r)
        return r





class BottleNeck(nn.Module):
    expansion = 4
    def __init__(self, inFeatures, outFeatures, stride = 1, isLast = False):
        super().__init__()
        self.isLast = isLast
        self.conv1x1_1 = nn.Sequential(
            nn.Conv2d(in_channels = inFeatures, out_channels = outFeatures, kernel_size = 1),
            nn.BatchNorm2d(outFeatures),
            nn.ReLU()
        )

        self.conv3x3_1 = nn.Sequential(
            nn.Conv2d(in_channels=outFeatures, out_channels=outFeatures, kernel_size=3, padding = 1, stride = stride),
            nn.BatchNorm2d(outFeatures),
            nn.ReLU()
        )

        self.conv1x1_2 = nn.Sequential(
            nn.Conv2d(in_channels = outFeatures, out_channels = outFeatures * self.expansion, kernel_size = 1),
            nn.BatchNorm2d(outFeatures * self.expansion),
        )

        self.shortcutLayers = []
        if stride != 1 or inFeatures != self.expansion * outFeatures:
            self.shortcutLayers.append(nn.Conv2d(inFeatures, outFeatures * self.expansion, kernel_size = 1, stride = stride, bias = False))
            self.shortcutLayers.append(nn.BatchNorm2d(outFeatures * self.expansion))

        self.shortcut = nn.Sequential(*self.shortcutLayers)


    def forward(self,x):
        res = self.conv1x1_1(x)
        res = self.conv3x3_1(res)
        res = self.conv1x1_2(res)
        res += self.shortcut(x)
        out = nn.ReLU(res)

        if self.isLast:
            return out, res
        else:
            return out



# l1= nn.Sequential(
#     nn.Conv2d(in_channels=3, out_channels=64, kernel_size = 3, stride = 1, padding = 1),
#     nn.BatchNorm2d(64)
# )
#
# l2= nn.Sequential(
#     nn.Conv2d(in_channels=64, out_channels=64, kernel_size = 3, stride = 1, padding = 1),
#     nn.BatchNorm2d(64)
# )
#
#
# model = nn.Sequential(l1,l2)
#
model = BottleNeck(3,64, isLast=True)
tImg = torch.randn((1,3,28,28), dtype = torch.float32)

res, residue = model(tImg)
print(residue.shape)

# res+=l1(tImg)
# print(res.shape)