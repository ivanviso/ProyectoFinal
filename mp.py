from multiprocessing import Process
import time
def infiniprint(string,tiempo) :
    while True: 
        print(string)
        time.sleep(tiempo)
if __name__ == '__main__':
    p = Process(target=infiniprint, args=('a',1))
    p.start()
    p.join
if __name__ == '__main__':
    p = Process(target=infiniprint, args=('b',5))
    p.start()
    p.join
if __name__ == '__main__':
    p = Process(target=infiniprint, args=('c',10))
    p.start()
    p.join