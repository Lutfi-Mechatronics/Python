


from gevent.threading import Thread
from os import name
# from time import time
# from time import ctime
import time
def timer(name, delay, repeat):
    print("timer:" + name + "started")
    while repeat >0:
        time.sleep(delay)
        print(name +" :"  + str(time.ctime(time.time())))
        repeat -=1
    print("timer : "+name+" completed")

def main():
    print("timer:" + name + "started")
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    # t3 = Thread(target=timer, args=("Timer3", 3, 5))
    # t4 = Thread(target=timer, args=("Timer4", 4, 5))
    t1.start()
    t2.start()
    # t3.start()
    # t4.start()

    print("Main completed")

if __name__ == '__main__':
    main()