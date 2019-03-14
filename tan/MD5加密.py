import hashlib
encry = 'csdn'.encode('utf-8')
md5 = hashlib.md5()  #获取MD5对象
md5.update(encry)    #encry为加密内容
md5_value = md5.hexdigest() #md5.hexdigest()为加密结果
print(md5_value)

#   TypeError: Unicode-objects must be encoded before hashing

