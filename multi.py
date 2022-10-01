from multiprocessing import Pool
import os, time, random


def worker(task):
    t_start = time.time()
    print(task, os.getpid())


if __name__ == '__main__':

    po = Pool(3)
    for i in range(0,10):
        po.apply_async(worker, (i,))

    po.close
