def testError():
    n=1/0
try:
    testError()
except:
    print('除数不能为0')
