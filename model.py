### 1.批量命名图片
import os
import csv
import codecs

#批量命名图片
path = r"/home/aistudio/data_image/train"
fileList = os.listdir(path)  # 待修改文件夹
os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
f = csv.reader(codecs.open('/home/aistudio/data/data48784/train_label.csv','r','utf-8'))
next(f)
for i in f:
    print(i[1])
    if(i[0]!=os.name):
        os.rename(i[0], ('%s'+'.jpg')%i[1])  # 文件重新命名
        
### 2.将图片转换成灰度图

from PIL import Image

#灰度图
def Image2GRAY(path):
    # 获取临时文件夹中的所有图像路径
    for item in range(1,5001):
        # 使图像灰度化并保存
        im = Image.open(path + '/%s.jpg'%item).convert('L')
        im.save('/home/aistudio/GrayscaleImage' + '/%s.jpg'%item)

if __name__ == '__main__':
    # 临时数据存放路径
    path = '/home/aistudio/data_image/test'
    Image2GRAY(path)
    
### 3.切割图片并分类
import uuid

#切割图片并分类
class YanZhenMaUtil():
    def __init__(self):
        pass

    def splitimage(self, src, dstpath):
        name = src.split('/')
        name1 = name[name.__len__() - 1]
        name2 = name1.split('.')[0]
        l1 = list(name2)
        img = Image.open(src) #把每张图片裁成四张25*40的小图片
        box = [(9, 0, 34, 40),(34, 0, 59, 40),(59, 0, 84, 40),(84, 0, 109, 40)]
        for item in range(4):
            if l1[item].isdigit():
                path1 = dstpath + '/%s' % l1[item]
            elif l1[item].islower():
                path1 = dstpath + '/%s%s' %(l1[item],l1[item])
            elif l1[item].isupper():
                path1 = dstpath + '/%s' % l1[item]

            if not os.path.exists(path1):
                os.makedirs(path1)

            img.crop(box[item]).save(path1 + '/%s_.png' % uuid.uuid1())
            print(item)

if __name__ == '__main__':
    root_path = '/home/aistudio/data_image/train/' # 目标文件夹（被切分的图片）
    dstpath = '/home/aistudio/data_image/data' # 切分后保存图片的路径
    imgs = os.listdir(root_path)
    yanZhenMaUtil = YanZhenMaUtil()
    for src in imgs:
        src = root_path + src
        yanZhenMaUtil.splitimage(src=src, dstpath=dstpath)
