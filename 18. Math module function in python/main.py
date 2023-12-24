# Import math module and functions
import math
from math import *




# Many functions regarding math modules in python can be find using helf(math) method.
help(math)



nlis = []
nlis.append(math.acos(1))
nlis.append(math.acos(-1))
print(nlis)


print(math.acosh(1729))



nlis = []
nlis.append(math.asin(1))
nlis.append(math.asin(-1))
print(nlis)


print(math.asinh(1729))


nlis = []
nlis.append(math.atan(math.inf)) # pozitive infinite
nlis.append(math.atan(-math.inf)) # negative infinite
print(nlis)




print(math.atan2(1729, 37))
print(math.atan2(1729, -37))
print(math.atan2(-1729, -37))
print(math.atan2(-1729, 37))
print(math.atan2(math.pi, math.inf))
print(math.atan2(math.inf, math.e))
print(math.atan2(math.tau, math.pi))



nlis=[]
nlis.append(math.atanh(-0.9999))
nlis.append(math.atanh(0))
nlis.append(math.atanh(0.9999))
print(nlis)




pi_number = math.pi # math.pi is equal to pi_number 3.14.
print(f'The nearest integer greater than pi number is {math.ceil(pi_number)}.')



print(f'The combination of 6 with 2 is {math.comb(6, 2)}.')
print(math.comb(10, 3.14)) # It returns a TypeError


print(f'The copysign of thes two numbers -3.14 and 2.718 is {math.copysign(-3.14, 2.718)}.')
print(f'The copysign of thes two numbers 1729 and -0.577 is {math.copysign(1729, -0.577)}.')




print(math.cos(0))
print(math.cos(math.pi/6))
print(math.cos(-1))
print(math.cos(1))
print(math.cos(1729))
print(math.cos(90))



nlis = []
nlis.append(math.cosh(1))
nlis.append(math.cosh(0))
nlis.append(math.cosh(-5))
print(nlis)


nlis = []
nlis.append(math.degrees(math.pi/2))
nlis.append(math.degrees(math.pi))
nlis.append(math.degrees(math.pi/4))
nlis.append(math.degrees(-math.pi))
print(nlis)



print(math.dist([30], [60]))
print(math.dist([0.577, 1.618], [3.14, 2.718]))
x = [0.577, 1.618, 2.718]
y = [6, 28, 37]
print(math.dist(x, y))





nlis = []
nlis.append(math.erf(math.inf))
nlis.append(math.erf(math.pi))
nlis.append(math.erf(math.e))
nlis.append(math.erf(math.tau))
nlis.append(math.erf(0))
nlis.append(math.erf(6))
nlis.append(math.erf(1.618))
nlis.append(math.erf(0.577))
nlis.append(math.erf(-math.inf))
print(nlis)




nlis = []
nlis.append(math.erfc(math.inf))
nlis.append(math.erfc(math.pi))
nlis.append(math.erfc(math.e))
nlis.append(math.erfc(math.tau))
nlis.append(math.erfc(0))
nlis.append(math.erfc(6))
nlis.append(math.erfc(1.618))
nlis.append(math.erfc(0.577))
nlis.append(math.erfc(-math.inf))
print(nlis)



nlis = []
nlis.append(math.exp(math.inf))
nlis.append(math.exp(math.pi))
nlis.append(math.exp(math.e))
nlis.append(math.exp(math.tau))
nlis.append(math.exp(0))
nlis.append(math.exp(6))
nlis.append(math.exp(1.618))
nlis.append(math.exp(0.577))
nlis.append(math.exp(-math.inf))
print(nlis)




nlis = []
nlis.append(math.expm1(math.inf))
nlis.append(math.expm1(math.pi))
nlis.append(math.expm1(math.e))
nlis.append(math.expm1(math.tau))
nlis.append(math.expm1(0))
nlis.append(math.expm1(6))
nlis.append(math.expm1(1.618))
nlis.append(math.expm1(0.577))
nlis.append(math.expm1(-math.inf))
print(nlis)



print(f'The absolute value of the number -1.618 is {math.fabs(-1.618)}.')



print(f'The factorial of the number 6 is {math.factorial(6)}.')


# Factorial of negative numbers returns a ValueError.
print(math.factorial(-6))


# Factorial of non-unteger numbers returns a TypeError.
print(math.factorial(3.14))



print(math.floor(3.14))


print(math.fmod(37, 6))
print(math.fmod(1728, 37))


print(math.frexp(2.718))


special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(math.fsum(special_nums))


print(math.gamma(3.14))
print(math.gamma(6))
print(math.gamma(2.718))



print(math.gcd(3, 10))
print(math.gcd(4, 8))
print(math.gcd(0, 0))


print(math.hypot(3, 4))
print(math.hypot(5, 12))
print(math.hypot(8, 15))


print(math.isclose(math.pi, math.tau)) # tau number is 2 times higher than pi number
print(math.isclose(3.14, 2.718))
print(math.isclose(3.14, 1.618))
print(math.isclose(10, 5, rel_tol = 3, abs_tol=0))
print(math.isclose(3.14, 3.1400000000001))



nlis = []
nlis.append(math.isfinite(math.inf))
nlis.append(math.isfinite(math.pi))
nlis.append(math.isfinite(math.e))
nlis.append(math.isfinite(math.tau))
nlis.append(math.isfinite(0))
nlis.append(math.isfinite(6))
nlis.append(math.isfinite(1.618))
nlis.append(math.isfinite(0.577))
nlis.append(math.isfinite(-math.inf))
nlis.append(math.isfinite(float('NaN')))
nlis.append(math.isfinite(float('inf')))
print(nlis)


nlis = []
nlis.append(math.isinf(math.inf))
nlis.append(math.isinf(math.pi))
nlis.append(math.isinf(math.e))
nlis.append(math.isinf(math.tau))
nlis.append(math.isinf(0))
nlis.append(math.isinf(6))
nlis.append(math.isinf(1.618))
nlis.append(math.isinf(0.577))
nlis.append(math.isinf(-math.inf))
print(nlis)



nlis = []
nlis.append(math.isnan(float('NaN')))
nlis.append(math.isnan(math.inf))
nlis.append(math.isnan(math.pi))
nlis.append(math.isnan(math.e))
nlis.append(math.isnan(math.tau))
nlis.append(math.isnan(0))
nlis.append(math.isnan(6))
nlis.append(math.isnan(1.618))
nlis.append(math.isnan(0.577))
nlis.append(math.isnan(-math.inf))
nlis.append(math.isnan(math.nan))
print(nlis)



print(math.isqrt(4))
print(math.isqrt(5))
print(math.isqrt(-5))



print(math.isqrt(3.14))


nlis = []
nlis.append(math.lcm(3, 5, 25))
nlis.append(math.lcm(9, 6, 27))
nlis.append(math.lcm(21, 27, 54))
print(nlis)



print(math.ldexp(20, 4))
print(20*(2**4))

print(math.gamma(6))
print(math.lgamma(6))
print(math.log(120)) # print(math.gamma(6)) = 120



nlis = []
nlis.append(math.log(90))
nlis.append(math.log(1))
nlis.append(math.log(math.e))
nlis.append(math.log(math.pi))
nlis.append(math.log(math.tau))
nlis.append(math.log(math.inf))
nlis.append(math.log(math.nan))
print(nlis)



nlis = []
nlis.append(math.log10(90))
nlis.append(math.log10(1))
nlis.append(math.log10(math.e))
nlis.append(math.log10(math.pi))
nlis.append(math.log10(math.tau))
nlis.append(math.log10(math.inf))
nlis.append(math.log10(math.nan))
print(nlis)


nlis = []
nlis.append(math.log1p(90))
nlis.append(math.log1p(1))
nlis.append(math.log1p(math.e))
nlis.append(math.log1p(math.pi))
nlis.append(math.log1p(math.tau))
nlis.append(math.log1p(math.inf))
nlis.append(math.log1p(math.nan))
print(nlis)



nlis = []
nlis.append(math.log2(90))
nlis.append(math.log2(2))
nlis.append(math.log2(1))
nlis.append(math.log2(math.e))
nlis.append(math.log2(math.pi))
nlis.append(math.log2(math.tau))
nlis.append(math.log2(math.inf))
nlis.append(math.log2(math.nan))
print(nlis)



print(math.modf(math.pi))
print(math.modf(math.e))
print(math.modf(1.618))


nlis = []
nlis.append(math.nextafter(3.14, 90))
nlis.append(math.nextafter(6, 2.718))
nlis.append(math.nextafter(3, math.e))
nlis.append(math.nextafter(28, math.inf))
nlis.append(math.nextafter(1.618, math.nan))
nlis.append(math.nextafter(1, 1))
nlis.append(math.nextafter(0, 0))
print(nlis)




print(math.perm(6, 2))
print(math.perm(6, 6))


print(math.pow(10, 2))
print(math.pow(math.pi, math.e))


special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(math.prod(special_nums))




nlis = []
nlis.append(math.radians(0))
nlis.append(math.radians(30))
nlis.append(math.radians(45))
nlis.append(math.radians(60))
nlis.append(math.radians(90))
nlis.append(math.radians(120))
nlis.append(math.radians(180))
nlis.append(math.radians(270))
nlis.append(math.radians(360))
print(nlis)




nlis = []
nlis.append(math.remainder(3.14, 2.718))
nlis.append(math.remainder(6, 28))
nlis.append(math.remainder(5, 3))
nlis.append(math.remainder(1729, 37))
print(nlis)



nlis = []
nlis.append(math.sin(math.pi))
nlis.append(math.sin(math.pi/2))
nlis.append(math.sin(math.e))
nlis.append(math.sin(math.nan))
nlis.append(math.sin(math.tau))
nlis.append(math.sin(30))
nlis.append(math.sin(-5))
nlis.append(math.sin(37))
print(nlis)




nlis = []
nlis.append(math.sinh(1))
nlis.append(math.sinh(0))
nlis.append(math.sinh(-5))
nlis.append(math.sinh(math.pi))
nlis.append(math.sinh(math.e))
nlis.append(math.sinh(math.tau))
nlis.append(math.sinh(math.nan))
nlis.append(math.sinh(math.inf))
print(nlis)


nlis = []
nlis.append(math.sqrt(1))
nlis.append(math.sqrt(0))
nlis.append(math.sqrt(37))
nlis.append(math.sqrt(math.pi))
nlis.append(math.sqrt(math.e))
nlis.append(math.sqrt(math.tau))
nlis.append(math.sqrt(math.nan))
nlis.append(math.sqrt(math.inf))
print(nlis)




nlis = []
nlis.append(math.tan(0))
nlis.append(math.tan(30))
nlis.append(math.tan(45))
nlis.append(math.tan(60))
nlis.append(math.tan(90))
nlis.append(math.tan(120))
nlis.append(math.tan(180))
nlis.append(math.tan(270))
nlis.append(math.tan(360))
print(nlis)



nlis = []
nlis.append(math.tanh(1))
nlis.append(math.tanh(0))
nlis.append(math.tanh(-5))
nlis.append(math.tanh(math.pi))
nlis.append(math.tanh(math.e))
nlis.append(math.tanh(math.tau))
nlis.append(math.tanh(math.nan))
nlis.append(math.tanh(math.inf))
print(nlis)



nlis = []
nlis.append(math.trunc(1))
nlis.append(math.trunc(0))
nlis.append(math.trunc(-5))
nlis.append(math.trunc(0.577))
nlis.append(math.trunc(1.618))
nlis.append(math.trunc(math.pi))
nlis.append(math.trunc(math.e))
nlis.append(math.trunc(math.tau))
print(nlis)




import sys
nlis = []
nlis.append(math.ulp(1))
nlis.append(math.ulp(0))
nlis.append(math.ulp(-5))
nlis.append(math.ulp(0.577))
nlis.append(math.ulp(1.618))
nlis.append(math.ulp(math.pi))
nlis.append(math.ulp(math.e))
nlis.append(math.ulp(math.tau))
nlis.append(math.ulp(math.nan))
nlis.append(math.ulp(math.inf))
nlis.append(math.ulp(-math.inf))
nlis.append(math.ulp(float('nan')))
nlis.append(math.ulp(float('inf')))
x = sys.float_info.max
nlis.append(math.ulp(x))
print(nlis)


