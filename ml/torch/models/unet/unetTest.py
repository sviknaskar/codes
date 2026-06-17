import os
import cv2
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import matplotlib.pyplot as plt
import segmentation_models_pytorch as smp
from torchvision import transforms
from PIL import Image
from tqdm import tqdm
from torchsummary import summary


dataDir = "D:/Projects/data/4unet/aerial_data/"
fileNames, maskNames = [], []
for file in os.listdir(dataDir+"imgs"):
    fileNames.append(dataDir +"imgs/" + file)

for file in os.listdir(dataDir+"masks"):
    maskNames.append(dataDir +"masks/" +file)

# print(f"{fileNames[0]}  {maskNames[0]}")


class segDataset(Dataset):
    def __init__(self, fileNames, maskNames, transform = None):
        self.imageNames = fileNames
        self.maskNames = maskNames
        self.transform = transform

    def __len__(self):
        return len(self.imageNames)

    def __getitem__(self, idx):
        img = cv2.imread(self.imageNames[idx])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if transforms is not None:
            imgP = Image.fromarray(img)
            imgP = self.transform(imgP)

        mask = cv2.imread(self.maskNames[idx])
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        if transforms is not None:
            maskP = Image.fromarray(mask)
            maskP = self.transform(maskP)
        return imgP, maskP


dataTransforms = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

data = segDataset(fileNames, maskNames, dataTransforms)
# print(f"data size : {len(data)}")

trainRatio = 0.8

trainSize = int(len(data) * trainRatio)
valSize = len(data) - trainSize

# print(f"{trainSize}     {valSize}")

# torch.manual_seed(112)
trainData, valData = random_split(data, [trainSize, valSize])

trainDataLoader = DataLoader(trainData, batch_size = 32, shuffle = True)
valDataLoader = DataLoader(valData, batch_size = 32, shuffle = True)

# segDataLoader = DataLoader(data, batch_size = 32, shuffle = True)

# print("pause")
img, mask = next(iter(valDataLoader))


# imgName = data.imageNames[0]
# print(imgName)

# model = smp.Unet(
#     encoder_name="resnet34",
#     encoder_weights="imagenet",
#     in_channels=3,
#     classes=1,
# )
# summary(model, input_size=(3,256,256))
#
# print(img[0].shape)

# print(img[0][0][0].max)
#
# res = model(img[0].unsqueeze(0))
# resMask = res[0][0].detach().numpy()
# print(resMask.shape)

plt.subplot(1,3,1)
plt.imshow(torch.swapaxes(img[0], 0, 2))

plt.subplot(1,3,2)
plt.imshow(torch.swapaxes(mask[0], 0, 2))
#
# plt.subplot(1,3,3)
# plt.imshow(resMask)
plt.show()

# print(f"{mask[0].shape}             {resMask.shape}")

# maskTmp = cv2.cvtColor(mask[0].detach().numpy(), cv2.CV_16FC1)
# maskTmp = cv2.Mat(mask[0][0].numpy())


def computeDiceCoeff(mask1, mask2, eps = 1e-6):
    intersection = (mask1* mask2)
    car1 = mask1.sum()
    car2 = mask2.sum()
    # return
    return (2*(intersection.sum()+eps) )/(car1+car2 + eps)


numEpochs = 2
device = "cpu"
if torch.cuda.is_available():
    device = "cuda"
print(device)

model = model.to(device)
criterion = computeDiceCoeff
optimizer = torch.optim.Adam(model.parameters(), lr = 0.00001)

for epochs in range(numEpochs):
    model.train()
    with tqdm(total = len(trainData)) as bar:
        for image, mask in trainDataLoader:
            optimizer.zero_grad()
            res = model(image)
            loss = criterion(res, mask)
            loss.backward()
            optimizer.step()
            bar.update()