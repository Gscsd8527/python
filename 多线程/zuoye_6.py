if __name__=='__main__':
    import time
    # time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()
    # 的形式。如果参数未给或者为None的时候，将会默认time.time()
    # 为参数。它的作用相当于time.asctime(time.localtime(secs))。
    print(time.ctime(time.time()))
    # time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))