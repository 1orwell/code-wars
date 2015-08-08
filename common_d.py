def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(args):
    return reduce(lcm, args)

def convertFracts(lst):
    arg = [i[1] for i in lst ]
    lcm = lcmm(arg)
    for frac in lst:
        mult = int(lcm / frac[1])
        frac[1] = lcm
        frac[0] = frac[0] * mult
    return lst

print convertFracts([[6, 12], [4, 3], [1, 6]])
