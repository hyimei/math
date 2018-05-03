def euclidean(a, b):
    q = a // b
    r = a % b

    if r == 0:
        return (1, 1-q)
    (m, n) = euclidean(b, r)
    return (n, m-q*n)

def verify_euc(a, b, d, e):
    (x, y) = e
    return a * x + b * y == d

e1 = euclidean(314, 159)
print('find (x, y) such that 314x + 159y = 1, result=', e1)
print('verify result', verify_euc(314, 159, 1, e1))
# there is other solution (-40, 79) 
print('verify result', verify_euc(314, 159, 1, (-40, 79))) 

'''
python3 euclidean_algorithm.py 
find (x, y) such that 314x + 159y = 1, result= (119, -235)
verify result True
verify result True
'''
