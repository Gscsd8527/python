from PIL import Image

imgname = 0
def pingjie(imgs):
    print('------------pingjie-------------')
    target = Image.new('RGB', (size * 2, size * 1))  #拼接前需要写拼接完成后的图片大小 1200*600
    for i in range(len(imgs)):
        a = size * i         # 图片距离左边的大小
        b = 0                # 图片距离上边的大小
        c = size * (i + 1)   # 图片距离左边的大小 + 图片自身宽度
        d = size             # 图片距离上边的大小 + 图片自身高度
        target.paste(imgs[i], (a, b, c, d))
        global imgname
        print('拼接图片的路径为：',path1 + str(imgname) + '.jpg')
        target.save(path1 + str(imgname) + '.jpg')
        imgname += 1

def pj():
    print('------------pj-------------')
    #取1,3是因为每行拼接完整都是最后那个，第一行是0，1命名，第二行是2,3命名，所以取后面那个值
    imglist = [1,3]
    img = []
    for i in imglist:
        print('完整行的拼接路径为：'+ path1 + str(i) + '.jpg')
        img.append(Image.open(path1 + str(i) + '.jpg'))
    target = Image.new('RGB', (size * 2, size * 2))  #拼接前需要写拼接完成后的图片大小 1200*1200
    for i in range(len(img)):
        a = 0  # 图片距离左边的大小
        b = size * i  # 图片距离上边的大小
        c = size * 2  # 图片距离左边的大小 + 图片自身宽度
        d = size * (i + 1)  # 图片距离上边的大小 + 图片自身高度
        target.paste(img[i], (a, b, c, d))
        global imgname
        target.save(path1 + 'pingjie' + '.jpg')

if __name__ == '__main__':
    size = 600  #图片的宽高都为600像素
    path = 'G:/img/img1/'  # 存放要拼接图片的目录
    path1 = 'G:/img/img2/' # 拼接后图片的存放目录
    index = 0  #图片的名字
    for i in range(2):  #有两行，所以需要循环两次
        images = [] #每一次拼接只能一行一行拼接，不能在第一行拼接完后再在其基础上拼接第二行的图片，矩阵不允许这样操作
        for j in range(2):  #每行有两张图片，所以也要循环两次
            print(path + str(index) + '.jpg')
            images.append(Image.open(path + str(index) + '.jpg'))
            index += 1
        print('第 {} 行拼接完成'.format(i))
        pingjie(images)
    pj()
