def looger(fn):
    def wrap(*arge,**kwarge):
        ret=fn(*arge,**kwarge)
        return ret
    return wrap
def show():
    print('小明')
foo=looger(show())