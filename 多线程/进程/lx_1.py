import multiprocessing
import time
def main():
    while True:
        print('-------2------')
        time.sleep(1)

if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=main)
    sub_process.start()
    while True:
        print('-------1------')
        time.sleep(1)
