# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:21:20 2021

@author: ziaoj
"""
'''创建自己的数据集'''

#导入相关库
from torchvision import transforms as transforms
from torch.utils.data import Dataset
from PIL import Image
import matplotlib.pyplot as plt


#以torch.utils.data.Dataset为基类创建MyDataset
class MyDataset(Dataset):
    #step1:初始化
    def __init__(self,txt,transform=None,target_transform=None):
        fh = open(txt,'r')   #打开标签文件
        imgs = []            #创建列表，装东西
        for line in fh:      #遍历标签文件每行
            line = line.rstrip()#删除字符串末尾的空格
            words = line.split()#能过空格分割字符串，变成列表
            imgs.append((words[0],int(words[1])))#把图片名words[0],标签int(words[1])组成元组放在imgs里

        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform
        
    def __getitem__(self,index):#检索函数
        fn,label = self.imgs[index]#读取文件名、标签
        img = Image.open(fn).convert('L')#通过PIL.Image读取图片
        if self.transform is not None:
            img = self.transform(img)
        return img,label
    
    def __len__self(self):
        return len(self.imgs)
    
trans_form = transforms.Compose([transforms.ToTensor()])

train_data = MyDataset(txt='E:\\Pytorch_Learn\\Datasets_Making\\Mnist_Resolve2\\train.txt',transform=trans_form)
test_data = MyDataset(txt='E:\\Pytorch_Learn\\Datasets_Making\\Mnist_Resolve2\\test.txt',transform=trans_form)

plt.figure(1)
fig=plt.subplot(1,2,1)
plt.imshow(train_data[0][0].numpy()[0])
fig.set_title(str(train_data[0][1]))

fig2=plt.subplot(1,2,2)
plt.imshow(test_data[0][0].numpy()[0])
fig2.set_title(str(test_data[0][1]))