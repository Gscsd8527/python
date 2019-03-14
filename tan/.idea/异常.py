try:
    a = 'str'
    b = 2
    print(a - b)
except Exception as e:
    print(e)
    print(e.args[0])