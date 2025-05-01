import numpy as np
from box_counting import box_counting_fd
from hurst_exponent import calculate_hurst
from petrosian_fd import petrosian_fd

# Genera una serie de datos aleatoria simulada
data = np.random.randn(1000)

# Prueba Box Counting
print(f"Box-counting FD: {box_counting_fd(data):.3f}")

# Prueba Exponente de Hurst
print(f"Hurst exponent: {calculate_hurst(data):.3f}")

# Prueba Petrosian FD
print(f"Petrosian FD: {petrosian_fd(data):.3f}")
