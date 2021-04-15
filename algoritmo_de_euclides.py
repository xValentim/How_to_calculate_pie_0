#algoritmo de Euclides
def mdc(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return mdc(b, r)

def is_co_prime(a, b):
    if mdc(a, b) == 1:
        return True
    else:
        return False
        
'''def mdc(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a'''

#print(mdc(93, 10))
#print(mdc(95, 10))





