# 三角形
def main(line):
    for i in range(line):
        for j in range(0, line - i):
            print(end=' ')
        for k in range(line - i, line):
            print('*', end=' ')
        print('')

if __name__ == '__main__':
    line_num = int(input('打印行数： '))
    main(line_num)

