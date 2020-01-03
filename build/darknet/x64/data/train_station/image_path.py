import os

path='/home/joelan/darknet/build/darknet/x64/data/train_station/yolos/'

imgList=os.listdir('image')

print(imgList)

textFile=open('train.txt','w')

for img in imgList:
    imgPath=path+img+'\n'
    textFile.write(imgPath)