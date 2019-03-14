from PIL import Image
img = Image.open('G:/img/1.jpg')
print('图片的大小为： {}'.format(img.size))
print('将图片切分成等四份，4张 600 X 600 的图片')
size = 600  #图片大小都为600，所以只设置一个变量
left = 0  #图片距离左边的宽度乘积值
shang = 0  #图片距离上边的宽度乘积值
index = 0  #图片名
for i in range(4):
    if i == 2:
        # 当循环到第三个值时，需要切第二行的图片
        shang += 1
        left = 0
    a = size * left  # 图片距离左边的大小
    b = size * shang  # 图片距离上边的大小
    c = size * (left + 1)  # 图片距离左边的大小 + 图片自身宽度
    d = size * (shang + 1)  # 图片距离上边的大小 + 图片自身高度
    print('a= {},b= {},c= {}, d= {}'.format(a,b,c,d))
    croping = img.crop((a,b,c,d))
    croping.save('G:/img/img1/'+ str(index) + '.jpg')
    index += 1
    left += 1
