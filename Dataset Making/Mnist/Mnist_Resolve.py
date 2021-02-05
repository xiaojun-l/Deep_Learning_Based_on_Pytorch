# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:42:20 2021

@author: ziaoj
"""
#本程序对Minst数据集进行分解，将手写数字图像及对应的标签保存在本地文件夹下

#导入相关库
import torch
from torchvision import datasets,transforms
import os
from PIL import Image
import matplotlib.pyplot as plt

#清空变量、命令行语句及图窗
plt.close('all')

#加载数据集
train_dataset = datasets.MNIST(root='C:\\Users\\ziaoj\\data\\',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)
test_dataset = datasets.MNIST(root='C:\\Users\\ziaoj\\data\\',
                               train=False,
                               transform=transforms.ToTensor())

#显示训练集第1项及其标签
fig = plt.figure(1)
plt.imshow(train_dataset[0][0].numpy()[0])
fig.suptitle('Number '+str(train_dataset[0][1]))

fig2 = plt.figure(2)
plt.imshow(test_dataset[0][0].numpy()[0])
fig2.suptitle('Number '+str(test_dataset[0][1]))

#将数据集中的数据转换为JPG图像和文本标签并保存在本地文件夹下
#定义tensor转图片的函数 
def convert_to_img(Train,root):
    
    if Train:
        f = open(root+'train.txt','w')
        data_path = root + '\\train\\'
        dataset = train_dataset
    else:
        f = open(root+'test.txt','w')
        data_path = root + '\\test\\'
        dataset = test_dataset
    #如果不存在路径，则创建    
    if (not os.path.exists(data_path)):
        os.makedirs(data_path)
        
    for i,(img,label) in enumerate(dataset):
        img_path = data_path + str(i) + '.jpg';
        img_data = Image.fromarray(img.numpy()[0]*256)
        img_data.convert('L').save(img_path)
        tmp = str(label)
        f.write(img_path + ' ' + tmp + '\n')
        
    f.close()
    
root = 'E:\Pytorch_Learn\Datasets_Making\Mnist_Resolve2\\'
convert_to_img(True,root)
convert_to_img(False,root)

    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    