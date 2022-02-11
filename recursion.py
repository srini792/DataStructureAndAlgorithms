def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

print(fac(5))


def count(n):
    if n==0:
        return 0
    else:
        return n+count(n-1)

print(count(2))

'''
count(2)
else: return 2+count(2-1)
count(1)
else: return 1+count(1-1)
count(0)
if : return 0
'''
