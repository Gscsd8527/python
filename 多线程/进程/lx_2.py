import multiprocessing

def show_info(name, age):
    print(name, age)
if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=show_info, name='李云霄',  args=('古飞扬', 20))
    sub_process.start()
