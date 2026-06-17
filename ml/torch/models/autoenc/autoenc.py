import albumentations
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from torchsummary import summary
from torchvision import datasets, transforms
import albumentations as A
import cv2
import numpy


device = "cpu"
if torch.cuda.is_available():
    device = "cuda"

print(device)


def getEncoder(outFeatures, inFeatures=3, numBlocks = 2):
    enc = nn.Sequential(
        nn.Conv2d( in_channels = 3, out_channels = 16, kernel_size=3, padding = 1, stride = 1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size = 2, stride = 2),
        nn.Conv2d(in_channels = outFeatures, out_channels=8, kernel_size=3, padding=1, stride=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2)
    )
    return enc



def getDecoder():
    dec = nn.Sequential(
        nn.ConvTranspose2d(in_channels=8, out_channels=16, kernel_size=2, stride = 2, output_padding = 0),
        nn.ReLU(),
        nn.ConvTranspose2d(in_channels=16, out_channels=3, kernel_size=2, stride = 2, output_padding = 0),
        nn.Sigmoid()
    )
    return dec

#
# encModel = getEncoder(16)
# # summary(encModel, input_size = (3,64,64))
# decModel = getDecoder()
#
# tImg = torch.randn((1,3,64,64), dtype = torch.float32)
# res = encModel(tImg)
# res2 = decModel(res)
#
# print(res.shape)
# print(res2.shape)

class autoEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = getEncoder(16)

        self.decoder = getDecoder()
    def forward(self,x):
        res = self.encoder(x)
        res = self.decoder(res)
        return  res

# model = autoEncoder()
# tImg = torch.randn((1,3,64,64), dtype = torch.float32)
# res = model(tImg)
# print(res.shape)

dataTransformsA = A.Compose(
    [
        A.Resize(128,128),
        albumentations.ToTensorV2()
    ]
)

img = cv2.imread(f"D:/Projects/data/fruit/train/Banana/img_1521.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgResized = img
cv2.resize(img,(128,128),imgResized)
# plt.imshow(img)
# plt.show()

tImg = torch.tensor(img, dtype = torch.float32)
tImg = tImg.permute(2,0,1)
tImg = tImg.unsqueeze(0)
# print(tImg.shape)


dataTransforms = transforms.Compose(
    [
        transforms.Resize((128,128)),
        # transforms.ToTensor()
    ]
)


tImg = dataTransforms(tImg)
# tImg["image"].unsqueeze(0)
print(tImg.shape)



model = autoEncoder()
res = model(tImg)
imgRes = res[0].detach().permute(1,2,0).numpy()
plt.subplot(1,2,1)
plt.imshow(imgRes)
plt.subplot(1,2,2)
plt.imshow(imgResized)
plt.show()

crit = nn.MSELoss()
loss = crit(res, tImg)
print(loss)