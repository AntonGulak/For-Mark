import math
import threading, time
import sympy as sy
from time import *


def integral(p):
    global count
    x = sy.Symbol('x')
    y = sy.sqrt(x)
    a = math.pi
    b = 2 * math.pi
    strap = 0
    step = 10e-7
    count = int((b // step))
    ai = a
    bi = step
    while count != 0:
        h = y.subs(x, (ai + bi) / 2)
        strap += 0.5 * (y.subs(x, ai) + y.subs(x, bi)) * step
        ai = bi
        bi += step
        count -= 1


if __name__ == "__main__":
    for p in range(2, 12, 2):
        threads = [threading.Thread(target=integral, args=(p,)) for i in range(1, p+1)]
        start = time()
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        stop = time()
        print(f'{p} потоков - {stop - start} мс.')