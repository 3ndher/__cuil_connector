import math

U = .9
C = .2
I = .6
S = .4
F = .6
A = .4
prob = ((U+C+I) * (10-S))/20 * A * 1/(1-math.sin(F/10))
print(prob)