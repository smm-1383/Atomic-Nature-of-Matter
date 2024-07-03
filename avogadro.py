from sys import argv
from numpy import pi as p

av = './' + argv[1]

with open(av) as f:
    nums = [float(i) * 0.175 * 10 ** -6 for i in f.read().split('\n') if i]

D = sum(i ** 2 for i in nums) / len(nums) / 2

K = D * 6 * p * 5 * 10 * 9.135 * 10 ** -11 / 297
K1, K2 = str(K).split('e')

Na = 8.31446 / K
N1, N2 = str(Na).split('e')

print(f'Boltzmann: {float(K1):.4f}e{K2}')
print(f'Avogadro: {float(N1):.4f}e{N2}')
