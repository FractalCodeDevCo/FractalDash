import numpy as np
import nolds

def calculate_hurst(data):
    """
    Calcula el exponente de Hurst para identificar persistencia o anti-persistencia fractal.
    :param data: Serie de datos (array numpy).
    :return: Exponente de Hurst (float).
    """
    return nolds.hurst_rs(data)
