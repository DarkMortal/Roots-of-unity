abs = lambda x: (x if x >= 0 else -x)
DELTA = 0.001

PI = 3.14159265359
full_angle = PI * 2
half_angle = PI / 2

def root(n:float, x: int) -> float:
    # Max and min are used to take into account numbers less than 1
    lo = min(1, n)
    hi = max(1, n)
    mid = 0.0

    # Update the bounds to be off the target by a factor of 10
    while(100 * lo * lo < n):
        lo *= 10
    while(0.01 * hi * hi > n):
        hi *= 0.1

    for i in range(100):
        mid = (lo + hi)/2
        val = mid ** x
        if(val == n): return mid
        if(val > n): hi = mid
        else: lo = mid
    return mid

def exp(x:float, steps = 11):
    quant = 1.0
    res = quant
    for i in range(1,steps):
        quant *= (x / float(i))
        res += quant
    return res

to_radians = lambda deg: ((deg % 360)/180.0) * PI

def range_check(func):

    def inner(*args):
        angle = (args[0] % full_angle) * (-1 if args[0] < 0 else 1)        
        return func(angle)
    
    return inner

@range_check
def cosine(x:float) -> float:
    if x == 0.0:
        return 1.0
    if abs(x) < DELTA:
        return x
    else:
        v = cosine(x / 2.0)
        return 2.0 * v * v - 1

@range_check
def sine(x:float) -> float:
    if abs(x) < DELTA:
        return x
    else:
        v = sine(x / 2.0)
        return 2.0 * v * root(1 - v * v, 2) * (-1 if x <= full_angle and x >= PI else 1)