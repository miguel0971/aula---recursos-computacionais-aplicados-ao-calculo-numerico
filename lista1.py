import math

P1 = round(0.003456789, 5)
f1 = round(3.56789123, 5)
L1 = round(0.023456, 5)

t_real = 2.500
t_aprox = 2.463
pi_real = math.pi
pi_real_truncado = int(pi_real * 1000) / 1000
pi_aprox = 3.142

x_real = 0.785398
x_real_truncado = int(x_real * 1000) / 1000
x_aprox = 0.79
erroabsoluto = t_real - t_aprox
errorelativo = erroabsoluto / t_real * 100

print(f"{P1}\n{f1}\n{L1}\n\n{erroabsoluto:.3f}\n{errorelativo:.3f}\n\n{pi_real_truncado}\n{pi_aprox}\n\n{x_real_truncado}\n{x_aprox}")

